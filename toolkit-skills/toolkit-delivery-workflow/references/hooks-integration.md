# 钩子集成

## PostToolUse 钩子（可选）

Codex v2.1.139 增强了钩子能力，v2.1.141 新增 `terminalSequence` 类型。toolkit-delivery-workflow 可与以下钩子配合提升工作流体验：

**终端通知（v2.1.141+）**：配置 `terminalSequence` 类型钩子，实现阶段转换实时反馈：

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write",
        "hooks": [
          {
            "type": "command",
            "command": "echo 'Workflow updated' >> .workflow-notify.log"
          },
          {
            "type": "terminalSequence",
            "sequence": [
              {"action": "setTitle", "title": "[{当前阶段}] {项目名}"},
              {"action": "notify", "title": "阶段完成", "body": "{阶段名}已完成，{摘要}"},
              {"action": "bell"}
            ]
          }
        ]
      }
    ]
  }
}
```

**应用场景**：
- 阶段转换时更新终端窗口标题，显示当前阶段和项目名
- BUG 修复循环每轮结束后桌面通知，避免用户长时间不看终端
- 交付完成时铃声提醒
- 长时间运行的并行任务完成时推送通知

## PreCompact 钩子（v2.1.105+）

长时间运行的工作流（尤其是 BUG 修复循环）容易耗尽上下文，压缩时可能丢失关键状态。配置 PreCompact 钩子在压缩前自动保存关键状态：

```json
{
  "hooks": {
    "PreCompact": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "echo 'Context compaction imminent - workflow state saved to doc/workflow-status.json' >> .workflow-notify.log"
          }
        ]
      }
    ]
  }
}
```

**PreCompact 与工作流配合**：
- 压缩前自动读取 `doc/workflow-status.json` 保存当前阶段和进度
- 压缩后自动恢复工作流状态，确保不丢失阶段信息
- BUG 修复循环中建议主动使用 `/recap`（v2.1.108）保持上下文清晰
- 并行子 Agent 运行期间避免压缩，等待所有子 Agent 完成后再压缩

## 钩子配置安全

配置钩子时注意以下安全约束：
- 钩子命令不应阻塞超过 30 秒，否则影响工作流推进
- 钩子连续阻塞 ≥ 8 次时，平台会自动以警告结束当前回合（可通过 `CLAUDE_CODE_STOP_HOOK_BLOCK_CAP` 覆盖）
- 避免在钩子中执行需要用户交互的命令（如 `read -p`）
- 钩子命令失败不应阻止工作流主流程
