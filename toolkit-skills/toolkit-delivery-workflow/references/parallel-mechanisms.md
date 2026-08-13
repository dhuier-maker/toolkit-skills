# 并行开发机制

toolkit-delivery-workflow 在三个位置支持并行执行，其中阶段 3 和阶段 6 通过子 Agent 实现真正的并行，阶段 4+5 为伪并行（前后端有 API 契约依赖）。

## 并行执行总览

| 阶段 | 并行任务 | 机制 | 依赖关系 |
|------|---------|------|---------|
| 阶段 3 | UI 原型 + toolkit-visual-asset-generator 资源生成 | 2 个子 Agent 同时启动 | 零依赖，真并行 |
| 阶段 4+5 | 后端开发 + 前端开发 | 同进程顺序（伪并行） | 前端依赖后端 API 契约 |
| 阶段 6 | 后端审查 + 前端审查 | 2 个子 Agent 同时启动 | 零依赖，真并行 |

---

## 阶段 3: UI + 资源并行

**触发条件**：同时需要 UI 原型 + 图片/图表资源

**并行启动条件**：
- 阶段 2 架构设计完成
- UI 任务和资源任务互不依赖
- 输出目录隔离（src/ vs doc/images/）

**并行状态追踪**：

```json
{
  "parallelTasks": {
    "stage3_ui": {
      "agentId": "agent-xxx",
      "status": "in_progress",
      "startTime": "2026-05-07T10:00:00"
    },
    "stage3_image": {
      "agentId": "agent-yyy",
      "status": "in_progress",
      "startTime": "2026-05-07T10:00:00"
    }
  }
}
```

**汇合与整合**：

```
两个 Agent 都完成
      ↓
整合结果:
  1. toolkit-visual-asset-generator 背景图 → 复制到 UI 项目 assets/
  2. 图表 HTML → 复制到 prototypes/
  3. 更新 prototypeOutput 状态
      ↓
进入阶段 3.5 原型审查
```

---

## 阶段 4+5: 后端 + 前端（伪并行）

阶段4（后端开发）和阶段5（前端开发）伪并行执行：

**启动条件**：
- API 定义完成后（阶段2完成）
- 前端可先用 Mock 数据开发
- 后端完成后，前端切换真实 API

**并行状态追踪**：

```json
{
  "parallelTasks": {
    "backend": {
      "status": "in_progress",
      "progress": 60,
      "startTime": "2026-04-21T10:00:00",
      "estimatedEndTime": "2026-04-21T14:00:00"
    },
    "frontend": {
      "status": "in_progress",
      "progress": 40,
      "startTime": "2026-04-21T10:00:00",
      "estimatedEndTime": "2026-04-21T15:00:00"
    }
  }
}
```

**并行进度报告**：

```
═══════════════════════════════════════════════════════════
📊 并行开发进度
═══════════════════════════════════════════════════════════

🔧 后端开发 (toolkit-backend-architect)
├── 状态：进行中
├── 进度：60% ████████████░░░░░░░░
├── 已完成：用户模块、村庄模块
└── 进行中：通知模块

🎨 前端开发 (toolkit-frontend-engineer)
├── 状态：进行中
├── 进度：40% ████████░░░░░░░░░░░░
├── 已完成：登录页面、布局框架
└── 进行中：村庄列表页

⏱️ 预计完成时间：
├── 后端：约 2 小时
└── 前端：约 3 小时
```

**汇合条件**：
- 后端和前端都完成
- 任一失败则暂停等待处理
- 先完成的等待后完成的

---

## 阶段 6: 后端审查 + 前端审查（并行）

**触发条件**：全栈项目（后端代码 + 前端代码都存在）

**并行启动条件**：
- 阶段 4+5 都已完成
- 后端和前端审查互不依赖
- 输出文件隔离（doc/.review-backend.md / doc/.review-frontend.md）

**模型差异化**：后端审查推荐 `opus`（深度推理），前端审查推荐 `sonnet`（快速高效）

**并行状态追踪**：

```json
{
  "parallelTasks": {
    "stage6_backend_review": {
      "agentId": "agent-aaa",
      "model": "opus",
      "status": "in_progress",
      "startTime": "2026-05-07T14:00:00"
    },
    "stage6_frontend_review": {
      "agentId": "agent-bbb",
      "model": "sonnet",
      "status": "in_progress",
      "startTime": "2026-05-07T14:00:00"
    }
  }
}
```

**汇总流程**：

```
两个审查 Agent 都完成
      ↓
1. Read doc/.review-backend.md → 提取后端 Critical/Warning/Info
2. Read doc/.review-frontend.md → 提取前端 Critical/Warning/Info
3. 合并为统一的 doc/code-review-report.md
4. 更新 reviewFindings
      ↓
如有 Critical → 按所属端分配修复 Agent → 重新审查
无 Critical → 进入阶段 7
```
