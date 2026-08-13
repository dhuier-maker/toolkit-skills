# 交付流程（阶段 8）

## 8.1 交付前验证

进入交付阶段前，执行最终验证：

```
1. 读取 workflow-status.json，确认所有阶段状态为 completed
2. 检查关键产物文件是否存在：
   ├── doc/PRD.md
   ├── doc/API.md
   ├── doc/code-review-report.md（或 doc/.review-backend.md + doc/.review-frontend.md）
   └── doc/QA_Report.md
3. 确认无遗留 Critical 问题（reviewFindings.critical = 0 且 bugsRemaining.critical = 0）
4. 输出交付前验证报告
```

## 8.2 交付选项（结构化）

向用户展示以下交付选项：

| 选项 | 说明 | 适用场景 |
|------|------|---------|
| **① merge** | 合并到当前分支 | 功能开发完成，直接合并到主分支 |
| **② PR** | 创建 Pull Request | 需要代码审查后合并（推荐团队协作） |
| **③ keep** | 保留当前分支，不合并 | 需要后续继续开发或手动处理 |
| **④ discard** | 丢弃所有变更 | 开发结果不理想，放弃本次开发 |

**选项交互流程**：
```
📦 交付选项：

  ① merge  — 合并到当前分支（适合个人开发）
  ② PR     — 创建 Pull Request（推荐团队协作）
  ③ keep   — 保留分支，稍后手动处理
  ④ discard — 丢弃所有变更

请选择交付方式 [1-4]：
```

## 8.3 各选项执行流程

**① merge**：
```
1. git add 所有变更文件
2. git commit -m "feat: {项目名} 开发完成"
3. git merge 到主分支（如当前不在主分支）
4. 输出合并结果
```

**② PR**：
```
1. git add 所有变更文件
2. git commit -m "feat: {项目名} 开发完成"
3. git push -u origin {当前分支}
4. gh pr create --title "feat: {项目名}" --body "{PR描述}"
5. 输出 PR URL
```

**③ keep**：
```
1. 输出当前分支名和未提交文件列表
2. 提示用户稍后手动处理
3. 输出 git status 摘要
```

**④ discard**：
```
1. 确认用户选择（二次确认，防止误操作）
2. git checkout . （丢弃所有未提交变更）
3. 如在 worktree 中 → ExitWorktree(action: "remove")
4. 输出丢弃确认
```

## 8.4 Worktree 清理流程

如果 `worktreeMode = true`，在交付选项执行后自动触发 Worktree 清理：

```
交付选项执行完成
    ↓
检查 workflow-status.json 中 worktreeMode
    ↓
worktreeMode = true ?
    ├── 是 → 执行 Worktree 清理：
    │   1. 确认所有变更已合并/推送（merge 或 PR 选项）
    │   2. 调用 ExitWorktree(action: "remove") 清理工作树
    │   3. 输出清理结果
    │   4. 更新 workflow-status.json: worktreeMode = false
    │   └── 如果用户选择 keep → ExitWorktree(action: "keep")，保留工作树
    └── 否 → 跳过 Worktree 清理
```

**Worktree 清理安全检查**：
- 未提交的变更 → 警告用户，不自动清理
- 未合并的分支 → 提示用户先合并或创建 PR
- 清理前确认所有产物已保存到主工作区

**Worktree 清理失败处理**（v2.1.143 安全增强）：
- `git worktree remove` 失败时，平台不再回退到 `rm -rf`（防止丢失 gitignored 或进行中的文件）
- 处理流程：
  ```
  ExitWorktree(action: "remove") 失败
      ↓
  1. 输出警告：Worktree 清理失败，可能存在 gitignored 或进行中的文件
  2. 改为 ExitWorktree(action: "keep") 保留工作树
  3. 提示用户手动清理命令：
     > "Worktree 清理失败，工作树已保留。
     > 手动清理命令：git worktree remove {path}"
  4. 更新 workflow-status.json: worktreeCleanupStatus = "failed-kept"
  ```

## 8.5 交付报告

汇总所有产物，输出最终交付报告：

```
═══════════════════════════════════════════════════════════
📦 项目交付报告：{项目名}
═══════════════════════════════════════════════════════════

📊 开发统计：
├── 开发模式：{full/incremental}
├── 项目类型：{general/toolkit-bi-dashboard}
├── Worktree 模式：{是/否}
├── 总耗时：{startTime → now}
└── 模块数：{totalModules}（已完成 {completedModules}）

📄 产物清单：
├── 需求文档：doc/PRD.md
├── API 文档：doc/API.md
├── 代码审查：doc/code-review-report.md
├── 测试报告：doc/QA_Report.md
├── 后端代码：{directories.backend}
└── 前端代码：{directories.frontend}

🔍 质量指标：
├── Code Review Critical：0
├── Code Review Warning：{N}
├── BUG Critical：0
├── BUG Warning：{M}
└── 遗留 deferred 项：{K}

🚀 交付方式：{merge/PR/keep/discard}
├── 分支：{branchName}
├── PR URL：{url}（如适用）
└── Worktree 清理：{已清理/不适用/已保留/清理失败-已保留}

⚠️ 遗留项（如有）：
├── deferred BUG：{列表}
└── deferred Review 问题：{列表}
```
