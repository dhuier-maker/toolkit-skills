# 状态管理

使用 `{workspace}/{files.workflowStatus}` 追踪项目状态：
```json
{
  "currentPhase": "config-init | demand-confirm | architecting | prototyping | backend-dev | frontend-dev | code-review | testing | bugfix | delivered",
  "phaseHistory": [
    {"phase": "config-init", "status": "completed", "time": "timestamp"},
    {"phase": "demand-confirm", "status": "completed", "time": "timestamp"}
  ],
  "config": {
    "projectName": "my-project",
    "workspace": ".",
    "directories": {...},
    "files": {...}
  },
  "mode": "full",
  "worktreeMode": false,
  "worktreeBranch": null,
  "bgIsolation": null,
  "scope": {
    "newModules": [],
    "existingModules": []
  },
  "projectType": "general",
  "parallelTasks": {
    "backend": {
      "status": "pending | in_progress | completed | failed",
      "progress": 0,
      "startTime": null,
      "endTime": null
    },
    "frontend": {
      "status": "pending | in_progress | completed | failed",
      "progress": 0,
      "startTime": null,
      "endTime": null
    },
    "stage3_ui": {
      "agentId": null,
      "status": "pending | in_progress | completed | failed",
      "startTime": null,
      "endTime": null
    },
    "stage3_image": {
      "agentId": null,
      "status": "pending | in_progress | completed | failed",
      "startTime": null,
      "endTime": null
    },
    "stage6_backend_review": {
      "agentId": null,
      "model": "opus",
      "status": "pending | in_progress | completed | failed",
      "startTime": null,
      "endTime": null
    },
    "stage6_frontend_review": {
      "agentId": null,
      "model": "sonnet",
      "status": "pending | in_progress | completed | failed",
      "startTime": null,
      "endTime": null
    }
  },
  "reviewModelPreference": {
    "backend": "opus",
    "frontend": "sonnet"
  },
  "reviewReports": {
    "backend": "doc/.review-backend.md",
    "frontend": "doc/.review-frontend.md",
    "merged": "doc/code-review-report.md"
  },
  "prototypeOutput": {
    "type": "none | toolkit-rapid-ui-prototyper | toolkit-bi-dashboard",
    "path": null,
    "inheritedByFrontend": false
  },
  "estimation": {
    "totalAPIs": 0,
    "projectScale": "small | medium | large",
    "estimatedTime": {
      "demand": "10 min",
      "architect": "30 min",
      "backend": "2-4 hours",
      "frontend": "3-5 hours",
      "review": "30 min",
      "test": "1-2 hours",
      "total": "7-12 hours"
    }
  },
  "bugsFound": 0,
  "bugsFixed": 0,
  "bugsRemaining": {
    "critical": 0,
    "warning": 0,
    "info": 0
  },
  "reviewFindings": {
    "critical": 0,
    "warning": 0,
    "info": 0
  },
  "reviewBlocked": false,
  "reviewFix": {
    "iteration": 0,
    "noProgressCount": 0,
    "lastFixSummary": {
      "attemptedIssues": [],
      "result": "progress | no-progress",
      "note": ""
    }
  },
  "bugFixRemediation": {
    "noProgressCount": 0,
    "lastFixSummary": {
      "attemptedBugs": [],
      "result": "progress | no-progress",
      "deferredCount": 0,
      "simplifiedCount": 0
    }
  },
  "developmentProgress": {
    "totalModules": 0,
    "completedModules": 0,
    "currentModule": "",
    "backend": {
      "modules": []
    },
    "frontend": {
      "modules": []
    }
  },
  "bugFixHistory": [
    {"round": 1, "found": 5, "fixed": 4, "remaining": 1, "time": "timestamp"}
  ],
  "bugFixRound": 0,
  "lastBugFixTime": "timestamp",
  "userInterrupted": false,
  "rollbackHistory": [
    {
      "from": "testing",
      "to": "architecting",
      "reason": "用户请求：API设计不合理",
      "time": "timestamp",
      "preservedFiles": ["doc/PRD.md"]
    }
  ],
  "retryHistory": [
    {
      "skill": "toolkit-qa-tester",
      "error": "MCP连接失败",
      "retries": 1,
      "maxRetries": 3,
      "time": "timestamp"
    }
  ],
  "startTime": "timestamp"
}
```

### 状态字段说明

| 字段 | 说明 |
|------|------|
| `currentPhase` | 当前阶段（细化后的8个阶段） |
| `mode` | 开发模式：full（全量）/ incremental（增量） |
| `worktreeMode` | 是否启用 Worktree 完整隔离模式（默认 false） |
| `worktreeBranch` | Worktree 分支名（如 `feature/xxx`，仅 worktreeMode=true 时有值） |
| `bgIsolation` | 隔离模式：`null`（默认，无隔离）/ `"worktree"`（完整隔离）/ `"none"`（轻量隔离，后台直接编辑） |
| `scope` | 增量模式下的开发范围 |
| `projectType` | 项目类型：general / toolkit-bi-dashboard |
| `parallelTasks` | 并行任务状态（后端/前端 + 阶段3 UI/资源 + 阶段6 后端审查/前端审查） |
| `reviewModelPreference` | 审查模型偏好配置（backend/frontend 分别指定模型） |
| `reviewReports` | 审查报告路径（backend/frontend 分报告 + 合并后总报告） |
| `prototypeOutput` | 原型输出信息 |
| `estimation` | 进度估算 |
| `reviewFix` | Code Review 修复的降级追踪（noProgressCount、修复摘要） |
| `bugFixRemediation` | BUG 修复的降级追踪（noProgressCount、推迟数、简化数） |
| `developmentProgress` | 模块级开发进度（totalModules、completedModules、各模块状态） |
| `rollbackHistory` | 回退历史记录 |
| `retryHistory` | 重试历史记录 |
