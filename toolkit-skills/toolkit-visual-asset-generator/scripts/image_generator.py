#!/usr/bin/env python3
"""
图片生成器 - 精简版
支持从配置文件读取 API 参数，调用 GPT-Image-2 或兼容 API
"""

import os
import sys
import json
import time
import base64
import argparse
import requests
from pathlib import Path
from datetime import datetime
from typing import Optional, Dict, Any

# 默认配置
DEFAULT_CONFIG = {
    "api": {
        "base_url": "https://api.apimart.ai/v1",
        "api_key_env": "OPENAI_API_KEY",
        "model": "gpt-image-2",
        "timeout": 30,
        "max_wait": 120,
        "poll_interval": 5
    },
    "output": {
        "directory": "doc/images",
        "filename_pattern": "{timestamp}_{brief}.png",
        "save_metadata": True
    },
    "defaults": {
        "task": "poster",
        "direction": "balanced",
        "aspect": "3:4",
        "quality": "final"
    },
    "tasks": {
        "poster": {"aspect": "3:4", "description": "海报"},
        "article": {"aspect": "16:9", "description": "文章封面"},
        "ppt": {"aspect": "16:9", "description": "PPT配图"},
        "slide-full": {"aspect": "16:9", "description": "整页幻灯片（发布会级）"},
        "product": {"aspect": "1:1", "description": "商品图"},
        "banner": {"aspect": "16:9", "description": "Banner"},
        "social": {"aspect": "1:1", "description": "社交媒体图"},
        "bi-background": {"aspect": "16:9", "description": "BI大屏背景"}
    },
    "aspects": {
        "1:1": "2048x2048",
        "3:4": "1728x2304",
        "4:3": "2304x1728",
        "16:9": "2848x1600",
        "9:16": "1600x2848"
    }
}


def find_config_path() -> Path:
    """查找配置文件路径"""
    candidates = [
        Path.cwd() / "doc" / "image-gen-config.json",
        Path.cwd().parent / "doc" / "image-gen-config.json",
        Path.home() / ".claude" / "image-gen-config.json",
    ]
    for p in candidates:
        if p.exists():
            return p
    return candidates[0]


def load_config(config_path: Optional[Path] = None) -> Dict[str, Any]:
    """加载配置文件"""
    if config_path is None:
        config_path = find_config_path()

    if config_path.exists():
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                user_config = json.load(f)
            config = DEFAULT_CONFIG.copy()
            for key in user_config:
                if isinstance(user_config[key], dict) and key in config:
                    config[key] = {**config[key], **user_config[key]}
                else:
                    config[key] = user_config[key]
            return config
        except Exception as e:
            print(f"⚠️ 配置文件加载失败: {e}，使用默认配置")
    return DEFAULT_CONFIG


def get_api_key(config: Dict[str, Any]) -> str:
    """获取 API Key

    支持两种方式：
    1. 从配置文件直接读取 api_key 字段
    2. 从环境变量读取（通过 api_key_env 指定变量名）
    """
    api_config = config.get("api", {})

    # 方式1：直接从配置文件读取
    if api_config.get("api_key"):
        return api_config["api_key"]

    # 方式2：从环境变量读取
    api_key_env = api_config.get("api_key_env", "OPENAI_API_KEY")
    api_key = os.environ.get(api_key_env)

    if not api_key:
        raise RuntimeError(
            f"❌ 未设置 API Key。请在配置文件中设置 api_key，"
            f"或设置环境变量: export {api_key_env}='sk-...'"
        )
    return api_key


def compile_prompt(brief: str, task: str, direction: str = "balanced") -> str:
    """编译生成 Prompt"""
    task_profiles = {
        "poster": {
            "goal": "吸引注意力，传达活动信息",
            "style": "editorial campaign key visual, premium poster design",
            "constraints": "clean hierarchy, text-safe zone, disciplined background"
        },
        "product": {
            "goal": "展示产品特点，激发购买欲望",
            "style": "high-end commercial product photography",
            "constraints": "product as hero, clean background, material fidelity"
        },
        "ppt": {
            "goal": "支持演示叙事，视觉隐喻",
            "style": "presentation cover art, clean visual metaphor",
            "constraints": "readable from distance, space for title overlay"
        },
        "slide-full": {
            "goal": "整页幻灯片，发布会级视觉冲击力",
            "style": "high-impact keynote slide, cinematic composition, premium editorial design",
            "constraints": "1920x1080 slide format, strong visual hierarchy, space for title and key data, professional finish"
        },
        "banner": {
            "goal": "品牌展示，吸引点击",
            "style": "premium banner design, web-ready visual",
            "constraints": "horizontal composition, clear focal point"
        },
        "social": {
            "goal": "社交传播，引发互动",
            "style": "social media ready, eye-catching square format",
            "constraints": "square composition, mobile-friendly"
        },
        "article": {
            "goal": "吸引点击，传达文章主题",
            "style": "editorial cover art, blog hero image, premium publication style",
            "constraints": "strong typography space, visual hierarchy, share-friendly composition"
        },
        "bi-background": {
            "goal": "数据可视化背景，科技感氛围",
            "style": "futuristic data visualization background, tech aesthetic, dark gradient with light accents",
            "constraints": "non-distracting background, clear data overlay zone, blue/cyan dominant palette, grid or particle elements"
        }
    }

    profile = task_profiles.get(task, task_profiles["poster"])

    direction_hints = {
        "conservative": "clean, corporate, polished, lower-risk",
        "balanced": "premium editorial, contemporary, commercially strong",
        "bold": "dramatic, high-contrast, vivid, assertive"
    }

    prompt = f"""Create a {task} image. {profile['goal']}.

Brief: {brief}

Style: {profile['style']}, {direction_hints.get(direction, direction_hints['balanced'])}.

Constraints: {profile['constraints']}.
Avoid: random HUD overlays, generic fog, empty gradients, floating debris, AI slop tropes.

Emphasize strong hierarchy, intentional whitespace, and polished professional finish."""

    return prompt.strip()


def submit_task(
    prompt: str,
    aspect: str,
    config: Dict[str, Any],
    api_key: str,
    reference_image: Optional[str] = None
) -> Dict[str, Any]:
    """提交图片生成任务"""
    base_url = config["api"]["base_url"]
    model = config["api"]["model"]
    timeout = config["api"]["timeout"]

    url = f"{base_url}/images/generations"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": model,
        "prompt": prompt,
        "n": 1,
        "size": aspect
    }

    if reference_image and os.path.exists(reference_image):
        try:
            with open(reference_image, 'rb') as f:
                img_bytes = f.read()
            b64 = base64.b64encode(img_bytes).decode('utf-8')
            ext = Path(reference_image).suffix.lstrip('.') or 'png'
            data["image_urls"] = [f"data:image/{ext};base64,{b64}"]
            print(f"   📎 参考图: {Path(reference_image).name}")
        except Exception as e:
            print(f"   ⚠️ 参考图处理失败: {e}")

    print(f"   📤 提交任务...")
    print(f"   📝 Prompt: {prompt[:80]}...")
    print(f"   📐 Size: {aspect}")

    response = requests.post(url, headers=headers, json=data, timeout=timeout)
    response.raise_for_status()
    result = response.json()

    if result.get("code") == 200:
        task_id = result["data"][0]["task_id"]
        print(f"   ✅ 任务已提交: {task_id}")
        return {"success": True, "task_id": task_id}
    else:
        error_msg = result.get("error", {}).get("message", "Unknown error")
        print(f"   ❌ 提交失败: {error_msg}")
        return {"success": False, "error": error_msg}


def wait_for_completion(
    task_id: str,
    config: Dict[str, Any],
    api_key: str
) -> Dict[str, Any]:
    """轮询等待任务完成"""
    base_url = config["api"]["base_url"]
    max_wait = config["api"].get("max_wait", 120)
    poll_interval = config["api"].get("poll_interval", 5)

    print(f"   ⏳ 等待生成完成...")
    time.sleep(10)

    url = f"{base_url}/tasks/{task_id}"
    headers = {"Authorization": f"Bearer {api_key}"}

    start_time = time.time()
    attempts = 0

    while time.time() - start_time < max_wait:
        attempts += 1
        elapsed = int(time.time() - start_time)

        try:
            response = requests.get(url, headers=headers, timeout=30)
            response.raise_for_status()
            result = response.json()
        except Exception as e:
            print(f"   ⚠️ 查询失败: {e}")
            time.sleep(poll_interval)
            continue

        if result.get("code") != 200:
            error_msg = result.get("error", {}).get("message", "Query failed")
            return {"success": False, "error": error_msg}

        task_data = result["data"]
        status = task_data.get("status")
        progress = task_data.get("progress", 0)

        if status == "completed":
            print(f"   ✅ 生成完成! (耗时 {elapsed}s)")
            return {"success": True, "data": task_data}
        elif status == "failed":
            error_msg = task_data.get("error", {}).get("message", "Task failed")
            return {"success": False, "error": error_msg}
        else:
            print(f"   🔄 {status} ({progress}%) [{elapsed}s]", end="\r")
            time.sleep(poll_interval)

    return {"success": False, "error": "Timeout"}


def download_image(
    image_url: str,
    save_path: str,
    max_retries: int = 3
) -> bool:
    """下载图片（支持重试）"""
    for attempt in range(1, max_retries + 1):
        try:
            print(f"   📥 下载中... (attempt {attempt})")
            response = requests.get(image_url, stream=True, timeout=300)
            response.raise_for_status()

            with open(save_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)

            file_size = os.path.getsize(save_path) / 1024
            print(f"   ✅ 已保存: {save_path} ({file_size:.1f} KB)")
            return True
        except Exception as e:
            print(f"   ⚠️ 下载失败: {str(e)[:50]}")
            time.sleep(2)

    return False


def generate(
    brief: str,
    task: Optional[str] = None,
    aspect: Optional[str] = None,
    direction: str = "balanced",
    reference_image: Optional[str] = None,
    style_ref: Optional[str] = None,
    config_path: Optional[Path] = None,
    save_metadata: bool = True
) -> Dict[str, Any]:
    """
    生成图片的主函数

    Args:
        brief: 图片描述
        task: 任务类型 (poster/product/ppt/slide-full/banner/social)
        aspect: 图片比例 (1:1/3:4/16:9/9:16/4:3)
        direction: 风格方向 (conservative/balanced/bold)
        reference_image: 参考图片路径（可选）
        style_ref: 风格参考文本（可选，用于 slide-full，传入 grammar 描述）
        config_path: 配置文件路径（可选）
        save_metadata: 是否保存元数据

    Returns:
        生成结果字典
    """
    # 输入验证
    if not brief or not brief.strip():
        return {"success": False, "error": "❌ 图片描述不能为空"}

    brief = brief.strip()
    if len(brief) > 500:
        brief = brief[:500]
        print(f"   ⚠️ 描述过长，已截断为 500 字符")

    # 1. 加载配置
    config = load_config(config_path)

    # 2. 确定参数
    task = task or config["defaults"]["task"]
    direction = direction or config["defaults"]["direction"]

    # 从任务类型获取默认比例
    if aspect is None:
        if task in config.get("tasks", {}):
            aspect = config["tasks"][task].get("aspect", "1:1")
        else:
            aspect = config["defaults"]["aspect"]

    # 3. 确保输出目录存在
    output_dir = Path(config["output"]["directory"])
    if not output_dir.is_absolute():
        if config_path and config_path.exists():
            output_dir = config_path.parent.parent / output_dir
        else:
            output_dir = Path.cwd() / output_dir
    output_dir.mkdir(parents=True, exist_ok=True)

    # 4. 获取 API Key
    try:
        api_key = get_api_key(config)
    except RuntimeError as e:
        return {"success": False, "error": str(e)}

    print(f"\n{'='*60}")
    print(f"🎨 图片生成")
    print(f"{'='*60}")
    print(f"📝 需求: {brief}")
    print(f"📦 类型: {task} | 比例: {aspect} | 风格: {direction}")
    print()

    # 5. 编译 Prompt
    prompt = compile_prompt(brief, task, direction)
    # slide-full 可追加风格参考文本
    if style_ref:
        prompt = f"{prompt}\n\nStyle Guide:\n{style_ref}"

    # 6. 提交任务
    submit_result = submit_task(prompt, aspect, config, api_key, reference_image)
    if not submit_result["success"]:
        return {"success": False, "error": submit_result.get("error")}

    task_id = submit_result["task_id"]

    # 7. 等待完成
    wait_result = wait_for_completion(task_id, config, api_key)
    if not wait_result["success"]:
        return {"success": False, "error": wait_result.get("error")}

    task_data = wait_result["data"]

    # 8. 提取图片 URL
    images = task_data.get("result", {}).get("images", [])
    if not images or not images[0].get("url"):
        return {"success": False, "error": "No image URL in result"}

    image_url = images[0]["url"][0]

    # 9. 下载图片
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    safe_name = "".join(c if c.isalnum() or c in "_-" else "_" for c in brief[:20])
    filename = f"{timestamp}_{safe_name}.png"
    filepath = output_dir / filename

    if not download_image(image_url, str(filepath)):
        url_file = filepath.with_suffix(".url.txt")
        with open(url_file, 'w') as f:
            f.write(image_url)
        print(f"   ⚠️ 下载失败，URL 已保存: {url_file}")
        filepath = url_file

    # 10. 保存元数据
    if save_metadata:
        meta = {
            "timestamp": datetime.now().isoformat(),
            "brief": brief,
            "task": task,
            "aspect": aspect,
            "direction": direction,
            "prompt": prompt,
            "task_id": task_id,
            "image_url": image_url,
            "filepath": str(filepath),
            "actual_time": task_data.get("actual_time"),
            "model": config["api"]["model"]
        }
        meta_file = filepath.with_suffix(".json")
        with open(meta_file, 'w', encoding='utf-8') as f:
            json.dump(meta, f, indent=2, ensure_ascii=False)

    print(f"\n{'='*60}")
    print(f"✅ 完成!")
    print(f"{'='*60}")
    print(f"📁 文件: {filepath}")
    print(f"🔗 URL: {image_url[:60]}...")
    print(f"⚠️  链接 24h 有效")

    return {
        "success": True,
        "filepath": str(filepath),
        "url": image_url,
        "task_id": task_id,
        "prompt": prompt
    }


def generate_batch(
    tasks: list,
    direction: str = "balanced",
    config_path: Optional[Path] = None,
    save_metadata: bool = True,
    parallel: bool = False,
    style_ref: Optional[str] = None
) -> Dict[str, Any]:
    """
    批量生成图片

    Args:
        tasks: 任务列表，每个任务是一个字典，包含:
            - brief: 图片描述（必需）
            - task: 任务类型（可选）
            - aspect: 图片比例（可选）
            - reference_image: 参考图片路径（可选）
        direction: 风格方向 (conservative/balanced/bold)
        config_path: 配置文件路径（可选）
        save_metadata: 是否保存元数据
        parallel: 是否并行执行（注意：可能受 API 速率限制）
        style_ref: 风格参考文本（可选，用于 slide-full）

    Returns:
        批量生成结果字典
    """
    if not tasks:
        return {"success": False, "error": "❌ 任务列表不能为空"}

    results = []
    success_count = 0
    failed_count = 0

    print(f"\n{'='*60}")
    print(f"🎨 批量图片生成")
    print(f"{'='*60}")
    print(f"📝 任务数量: {len(tasks)}")
    print(f"⚡ 执行模式: {'并行' if parallel else '顺序'}")
    print()

    for i, task_item in enumerate(tasks, 1):
        brief = task_item.get("brief")
        if not brief:
            print(f"   ⚠️ 任务 {i}: 缺少 brief，跳过")
            failed_count += 1
            results.append({"success": False, "error": "Missing brief"})
            continue

        print(f"\n[{i}/{len(tasks)}] 处理: {brief[:50]}...")

        result = generate(
            brief=brief,
            task=task_item.get("task"),
            aspect=task_item.get("aspect"),
            direction=direction,
            reference_image=task_item.get("reference_image"),
            style_ref=task_item.get("style_ref") or style_ref,
            config_path=config_path,
            save_metadata=save_metadata
        )

        results.append(result)

        if result.get("success"):
            success_count += 1
        else:
            failed_count += 1

    print(f"\n{'='*60}")
    print(f"📊 批量生成完成")
    print(f"{'='*60}")
    print(f"✅ 成功: {success_count}")
    print(f"❌ 失败: {failed_count}")

    return {
        "success": failed_count == 0,
        "total": len(tasks),
        "success_count": success_count,
        "failed_count": failed_count,
        "results": results
    }


def main():
    """命令行入口"""
    parser = argparse.ArgumentParser(description="图片生成器")
    parser.add_argument("brief", help="图片描述")
    parser.add_argument("--task", "-t", choices=["poster", "article", "product", "ppt", "slide-full", "banner", "social", "bi-background"],
                       default="poster", help="任务类型")
    parser.add_argument("--aspect", "-a", default=None, help="图片比例 (1:1/3:4/16:9)")
    parser.add_argument("--direction", "-d", choices=["conservative", "balanced", "bold"],
                       default="balanced", help="风格方向")
    parser.add_argument("--reference", "-r", default=None, help="参考图片路径")
    parser.add_argument("--style-ref", "-s", default=None, help="风格参考文本（用于 slide-full）")
    parser.add_argument("--config", "-c", default=None, help="配置文件路径")
    parser.add_argument("--batch", "-b", default=None, help="批量任务 JSON 文件路径")

    args = parser.parse_args()

    config_path = Path(args.config) if args.config else None

    # 批量模式
    if args.batch:
        batch_file = Path(args.batch)
        if not batch_file.exists():
            print(f"❌ 批量任务文件不存在: {batch_file}")
            sys.exit(1)

        try:
            with open(batch_file, 'r', encoding='utf-8') as f:
                tasks = json.load(f)
        except Exception as e:
            print(f"❌ 读取批量任务文件失败: {e}")
            sys.exit(1)

        if not isinstance(tasks, list):
            print("❌ 批量任务文件必须是 JSON 数组格式")
            sys.exit(1)

        result = generate_batch(
            tasks=tasks,
            direction=args.direction,
            config_path=config_path,
            style_ref=args.style_ref
        )

        if not result["success"]:
            sys.exit(1)
        return

    # 单张模式
    result = generate(
        brief=args.brief,
        task=args.task,
        aspect=args.aspect,
        direction=args.direction,
        reference_image=args.reference,
        style_ref=args.style_ref,
        config_path=config_path
    )

    if not result["success"]:
        print(f"\n❌ 生成失败: {result.get('error')}")
        sys.exit(1)


if __name__ == "__main__":
    main()
