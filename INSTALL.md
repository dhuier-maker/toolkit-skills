# 安装与更新

## 获取仓库

```bash
git clone https://github.com/dhuier-maker/toolkit-skills.git
cd toolkit-skills
```

## 项目级安装（推荐）

项目级 Skill 只对当前仓库生效。先在目标项目根目录创建目录：

```powershell
New-Item -ItemType Directory -Force .agents\skills | Out-Null
```

按需复制，例如安装前端开发、代码审查和 QA：

```powershell
Copy-Item -Recurse <下载目录>\toolkit-skills\toolkit-frontend-engineer .agents\skills\
Copy-Item -Recurse <下载目录>\toolkit-skills\toolkit-code-reviewer .agents\skills\
Copy-Item -Recurse <下载目录>\toolkit-skills\toolkit-qa-tester .agents\skills\
```

macOS/Linux：

```bash
mkdir -p .agents/skills
cp -R <下载目录>/toolkit-skills/toolkit-frontend-engineer .agents/skills/
```

重新打开项目任务或让 Codex 重新加载工作区后，使用 `$toolkit-frontend-engineer` 等名称调用。

## 用户级安装

只有明确希望所有项目都能调用时，才复制到用户级目录 `~/.agents/skills/`。团队项目优先使用项目级安装，避免不同项目之间的 Skill 版本互相影响。

## 更新

先在克隆目录获取最新版：

```bash
git pull --ff-only
```

再用最新版目录覆盖目标项目中已安装的同名 Skill。覆盖前先检查项目是否对 Skill 做过本地定制；有定制时使用 Git 对比后合并，不要直接覆盖。

推荐记录来源版本：

```bash
git describe --tags --always
```

## 卸载

从目标项目的 `.agents/skills/` 删除对应 `toolkit-*` 目录即可。卸载项目级 Skill 不会影响其他项目或 GitHub 仓库。

## 常见检查

- Skill 目录内必须存在 `SKILL.md`。
- `SKILL.md` 的 `name` 应与目录名一致。
- 复制的是单个 Skill 目录，不是把外层仓库整体放入 `.agents/skills/`。
- 更新后若未生效，重新加载工作区或新建 Codex 任务。
