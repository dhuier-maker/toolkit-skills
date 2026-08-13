# 工作流中断恢复机制

## 一、中断检测

每次进入工作流时，首先检查 `doc/workflow-status.json`：

- `currentPhase` 为 `null` 或文件不存在 → 全新启动
- `currentPhase` 为 `delivered` → 项目已完成，询问是否开始新项目
- `currentPhase` 为其他值 → **检测到中断**，进入恢复流程

检测命令：
```bash
python scripts/check_workflow_status.py --json
```

---

## 二、恢复流程

```
检测到中断
    │
    ▼
读取 doc/workflow-status.json
    │
    ▼
解析 currentPhase、phaseHistory、developmentProgress
    │
    ▼
根据 currentPhase 判断恢复点
    │
    ▼
输出中断摘要，提供恢复选项
```

---

## 三、各阶段恢复点

### 主开发流程恢复点

| currentPhase | 恢复行为 | 保留状态 |
|-------------|---------|---------|
| `config-init` | 重新执行配置初始化 | - |
| `demand-confirm` | 展示已有 PRD，等待用户确认 | PRD.md |
| `architecting` | 从架构设计继续，保留已设计的 API | API.md、api/*.md |
| `prototyping` | 从 UI 原型继续，检查 sub-Agent 并行状态 | prototypes/*、stage3_ui/stage3_image 状态 |
| `backend-dev` | 恢复后端模块开发进度 | developmentProgress.backend |
| `frontend-dev` | 恢复前端模块开发进度 | developmentProgress.frontend |
| `code-review` | 从代码审查继续，检查 sub-Agent 并行状态 | reviewFindings、stage6_backend_review/stage6_frontend_review 状态 |
| `testing` | 从测试继续，保留已发现的 BUG | bugsFound、QA_Report.md |
| `bugfix` | 恢复 BUG 修复循环，保持降级计数 | bugFixRemediation、bugFixHistory |
| `delivered` | 项目已完成 | 全部产物 |

### 并行开发恢复

当 `currentPhase` 为 `backend-dev` 或 `frontend-dev` 时，需额外检查并行任务状态：

```json
"parallelTasks": {
  "backend": { "status": "completed", "completedAt": "..." },
  "frontend": { "status": "in_progress" }
}
```

- 后端已完成、前端中断 → 仅恢复前端开发
- 后端中断、前端已完成 → 仅恢复后端开发
- 两者均中断 → 按优先级恢复（通常先恢复未完成的一方）

### Agent Team 并行恢复（阶段 3 和阶段 6）

当 `currentPhase` 为 `prototyping` 或 `code-review` 时，需检查 sub-Agent 并行状态：

**阶段 3 恢复（prototyping）**：

```json
"parallelTasks": {
  "stage3_ui": { "agentId": "xxx", "status": "completed" },
  "stage3_image": { "agentId": "yyy", "status": "failed" }
}
```

| 状态组合 | 恢复行为 |
|----------|---------|
| 都完成 | 直接整合结果，进入阶段 3.5 |
| UI 完成、toolkit-visual-asset-generator 失败 | 仅重试 toolkit-visual-asset-generator Agent，完成后整合 |
| UI 失败、toolkit-visual-asset-generator 完成 | 仅重试 UI Agent，完成后整合 |
| 都失败 | 重新启动两个 Agent，或回退到顺序执行 |

**阶段 6 恢复（code-review）**：

```json
"parallelTasks": {
  "stage6_backend_review": { "agentId": "aaa", "model": "opus", "status": "completed" },
  "stage6_frontend_review": { "agentId": "bbb", "model": "sonnet", "status": "in_progress" }
}
```

| 状态组合 | 恢复行为 |
|----------|---------|
| 都完成 | 直接读取结果，合并生成 code-review-report.md |
| backend 完成、frontend 失败 | 仅重试 frontend Agent，完成后合并 |
| backend 失败、frontend 完成 | 仅重试 backend Agent，完成后合并 |
| 都失败 | 重新启动两个 Agent，或回退到单 Agent 顺序审查 |

**Agent Team 恢复原则**：
- 已完成的 Agent 结果**不丢弃**，仅重试失败的 Agent
- 重试时使用相同的上下文简报
- 连续 3 次 Agent 失败 → 降级为顺序执行（主 Agent 直接调用 Skill）


---

## 四、恢复输出模板

### 标准中断恢复

```
🔄 检测到项目「{projectName}」在阶段「{currentPhaseChinese}」中断

| 信息 | 值 |
|------|----|
| 当前阶段 | {currentPhaseChinese} |
| 开发进度 | {completedModules}/{totalModules} 模块已完成 |
| BUG 统计 | 发现 {bugsFound} / 修复 {bugsFixed} / 剩余 {bugsRemaining} |
| 最近更新 | {lastUpdate} |

请选择：
- 输入「继续」从断点恢复
- 输入「重新开始」从头开始（将重置状态文件）
- 输入「状态」查看详细状态摘要
```

### 修复循环中断恢复

当 `currentPhase` 为 `bugfix` 或修复降级记录中有数据时：

```
🔄 检测到修复循环中断

| 信息 | 值 |
|------|----|
| 修复轮次 | 第 {iteration} 轮 |
| 无进步轮次 | {noProgressCount}/3 |
| 上轮结果 | {result} |
| 已 defer | {deferredCount} |
| 已简化 | {simplifiedCount} |

⚠️ 当前降级级别：{degradationLevel}

请选择：
- 输入「继续」从当前轮次恢复
- 输入「跳过」标记为遗留，进入交付
```

---

## 五、场景恢复策略

### 5.1 上下文溢出恢复

当 Codex 上下文窗口溢出导致会话中断：

1. 新会话中读取 `doc/workflow-status.json` 判断当前阶段
2. 读取对应阶段的产物文件（PRD.md、API.md、QA_Report.md 等）
3. 使用阶段产物（而非历史对话）重建上下文
4. 从 `currentPhase` 指定的阶段继续执行

**关键原则**：状态文件和产物文件是上下文重建的唯一可靠来源，不依赖历史对话记忆。

### 5.2 会话断连恢复

当网络断开或 Codex 崩溃导致会话终止：

1. 重启后触发 `toolkit-delivery-workflow`（输入"继续项目"或触发词）
2. 自动检测 `workflow-status.json` 中的 `currentPhase`
3. 对照 `phaseHistory` 确认最后完成的阶段
4. 从断点继续，保留所有计数器和进度

### 5.3 用户主动暂停/恢复

**暂停**：用户输入"暂停"时：
- 更新 `workflow-status.json` 的 `lastUpdate` 时间戳
- 记录当前阶段和进度
- 不修改 `currentPhase`

**恢复**：用户输入"继续"时：
- 读取 `currentPhase`，从当前阶段恢复
- 展示中断期间的时间间隔
- 提示是否有文件在暂停期间被外部修改

### 5.4 阶段回退后恢复

如果 `phaseHistory` 中包含回退记录（`rollbackHistory`）：

```
⚠️ 检测到阶段回退记录：
  从「{from}」回退到「{to}」
  原因：{reason}
  时间：{time}

当前阶段：{currentPhase}

将从中断点继续，已回退阶段的产物可能已被清除。
```

---

## 六、恢复安全检查

恢复前自动执行以下检查：

| 检查项 | 说明 | 异常处理 |
|--------|------|---------|
| 状态文件完整性 | JSON 格式 + 必填字段 | 运行 `check_workflow_status.py` 诊断 |
| 产物文件存在性 | 当前阶段依赖的前序产物 | 缺失则回退到上一阶段 |
| 工作目录有效性 | workspace 路径存在 | 提示用户确认或修改 |
| 降级计数合理性 | noProgressCount ≤ 3 | 超过则重置为 0 |
| 模块进度一致性 | completedModules ≤ totalModules | 不一致则重新计数 |

```bash
# 恢复前完整检查
python scripts/check_workflow_status.py
python scripts/validate_phase_output.py --phase $(python scripts/check_workflow_status.py --json | jq -r '.currentPhaseNumber')
```

---

## 七、手动恢复操作

### 重置为指定阶段

当自动恢复无法处理时，可手动修改状态文件：

```json
{
  "currentPhase": "architecting",
  "phaseHistory": [
    {"phase": "config-init", "status": "completed", "time": "..."},
    {"phase": "demand-confirm", "status": "completed", "time": "..."}
  ],
  "developmentProgress": {
    "totalModules": 0,
    "completedModules": 0,
    "currentModule": "",
    "backend": { "modules": [] },
    "frontend": { "modules": [] }
  }
}
```

### 强制重置

```bash
# 完全重置（保留配置文件）
python -c "
import json
with open('doc/workflow-status.json', 'r') as f:
    data = json.load(f)
data['currentPhase'] = 'config-init'
data['phaseHistory'] = []
data['reviewFix'] = {'iteration': 0, 'noProgressCount': 0, 'lastFixSummary': {}}
data['bugFixRemediation'] = {'noProgressCount': 0, 'lastFixSummary': {}}
data['developmentProgress'] = {'totalModules': 0, 'completedModules': 0, 'currentModule': '', 'backend': {'modules': []}, 'frontend': {'modules': []}}
with open('doc/workflow-status.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
print('状态已重置为 config-init')
"
```

---

## 八、恢复失败处理

如果所有恢复尝试失败：

1. 备份当前状态文件和产物
   ```bash
   mkdir -p doc/backup/$(date +%Y%m%d_%H%M%S)
   cp doc/workflow-status.json doc/backup/$(date +%Y%m%d_%H%M%S)/
   cp -r doc/*.md doc/backup/$(date +%Y%m%d_%H%M%S)/ 2>/dev/null
   ```

2. 运行诊断报告了解最后状态
   ```bash
   python scripts/generate_workflow_report.py -o doc/recovery-diagnostic.md
   ```

3. 联系用户提供以下信息：
   - 诊断报告 (`doc/recovery-diagnostic.md`)
   - 备份路径
   - 期望恢复到的阶段

---

## 九、最佳实践

- **状态文件即真相**：`workflow-status.json` 是恢复的唯一权威来源
- **产物优先于历史**：阶段产物文件比对话历史更可靠
- **降级计数保留**：修复循环的 `noProgressCount` 在中断恢复后必须保留
- **模块进度保留**：`developmentProgress` 中的模块状态在中断恢复后必须保留
- **每次状态变化立即写入**：不依赖内存缓存，确保中断时状态不丢失
