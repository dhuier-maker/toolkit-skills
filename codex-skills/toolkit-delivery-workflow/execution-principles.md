# 统一执行原则

本文档定义了所有 SKILL 必须遵守的统一行为规则。toolkit-delivery-workflow 作为协调者负责执行这些规则，各子 SKILL 在实现层面遵循。

---

## 一、核心原则

1. **项目目录必须用户指定**，严禁自动生成 workspace 路径
2. **需求分析阶段必须等待用户确认**后才能继续（`demand-confirm`）
3. **架构设计、后端开发、前端开发、代码审查、测试阶段自动推进**，无需等待确认
4. **UI 原型阶段为可选交互阶段**（`prototyping`），需用户确认后进入正式开发
5. **修复循环无硬性轮次限制**，持续修复直到无问题或触发降级
6. **无进步检测**：连续修复无进展时触发 3 级渐进降级策略
7. **安全兜底**：单个修复循环最多 50 轮，防止极端情况
8. **每次状态变化必须立即更新** `doc/workflow-status.json`
9. **会话中断后自动检测恢复点**，支持从断点继续（保持所有计数器和进度）
10. **严格遵守安全边界**：禁止访问敏感文件，禁止跨 workspace 访问
11. **代码风格一致性**：自动检测并遵循项目已有代码风格
12. **并行任务隔离**：阶段 4+5（后端/前端伪并行）；阶段 3（UI+资源）和阶段 6（后端审查+前端审查）通过 Agent Team 子 Agent 实现真并行

---

## 二、子 SKILL 调用协议

### 2.1 触发机制

```
用户输入
    ↓
SKILL.md description 正则匹配
    ↓
加载对应 SKILL.md
    ↓
执行 SKILL 逻辑
```

### 2.2 toolkit-delivery-workflow 调用子 SKILL 规范

| 调用场景 | 调用方式 | 上下文传递 |
|---------|---------|-----------|
| 阶段 1 需求分析 | 触发 `toolkit-requirements-analyst` | 传递项目名称、workspace 路径 |
| 阶段 2 架构设计 | 触发 `toolkit-backend-architect` | 传递 PRD.md 路径、项目配置 |
| 阶段 3 UI 原型 | 触发 `toolkit-rapid-ui-prototyper` 或 `toolkit-bi-dashboard` | 传递需求类型标记、PRD 摘要 |
| 阶段 3 图片资源（可并行） | 触发 `toolkit-visual-asset-generator`（Agent Team 子 Agent） | 传递图片/图表需求、项目类型 |
| 阶段 4 后端开发 | 触发 `toolkit-backend-architect` | 传递 API.md、模块规划列表 |
| 阶段 5 前端开发 | 触发 `toolkit-frontend-engineer` | 传递 API.md、原型文件路径 |
| 阶段 6 后端审查（全栈并行） | 触发 `toolkit-code-reviewer`（Agent Team 子 Agent, model=opus） | 传递后端代码目录、输出路径 doc/.review-backend.md |
| 阶段 6 前端审查（全栈并行） | 触发 `toolkit-code-reviewer`（Agent Team 子 Agent, model=sonnet） | 传递前端代码目录、输出路径 doc/.review-frontend.md |
| 阶段 6 单端审查 | 触发 `toolkit-code-reviewer` | 传递代码目录路径 |
| 阶段 7 测试验证 | 触发 `toolkit-qa-tester` | 传递 PRD.md、API.md、部署地址 |
| BUG 修复 | 触发 `toolkit-backend-architect` 或 `toolkit-frontend-engineer` | 传递 BUG 报告、相关代码路径 |

### 2.3 调用约束

- 调用前必须确认当前阶段产物已就绪
- 调用后必须等待子 SKILL 完成并验证产物
- 子 SKILL 失败时按错误处理标准执行重试
- 子 SKILL 的输出文件路径必须符合产物规范（见第六节）

---

## 三、错误处理标准

### 3.1 重试策略

所有 SKILL 调用失败时，采用指数退避自动重试：

| 重试次数 | 延迟 | 说明 |
|---------|------|------|
| 第 1 次 | 5 秒 | 可能是瞬时错误 |
| 第 2 次 | 15 秒 | 可能是网络波动 |
| 第 3 次 | 45 秒 | 可能是服务暂时不可用 |

3 次重试后仍失败 → 记录错误到状态文件，暂停工作流，告知用户。

### 3.2 错误分类处理

| 错误类型 | 处理方式 | 是否阻塞 |
|---------|---------|---------|
| 网络超时 | 自动重试 3 次 | 是 |
| API Key 未配置 | 提示用户设置环境变量 | 是 |
| 安全边界违规 | 拒绝访问并提示原因 | 是 |
| 文件不存在 | 检查路径，尝试创建或回退 | 视情况 |
| 状态文件损坏 | 尝试修复或从备份恢复 | 是 |
| 子 SKILL 逻辑错误 | 记录错误，跳过或回退 | 视情况 |

### 3.3 回退机制

当某阶段无法继续时：

```
阶段执行失败
    │
    ├── 可重试 → 自动重试（最多 3 次）
    │
    ├── 可跳过（可选阶段）→ 记录跳过，进入下一阶段
    │
    └── 不可跳过 → 回退到上一阶段
                  │
                  └── 记录回退到 rollbackHistory
                      清除当前阶段的不完整产物
                      提示用户重新确认上一阶段
```

---

## 四、上下文传递机制

### 4.1 状态文件作为唯一真相源

`doc/workflow-status.json` 是所有 SKILL 间共享状态的唯一可靠来源：

```
┌─────────────────────────────────────────────────────┐
│                 workflow-status.json                 │
│                                                     │
│  currentPhase     ←── toolkit-delivery-workflow 写入       │
│  phaseHistory     ←── toolkit-delivery-workflow 写入       │
│  config           ←── 阶段 0 初始化写入              │
│  developmentProgress ←── 阶段 4/5 开发时更新         │
│  bugsFound/Fixed  ←── 阶段 7 测试时更新              │
│  reviewFindings   ←── 阶段 6 审查时更新              │
│  reviewFix        ←── 阶段 6 修复循环更新            │
│  bugFixRemediation ←── 阶段 7 修复循环更新           │
└─────────────────────────────────────────────────────┘
```

### 4.2 产物文件传递

子 SKILL 间通过文件系统传递大型上下文：

```
toolkit-requirements-analyst ──→ doc/PRD.md ──→ toolkit-backend-architect
                                       │
                                       ├──→ doc/API.md ──→ toolkit-frontend-engineer
                                       ├──→ doc/api/*.md ──→ toolkit-frontend-engineer
                                       └──→ src/main/java/* ──→ toolkit-code-reviewer
                                                                   │
                                              doc/code-review-report.md
                                                                   │
                                                                   ▼
                                                              toolkit-qa-tester
                                                                   │
                                                          doc/QA_Report.md
```

### 4.3 配置共享

项目配置文件 `doc/project.config.json` 在所有 SKILL 间共享：

```json
{
  "projectName": "...",
  "directories": { "backend": "...", "frontend": "..." },
  "security": { "blockedExtensions": [...], "sensitivePatterns": [...] },
  "codeStyle": { "autoDetect": true, "configFiles": [...] }
}
```

---

## 五、安全边界执行规范

### 5.1 文件访问规则

所有 SKILL 必须遵守统一的安全边界：

| 规则 | 适用范围 | 违反处理 |
|------|---------|---------|
| 操作范围限制 | 仅限 `{workspace}` 目录内 | 拒绝并记录 |
| 敏感文件跳过 | `.env`、`*.pem`、`*.key` | 自动跳过，记录 Info |
| 依赖目录跳过 | `node_modules/`、`.git/` | 自动跳过 |
| 系统目录禁止 | `/etc/`、`/root/`、`/usr/` | 拒绝并告警 |
| 跨项目隔离 | 禁止访问其他 workspace | 拒绝并记录 |

### 5.2 危险操作确认

以下操作需要用户明确确认：

| 操作 | 确认提示模板 |
|------|------------|
| 删除文件 | "即将删除 `{path}`，确认？" |
| 修改配置文件 | "即将修改 `{path}`，此文件包含项目配置，确认？" |
| 执行 shell 命令 | "即将执行：`{command}`，确认？" |
| 覆盖已有产物 | "`{path}` 已存在，是否覆盖？" |

### 5.3 安全违规处理流程

```
检测到安全边界违规
    │
    ▼
立即拒绝操作
    │
    ▼
输出违规信息：
  - 违规路径
  - 违反的规则
  - 建议的替代方案
    │
    ▼
记录到状态文件（如果是工作流上下文）
    │
    ▼
不阻塞工作流（Info 级别）
```

---

## 六、产物输出规范

### 6.1 文件路径规范

| 产物类型 | 路径模式 | 负责 SKILL |
|---------|---------|-----------|
| PRD 文档 | `doc/PRD.md` | toolkit-requirements-analyst |
| API 总览 | `doc/API.md` | toolkit-backend-architect |
| API 详细规范 | `doc/api/*.md` | toolkit-backend-architect |
| UI 原型 | `prototypes/*.html` | toolkit-rapid-ui-prototyper |
| BI 大屏项目 | `toolkit-bi-dashboard/` | toolkit-bi-dashboard |
| 后端代码 | `src/main/java/**/*.java` | toolkit-backend-architect |
| 前端代码 | `src/**/*.{vue,tsx,ts,js}` | toolkit-frontend-engineer |
| 代码审查报告 | `doc/code-review-report.md` | toolkit-code-reviewer |
| 测试报告 | `doc/QA_Report.md` | toolkit-qa-tester |
| 诊断报告 | `doc/diagnostic-report.md` | generate_workflow_report.py |

### 6.2 命名规范

- 文件名使用英文小写 + 连字符（kebab-case）
- 目录名使用英文小写 + 连字符
- 代码文件遵循对应语言的标准命名规范（Java: PascalCase, TypeScript: camelCase）
- 文档文件使用英文或中文，反映内容主题

### 6.3 产物完整性要求

| 产物 | 最小要求 |
|------|---------|
| PRD.md | ≥ 100 字节，包含功能描述和验收标准 |
| API.md | ≥ 100 字节，包含接口列表 |
| api/*.md | 至少 1 个接口规范文件 |
| 后端代码 | 至少 1 个 .java 文件 |
| 前端代码 | 至少 1 个 .vue/.tsx/.jsx 文件 |
| code-review-report.md | ≥ 50 字节 |
| QA_Report.md | ≥ 50 字节 |

验证命令：
```bash
python scripts/validate_phase_output.py
```

---

## 七、降级与退出规则

### 7.1 修复循环降级

| noProgressCount | 策略 | 触发条件 |
|-----------------|------|---------|
| 0 | 正常运行 | 每轮持续减少问题 |
| 1 | 自动 defer | 连续 1 轮无进步：Low/Medium 问题自动标记为 deferred |
| 2 | 简化方案 | 连续 2 轮无进步：对无法修复的问题尝试简化方案 |
| 3 | 用户干预 | 连续 3 轮无进步：暂停循环，请求用户决策 |

### 7.2 循环退出条件

| 条件 | 行为 |
|------|------|
| 剩余问题 = 0 | 正常进入下一阶段 |
| 用户输入「跳过」 | 标记剩余问题为"遗留"，进入下一阶段 |
| 用户输入「放弃」 | 记录遗留问题，进入交付阶段 |
| iteration ≥ 50 | 强制退出，标记剩余为"遗留" |

### 7.3 阶段退出条件

| 阶段 | 退出条件 |
|------|---------|
| demand-confirm | 用户确认 PRD |
| architecting | API.md 生成完成 |
| prototyping | 用户确认原型或选择跳过 |
| backend-dev | 所有后端模块标记为 done |
| frontend-dev | 所有前端模块标记为 done |
| code-review | Critical = 0 |
| testing | 测试用例全部执行 |
| bugfix | 剩余 BUG = 0 或用户跳过 |

---

## 八、阶段推进规则

### 8.1 确认等待模板

当工作流暂停等待用户确认时，使用以下模板：

```
⏸️ 阶段 {N}（{阶段名称}）已完成。

产物：
  - {产物1}
  - {产物2}

输入「确认」继续，或「修改 XXX」指出需要修改的内容。
```

### 8.2 自动推进声明

当工作流自动推进时，简要输出：

```
⚡ 阶段 {N}（{阶段名称}）自动推进中...
   调用: {skill-name}
   输出: {产物列表}
```

### 8.3 中断恢复声明

当检测到中断时（详见 `recovery.md`）：

```
🔄 检测到项目在阶段「{phase}」中断。
   上次更新: {lastUpdate}
   输入「继续」从断点恢复。
```

---

## 九、并行执行规范

toolkit-delivery-workflow 支持三层并行：

### 9.1 Agent Team 真并行（阶段 3 和阶段 6）

使用 Codex 子 Agent（multi-agent tools when explicitly requested or permitted + an available asynchronous execution mechanism）实现真正的并行执行，子 Agent 拥有独立上下文。

**阶段 3 并行条件**：
- UI 任务（toolkit-bi-dashboard 或 toolkit-rapid-ui-prototyper）+ 资源任务（toolkit-visual-asset-generator）同时存在
- 输出目录隔离（src/ vs doc/images/）
- 两个 Agent 同时启动，完成后汇总整合

**阶段 6 并行条件**：
- 后端代码（src/main/java/）和前端代码（src/views/ 或 src/components/）都非空
- 输出文件隔离（doc/.review-backend.md vs doc/.review-frontend.md）
- 可选模型差异化（backend: opus, frontend: sonnet）
- 两个 Agent 同时启动，完成后汇总合并为 doc/code-review-report.md

**Agent Team 任务管理**：

```json
"parallelTasks": {
  "stage3_ui": { "agentId": "xxx", "status": "in_progress", "startTime": "..." },
  "stage3_image": { "agentId": "yyy", "status": "completed", "endTime": "..." },
  "stage6_backend_review": { "agentId": "aaa", "model": "opus", "status": "in_progress" },
  "stage6_frontend_review": { "agentId": "bbb", "model": "sonnet", "status": "in_progress" }
}
```

- 子 Agent 需要完整自包含的上下文简报（看不到主会话历史）
- 输出目录必须不重叠
- model 仅支持 sonnet/opus/haiku
- 等待所有 Agent 完成后汇总，再进入下一阶段

### 9.2 伪并行（阶段 4+5）

阶段 4（后端开发）和阶段 5（前端开发）伪并行条件：

- API 定义（doc/API.md）已完整生成
- 后端和前端模块无强依赖关系
- 前端已确认 UI 原型（如适用）

### 9.3 并行任务管理（通用）

```json
"parallelTasks": {
  "backend": { "status": "in_progress", "startedAt": "..." },
  "frontend": { "status": "pending" }
}
```

- 任一任务失败不影响另一方
- 双方完成后统一进入阶段 6（代码审查）
- 并行任务状态实时反映在 `parallelTasks` 字段

---

## 十、版本兼容

| 原则 | 说明 |
|------|------|
| 状态文件向后兼容 | 新增字段不影响旧版本读取 |
| 脚本独立可运行 | 每个脚本可独立执行，不依赖 Codex 运行时 |
| SKILL.md 自描述 | 每个 SKILL 完整描述自身行为，减少跨文档依赖 |
