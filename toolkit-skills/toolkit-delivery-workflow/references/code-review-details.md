# 代码审查详情（阶段 6）

## 6.1 并行检测

1. 检查 `{directories.backend}` 是否非空（存在 `src/main/java/**` 代码）
2. 检查 `{directories.frontend}` 是否非空（存在 `src/views/**` 或 `src/components/**` 代码，排除 node_modules）
3. **两者都非空** → 并行审查（6.2）
4. **仅一端非空** → 单 Agent 审查（6.3，现有逻辑不变）

## 6.2 并行审查（全栈项目）

```
阶段4+5 产出完成
      ↓
检测代码目录 → 后端代码 + 前端代码 都存在
      ↓
┌──────────────────────────────────────────────────────┐
│  准备两份独立的审查简报                                 │
│                                                      │
│  Agent A: toolkit-code-reviewer (backend)                    │
│  model: {reviewModelPreference.backend} (默认 opus)   │
│  审查范围: {directories.backend} (src/main/java/)     │
│  输出文件: doc/.review-backend.md                    │
│  重点: 安全漏洞、SQL注入、事务一致性、权限绕过          │
│                                                      │
│  Agent B: toolkit-code-reviewer (frontend)                   │
│  model: {reviewModelPreference.frontend} (默认 sonnet)│
│  审查范围: {directories.frontend}                    │
│            (src/views/ + src/components/)            │
│  输出文件: doc/.review-frontend.md                   │
│  重点: XSS漏洞、渲染性能、状态管理、内存泄漏           │
└──────────────────────────────────────────────────────┘
      ↓ 同时启动两个 Agent(an available asynchronous execution mechanism)
      ↓ 等待两个都完成
结果汇总:
  1. Read doc/.review-backend.md
  2. Read doc/.review-frontend.md
  3. 合并 Critical/Warning/Info 计数
  4. 生成统一的 doc/code-review-report.md:
     - 总览: Critical/Warning/Info 合计
     - 第一部分: 后端审查结果
     - 第二部分: 前端审查结果
  5. 更新 workflow-status.json 中的 reviewFindings
      ↓
  如有 Critical → 进入修复循环（6.4）
  无 Critical → 进入阶段 7
```

**模型分配策略**：

| 审查端 | 推荐模型 | 原因 |
|--------|---------|------|
| backend | `opus` | 后端安全漏洞、SQL注入、事务问题需要深度推理 |
| frontend | `sonnet` | 前端 XSS/性能问题审查相对标准 |
| 单端审查 | 继承主 agent | 保持向后兼容 |

模型偏好可通过 `reviewModelPreference` 配置：

```json
"reviewModelPreference": {
  "backend": "opus",
  "frontend": "sonnet"
}
```

**子 Agent 简报要点**：

Agent A (backend review) 简报结构：
- 审查范围：{directories.backend} (src/main/java/)
- 审查规则：安全漏洞(SQL注入/XSS/权限绕过)、性能(N+1查询/未使用索引)、事务一致性、代码规范
- 输出文件：doc/.review-backend.md
- 注意：跳过 .env/*.pem/*.key/node_modules/.git/

Agent B (frontend review) 简报结构：
- 审查范围：{directories.frontend} 中的 views/ 和 components/ (排除 node_modules/)
- 审查规则：XSS漏洞、渲染性能、状态管理、内存泄漏、无障碍访问
- 输出文件：doc/.review-frontend.md
- 注意：跳过 node_modules/.git/

## 6.3 单端审查（纯后端或纯前端项目）

保留现有逻辑不变：
1. 调用 toolkit-code-reviewer，传递配置上下文
2. toolkit-code-reviewer 输出：{docs}/code-review-report.md
3. 进入修复循环或进入阶段 7

## 6.4 修复循环

**无论并行审查还是单端审查，修复循环逻辑统一**：

1. **如有 Critical 问题**：
   - 阻塞测试，输出阻塞原因
   - **修复主体**：分析 Critical 问题所属
     - 后端问题 → 调用 toolkit-backend-architect 修复
     - 前端问题 → 调用 toolkit-frontend-engineer 修复
   - 修复完成后**自动返回阶段 6 重新审查**（并行审查模式下重新并行审查）
   - 对比本轮与上轮审查结果（reviewFindings）：
     - **Critical 有减少** → 重置 `reviewFix.noProgressCount = 0`，继续修复
     - **Critical 无减少** → `reviewFix.noProgressCount++`，触发降级
2. **如无 Critical 问题**：通过审查，进入阶段 7

## Code Review 降级策略

子 Agent 执行失败时，按以下优先级处理：

**第 0 层：模型降级（v2.1.143 平台自动）**：
- 当前模型过载 → 平台自动降级到 fallback-model
- 降级后重试一次，成功则继续；失败则进入任务降级

**第 1-3 层：任务降级**：

| 无进步轮数 | 策略 | 动作 |
|-----------|------|------|
| `noProgressCount = 1` | **自动 defer** | 将 Medium 级别问题标记为 `deferred`，仅保留 Critical 继续修复；输出降级报告 |
| `noProgressCount = 2` | **根因自检 + 简化方案** | 对当前 Critical 问题重新执行根因调查（之前的修复可能治标不治本），确认根因正确后再尝试简化修复方案或 workaround；输出根因自检报告 + 简化建议 |
| `noProgressCount = 3` | **根因状态报告 + 用户干预** | 暂停修复循环，输出完整状态报告（含每个剩余 Critical 问题的根因分析状态：已确认/待确认/疑似误判）；用户选择：继续 / 跳过剩余 / 放弃并继续到阶段 7 |

**降级报告格式**：
```
⚠️ 代码审查降级（第 N 轮无进步）

上轮尝试修复：{attemptedIssues}
结果：问题数未减少

降级动作：
  ├── deferred: M 个 Medium 级别问题已推迟
  └── 保留修复: K 个 Critical 问题继续

下一轮仍无进步将触发：{下一级策略}
```

## Code Review 阻塞规则

Code Review 阶段发现的 Critical 问题会阻塞测试阶段，必须修复后才能继续：
- **Critical 问题**：必须修复，否则无法进入测试阶段
- **Warning 问题**：建议修复，不阻塞测试
- **Info 问题**：供参考，不阻塞测试
