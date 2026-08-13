# Agent Team 调度协议

当某个阶段可拆分为多个独立任务时，使用 Codex 子 Agent 并行执行，完成后汇总结果。

## 启动子 Agent

```
Agent({
  description: "简短描述（3-5 词）",
  prompt: "完整的自包含上下文简报。子 Agent 看不到主会话历史，必须包含所有必要信息。",
  subagent_type: "general-purpose" | "Explore",  // 按场景选择（见下表）
  model: "opus" | "sonnet" | "haiku",  // 可选，默认继承主 agent
  run_in_background: true
})
→ 返回 task_id（用于后续等待和结果获取）
```

## subagent_type 选择指南

| 场景 | subagent_type | 说明 |
|------|--------------|------|
| 代码搜索、文件定位、符号查找 | `"Explore"` | 只读搜索 Agent，速度快，适合定位代码位置 |
| 代码审查、代码生成、多步骤任务 | `"general-purpose"` | 全功能 Agent，可读写文件、执行命令 |

**典型用法**：
- 阶段 2 架构设计前，用 `Explore` Agent 快速扫描项目现有代码结构和依赖
- 阶段 6 代码审查前，用 `Explore` Agent 定位需要重点审查的文件
- 阶段 3/4/5/6 的实际执行任务，继续使用 `general-purpose`

## 等待完成

- 子 Agent 完成后，系统发送 `<task-notification>` 通知
- **完成通知包含耗时信息**（v2.1.144+）：如 "Agent completed · 3h 2m 5s"，可用于估算和进度报告
- 使用 `TaskOutput(task_id, block=true)` 获取结果（阻塞等待）

## Agent View 监控（v2.1.139+）

启动并行子 Agent 后，可通过 `claude agents` 命令查看所有后台会话状态：

```
# 列出所有后台会话
claude agents

# 按工作目录过滤
claude agents --cwd <path>

# 附加到运行中的 Agent 进行交互
# 在 Agent View 界面中选择目标会话
```

**应用场景**：
- 阶段 3/6 并行任务运行时，查看各 Agent 状态和耗时
- 子 Agent 长时间无响应时，附加进入排查问题
- BUG 修复循环中，监控修复 Agent 的执行进度

## 结果汇总

1. 使用 Read 工具读取各子 Agent 的输出文件
2. 合并为统一报告/产物
3. 更新 workflow-status.json

## 子 Agent 行为规范

每个子 Agent 在完成任务后，必须遵循以下行为规范：

### 状态报告格式

子 Agent 返回结果时，必须以以下四种状态之一开头：

| 状态 | 含义 | 格式 |
|------|------|------|
| `DONE` | 任务完成，结果符合预期 | `DONE: {完成摘要}` |
| `DONE_WITH_CONCERNS` | 任务完成，但有需要关注的问题 | `DONE_WITH_CONCERNS: {完成摘要}; CONCERNS: {问题列表}` |
| `BLOCKED` | 任务无法继续，需要外部输入 | `BLOCKED: {阻塞原因}; NEEDS: {需要的输入}` |
| `NEEDS_CONTEXT` | 缺少必要上下文，无法开始 | `NEEDS_CONTEXT: {缺少的信息}` |

### 自审要求

子 Agent 在报告 `DONE` 或 `DONE_WITH_CONCERNS` 前，必须执行自审：

1. **对照简报检查**：逐项核对简报中的输出要求是否全部完成
2. **边界验证**：检查输出是否超出简报范围（越界修改了不相关文件）
3. **质量自查**：检查关键输出是否存在明显错误（空文件、语法错误、遗漏关键逻辑）

自审发现问题 → 状态降级为 `DONE_WITH_CONCERNS` 并列出问题

### 升级机制

| 触发条件 | 升级动作 |
|----------|---------|
| 子 Agent 返回 `BLOCKED` | 主 Agent 评估阻塞原因，提供所需输入后重新启动子 Agent |
| 子 Agent 返回 `NEEDS_CONTEXT` | 主 Agent 补充上下文后重新启动子 Agent |
| 子 Agent 返回 `DONE_WITH_CONCERNS` 且 concerns 含 Critical | 主 Agent 评估 concerns，决定：接受并继续 / 重新启动子 Agent / 人工介入 |
| 子 Agent 连续 2 次返回相同 BLOCKED 原因 | 升级为用户干预，暂停工作流等待用户决策 |

### 环境持久化（v2.1.143）

子 Agent 在后台会话重生后自动保持以下配置（无需重新初始化）：
- **MCP 服务器连接** — 由平台 `/bg` 保留 `--mcp-config` 保证
- **模型和 effort level** — 由平台后台会话保留机制保证
- **项目设置** (`--settings`) — 由平台保留

如 MCP 连接仍丢失（极端场景），子 Agent 应：
1. 报告 `DONE_WITH_CONCERNS; CONCERNS: MCP {name} 连接丢失`
2. 主 Agent 评估：重试 / 降级 / 用户干预

### 简报模板（含行为规范提示）

```
Agent({
  description: "简短描述",
  prompt: `
    [任务简报内容]

    --- 行为规范 ---
    完成任务后，你必须以以下格式报告状态：
    - DONE: {完成摘要}
    - DONE_WITH_CONCERNS: {完成摘要}; CONCERNS: {问题列表}
    - BLOCKED: {阻塞原因}; NEEDS: {需要的输入}
    - NEEDS_CONTEXT: {缺少的信息}

    报告前执行自审：
    1. 对照简报逐项检查输出要求是否全部完成
    2. 检查是否越界修改了不相关文件
    3. 检查关键输出是否存在明显错误
    发现问题 → 降级为 DONE_WITH_CONCERNS
  `,
  subagent_type: "general-purpose" | "Explore",
  run_in_background: true
})
```

## 关键约束

| 约束 | 说明 |
|------|------|
| **独立上下文** | 每个子 Agent 需要完整的自包含简报，包含：阶段上下文、输入文件路径、输出要求、约束规则、行为规范提示 |
| **目录隔离** | 子 Agent 的输出目录必须不重叠，避免文件写入冲突 |
| **模型限制** | model 仅支持 `sonnet` / `opus` / `haiku`，不支持第三方模型（GLM、GPT 等） |
| **单次启动** | 同一批次的所有子 Agent 应在一条消息中同时启动 |
| **全部完成再汇总** | 等待所有子 Agent 完成后，再进行结果汇总和下一阶段 |
| **状态报告必选** | 子 Agent 必须返回标准状态报告（DONE/DONE_WITH_CONCERNS/BLOCKED/NEEDS_CONTEXT），不接受无状态格式的返回 |

## 适用阶段

| 阶段 | 并行任务 | 触发条件 |
|------|---------|---------|
| 阶段 3 | UI 原型 + toolkit-visual-asset-generator 资源生成 | 同时需要 UI + 图片/图表资源 |
| 阶段 6 | 后端代码审查 + 前端代码审查 | 全栈项目（前后端代码都存在） |
