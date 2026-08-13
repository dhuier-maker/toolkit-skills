# Image-Based Slide 工作流

用 GPT-Image-2 生成整页幻灯片图片，再合成 PPTX 的完整流水线。适合需要发布会级视觉冲击力、不要求文字可编辑的场景。

**与 HTML 幻灯片的区别**：

| 维度 | HTML 幻灯片 | Image-Based Slide |
|------|------------|------------------|
| 文字可编辑 | ✅ 可（html2pptx） | ❌ 图片型 PPTX |
| 视觉丰富度 | CSS/渐变/ECharts | GPT-Image-2 渲染（光影/材质/真实感） |
| 适用场景 | 需要改稿的汇报/课件 | 品牌发布/pitch deck/不可改稿的展示 |

---

## 什么时候走这条路径

满足以下任一条件时走本工作流：
- 用户要求「发布会级」「pitch deck」「高级感」
- 用户接受 PPTX 不可编辑文字
- 需要产品渲染图/真实场景图作为 slide 背景

满足以下任一条件时走 HTML 幻灯片路径：
- 用户需要可编辑 PPTX
- 课件/培训/汇报类（可能需要改文字）
- 纯数据图表类（用 ECharts 更精确）

---

## 完整流程

### Step 1 · 判断走本工作流

在工作流 Step 1（交付格式确认）中明确询问：

> 这个 PPT 的用途是？...
> - **演讲/发布**：视觉优先，不需要在 PPT 里改文字 → 走 image-based slide
> - **汇报/课件**：需要在 PPT 里改文字 → 走 HTML 幻灯片 → export_deck_pptx.mjs

用户选择「演讲/发布」时，本工作流启动。

---

### Step 2 · 完成前置准备（共用主流程步骤）

1. **完成 showcase 2 页 grammar**（toolkit-experience-designer 标准流程 Step 3-4）
2. **产出 `outline.md`**（showcase 确认后、批量推页面前，见 slide-decks.md「outline.md 步骤」）
3. **固化 grammar 为风格描述文本**

grammar 示例：
```markdown
## Grammar

- 背景：深蓝渐变 #0d1b2a → #1a3a5c，光点粒子
- 字体：主标题 80pt bold，副标题 40pt regular
- 配色：#00d4ff（主色）、#ffd700（强调）、#ffffff（文字）
- 布局：标题居中上方，内容区中下，右侧留图
- 风格：科技感、数据可视化、电影级渲染
```

---

### Step 3 · 生成 per-page prompts

为 `outline.md` 中每一页生成独立 prompt 文件：

```
我的Deck/
├── outline.md
├── prompts/                    # ← 新建 prompts 目录
│   ├── 01-cover.md
│   ├── 02-agenda.md
│   ├── 03-problem.md
│   ├── ...
```

**每页 prompt 模板**（复制后填写）：

```markdown
# Slide N - {标题}

## 风格约束（来自 grammar）
（粘贴 grammar 中的风格描述）

## 页面内容
（来自 outline.md 的关键内容）

## Prompt
Write a prompt for GPT-Image-2 to generate this full slide image.
```

**生成 prompt 示例**（封面页）：

```markdown
# Slide 1 - 封面

## 风格约束（来自 grammar）
- 深蓝渐变背景 #0d1b2a → #1a3a5c + 光点粒子
- 配色：#00d4ff（主色）、#ffd700（强调）、#ffffff（文字）
- 科技感、数据可视化、电影级渲染
- 标题居中上方，副标题居下

## 页面内容
- 主标题：智慧乡村数据平台
- 副标题：2026年数字化转型成果汇报

## Prompt（最终生成给 GPT-Image-2）
Create a full-slide 16:9 presentation cover image for "智慧乡村数据平台".
Style: tech-blue keynote aesthetic, dark gradient background (#0d1b2a → #1a3a5c), floating light particles,
cyan accent (#00d4ff), cinematic rendering, premium presentation feel.
Layout: centered title at top, subtitle below, right side reserved for product visual.
Text to incorporate: "智慧乡村数据平台" as main title, "2026年数字化转型成果汇报" as subtitle.
High contrast, professional finish, no text rendering artifacts.
```

---

### Step 4 · 批量生成图片（支持并行）

**单张生成**：
```bash
python scripts/image_generator.py "GPT-Image-2 prompt..." \
  --task slide-full \
  --style-ref "$(cat grammar.txt)" \
  --out deck/slide-01.png
```

**批量生成**（batch_tasks.json）：
```json
[
  {"brief": "封面 slide prompt", "task": "slide-full", "style_ref": "grammar 文本"},
  {"brief": "议程 slide prompt", "task": "slide-full", "style_ref": "grammar 文本"},
  ...
]
```

```bash
python scripts/image_generator.py --batch batch_tasks.json
```

**并行出图**（利用 toolkit-delivery-workflow Agent Team）：
- 将 prompts 目录按每 5 页一组拆分
- 启动多个子 Agent 并行生成各组图片
- 各组图片输出到 `doc/images/slides/group-N/` 下
- 最后合并到 `doc/images/slides/` 主目录

---

### Step 5 · 合成 PPTX

**方式 A：图片铺满 PPTX**（最简，适合 image-based）

```python
import pptxgen
from pathlib import Path

def build_slide_pptx(slides_dir, output_path):
    pres = pptxgen()
    pres.layout = 'LAYOUT_WIDE'  # 13.333 x 7.5 inch

    for img_path in sorted(Path(slides_dir).glob("*.png")):
        slide = pres.addSlide()
        # 全幅铺满图片（无文字层，因为文字已烧录在图里）
        slide.background = {'color': 'ffffff'}
        slide.addImage(str(img_path), {
            'x': 0, 'y': 0,
            'w': '100%', 'h': '100%',
            'stretch': True
        })

    pres.writeFile(str(output_path))
```

**方式 B：图片 + 备注区**（推荐，保留演讲稿）

1. `speaker-notes.md` 自动生成（已在 P0 中实现）
2. 每张 slide 图片铺满背景
3. `slide.addNotes()` 写入备注

---

### Step 6 · 单页迭代

用户指出第 N 页不满意时：

1. 修改 `prompts/N-slide-name.md` 中的 prompt
2. 重新生成第 N 页图片（不影响其他页）
3. 重新合成 PPTX

```bash
# 只需重做第 N 页
python scripts/image_generator.py "$(cat prompts/03-problem.md | grep '## Prompt' -A 20)" \
  --task slide-full \
  --style-ref "$(cat grammar.txt)" \
  --out deck/slides/slide-03.png
```

---

### Fallback：生图失败

当某一页连续 3 次生图失败时，降级为**纯色背景 + 大标题**方案：

```markdown
降级 Prompt：
Create a minimal full-slide image with solid dark blue background (#0d1b2a),
large centered white bold title text "[实际标题]",
no decorative elements, professional presentation slide background only.
```

生成的降级图 + 备注中注明「该页以文本为主，如需更丰富视觉请手动处理」。

---

## 目录最终结构

```
我的Deck/
├── index.html                  # 预览用（可不生成）
├── outline.md                # 大纲
├── speaker-notes.md          # 演讲备注（自动生成）
├── grammar.md               # 风格描述（来自 showcase）
├── prompts/                 # 每页 prompt
│   ├── 01-cover.md
│   ├── 02-agenda.md
│   └── ...
├── doc/images/slides/       # 生成后的图片
│   ├── slide-01.png
│   ├── slide-02.png
│   └── ...
└── deck.pptx                # 最终交付物
```

---

## 关键原则

1. **prompt 是核心资产**：`prompts/*.md` 是半成品，改 prompt 比改 HTML 更轻量
2. **grammar 一次固化**：风格约束只写一次，所有 page prompt 引用它
3. **单页独立重生**：任意页可单独修改 prompt → 重生 → 重新合成，不影响其他页
4. **降级诚实**：GPT-Image-2 无法稳定生成的页（如精确数据图表），降级为纯色背景 + 标题，备注中标明
5. **不追求可编辑**：image-based slide 的定位是「视觉最大化」，不要在合成阶段试图做 pptxgenjs 手写文字层
