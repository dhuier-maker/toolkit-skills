# BUG 修复循环（阶段 7.5）

**铁律：先调查根因，再实施修复。禁止未确认根因就直接修改代码。**

BUG 修复执行主体：
- **后端 BUG** → toolkit-backend-architect（传递 BUG 列表 + 根因分析结果）
- **前端 BUG** → toolkit-frontend-engineer（传递 BUG 列表 + 根因分析结果）

## 根因调查流程（每个 BUG 修复前必执行）

```
发现 BUG
    ↓
1. 复现确认：验证 BUG 是否可稳定复现
    ↓
2. 根因定位：
   - 前端 BUG：检查控制台错误 → Network 请求/响应 → 组件状态/props → 渲染逻辑
   - 后端 BUG：检查日志/异常栈 → 入参/出参 → 数据库查询 → 业务逻辑
    ↓
3. 根因确认：用一句话描述根因（"因为 X，导致 Y"）
    ↓
4. 修复实施：针对根因修改代码
    ↓
5. 验证修复：复测确认 BUG 已解决且无回归
```

**根因报告格式**（每个 BUG 修复后输出）：
```
BUG #{id}: {标题}
├── 根因: {一句话根因描述}
├── 定位过程: {简述调查步骤}
├── 修复方案: {针对根因的修改}
└── 验证结果: {复测确认}
```

**禁止行为**：
- ❌ 看到报错直接改代码，不分析根因
- ❌ 凭直觉猜测根因，不验证
- ❌ 修复后不复测确认

BUG 修复采用**无限循环 + 退出条件**机制：

## an explicit completion objective 驱动 BUG 批量修复

当 BUG 数量 > 3 个且互相独立（无因果依赖）时，可用 `an explicit completion objective` 模式加速修复：

```
an explicit completion objective 修复所有BUG，直到QA测试通过
```

| 特性 | 串行修复（默认） | an explicit completion objective 模式 |
|------|----------------|-----------|
| 修复顺序 | 按发现顺序逐个 | Codex 自主判断优先级和顺序 |
| 并行潜力 | 每次修一批，测一批 | 可自主跳过已修复的，聚焦剩余 |
| 适用 | BUG 少或互相依赖 | BUG 多且互相独立 |
| 退出 | 同样的退出条件 | 同样的退出条件 |

> **注意**：`an explicit completion objective` 模式仍遵循根因调查铁律，不会跳过根因分析步骤。

## 退出条件（满足任一即可进入交付）

| 条件 | 说明 | 动作 |
|------|------|------|
| 无 BUG | 所有 BUG 已修复 | 直接进入阶段 8 (交付) |
| 软通过 | Critical=0 且 Warning≤3 | 提示用户，确认后可交付 |
| 降级后软通过 | Critical=0 且 Warning>3 但已到用户干预阶段 | 提示用户，确认后可交付 |
| 用户中断 | 用户输入"跳过"、"强制交付" | 直接进入阶段 8 (交付) |

## BUG 修复降级策略

子 Agent 执行失败时，按以下优先级处理：

**第 0 层：模型降级（v2.1.143 平台自动）**：
- 当前模型过载 → 平台自动降级到 fallback-model（如 opus → sonnet）
- 降级后重试一次，成功则继续；失败则进入任务降级

**第 1-3 层：任务降级**：

| 无进步轮数 | 策略 | 动作 |
|-----------|------|------|
| `noProgressCount = 1` | **自动 defer** | 将 Low/Medium 级别的 BUG 标记为 `deferred`，仅保留 High/Critical 继续修复；输出降级报告 |
| `noProgressCount = 2` | **根因自检 + 简化方案** | 对当前剩余 BUG 重新执行根因调查（之前的修复可能治标不治本），确认根因正确后再尝试简化修复方案或 workaround；输出根因自检报告 + 简化建议 |
| `noProgressCount = 3` | **根因状态报告 + 用户干预** | 暂停修复循环，输出完整状态报告（含每个剩余 BUG 的根因分析状态：已确认/待确认/疑似误判）；用户选择：继续 / 跳过剩余 / 放弃 |

**降级报告格式**：
```
⚠️ BUG 修复降级（第 N 轮无进步）

上轮尝试修复：{attemptedBugs}
结果：BUG 数量未减少

降级动作：
  ├── deferred: M 个 Low/Medium BUG 已推迟
  ├── simplified: K 个 BUG 已应用简化方案
  └── 保留修复: J 个 High/Critical BUG 继续

下一轮仍无进步将触发：{下一级策略}
```

## 修复流程

```
测试验证 → 发现 BUG
    ↓
分析 BUG 所属（前端/后端）
    ↓
调用对应 skill 修复：
  - 后端 BUG → toolkit-backend-architect
  - 前端 BUG → toolkit-frontend-engineer
    ↓
修复完成后返回阶段 7 重新测试验证
    ↓
对比本轮与上轮 BUG 数量：
  ├── 有减少（progress）→ 重置 noProgressCount=0，继续循环
  └── 无减少（no-progress）→ noProgressCount++ → 触发降级
    ↓
降级检查：
  ├── noProgressCount=1 → 自动 defer：Low/Medium → deferred
  ├── noProgressCount=2 → 简化方案：降低复杂度或替代方案
  └── noProgressCount=3 → 用户干预：继续/跳过/放弃
    ↓
退出检查
  ├── 无 BUG → 进入交付
  ├── Critical=0 且 Warning≤3 → 输出状态报告，等待用户确认
  ├── noProgressCount≥3 → 暂停，等待用户决策
  ├── Critical>0 且 noProgressCount<3 → 继续修复（循环）
  └── 用户输入"跳过"/"强制交付" → 进入交付
```
