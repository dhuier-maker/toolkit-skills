# 版本发布规范

## 版本号

采用语义化版本 `MAJOR.MINOR.PATCH`：

- `MAJOR`：删除或重命名 Skill、改变触发语义、引入不兼容目录结构。
- `MINOR`：新增 Skill、增加重要工作流或支持新的前端技术栈，保持兼容。
- `PATCH`：修正文案、规则、脚本和引用，不改变主要行为。

在 `1.0.0` 之前，可能不兼容的调整使用次版本号并在变更记录中标记“破坏性变更”。

## 发布前检查

1. 所有 Skill 通过 `quick_validate.py`。
2. README 的 Skill 数量与实际目录一致。
3. `SKILL.md` 的名称、目录名和 `agents/openai.yaml` 保持一致。
4. 至少选择一个真实前端项目完成核心 Skill 的冒烟验证。
5. 记录 lint、测试和构建的成功、失败及限制，不隐瞒工程基线问题。
6. 更新 `CHANGELOG.md` 和安装说明。
7. 确认未提交凭据、业务数据、构建产物、IDE 配置或本地缓存。

## Git 发布流程

```bash
git status
git diff --check
git add README.md INSTALL.md RELEASE.md CHANGELOG.md docs toolkit-skills
git commit -m "release: prepare vX.Y.Z"
git tag -a vX.Y.Z -m "toolkit-skills vX.Y.Z"
git push origin main
git push origin vX.Y.Z
```

发布前应人工查看暂存清单。只有仓库维护者或获得写权限的协作者能直接推送；其他人应通过 Fork 和 Pull Request 提交修改。

## 回滚

已发布版本不要改写同名标签。发现问题时创建修复提交并发布新的补丁版本；需要临时回退的使用者可检出上一标签后重新复制 Skill。
