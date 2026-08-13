# 适配后的来源指南

# Karpathy Guidelines

Behavioral guidelines to reduce common LLM coding mistakes, derived from [Andrej Karpathy's observations](https://x.com/karpathy/status/2015883857489522876) on LLM coding pitfalls and [Mnilax's extensions](https://x.com/Mnilax/status/2053116311132155938) on silent failure patterns.

**Tradeoff:** These guidelines bias toward caution over speed. For trivial tasks, use judgment.

---

## When to Apply

| 场景 | 推荐 | 说明 |
|------|------|------|
| 编写新功能代码 | Must | 避免过度设计，保持最小实现 |
| 审查/重构代码 | Must | 精准修改，不碰无关代码 |
| Bug 修复 | Must | 定义复现条件，验证修复 |
| 配置/脚本修改 | Skip | 简单操作无需准则约束 |
| 快速原型验证 | Optional | 原型阶段允许牺牲严谨性 |

## 1. Think Before Coding

**Don't assume. Don't hide confusion. Surface tradeoffs.**

Before implementing:
- State your assumptions explicitly. If uncertain, ask.
- If multiple interpretations exist, present them - don't pick silently.
- If a simpler approach exists, say so. Push back when warranted.
- If something is unclear, stop. Name what's confusing. Ask.

## 2. Simplicity First

**Minimum code that solves the problem. Nothing speculative.**

- No features beyond what was asked.
- No abstractions for single-use code.
- No "flexibility" or "configurability" that wasn't requested.
- No error handling for impossible scenarios.
- If you write 200 lines and it could be 50, rewrite it.

Ask yourself: "Would a senior engineer say this is overcomplicated?" If yes, simplify.

## 3. Surgical Changes

**Touch only what you must. Clean up only your own mess.**

When editing existing code:
- Don't "improve" adjacent code, comments, or formatting.
- Don't refactor things that aren't broken.
- Match existing style, even if you'd do it differently.
- If you notice unrelated dead code, mention it - don't delete it.

When your changes create orphans:
- Remove imports/variables/functions that YOUR changes made unused.
- Don't remove pre-existing dead code unless asked.

The test: Every changed line should trace directly to the user's request.

## 4. Goal-Driven Execution

**Define success criteria. Loop until verified.**

Transform tasks into verifiable goals:
- "Add validation" → "Write tests for invalid inputs, then make them pass"
- "Fix the bug" → "Write a test that reproduces it, then make it pass"
- "Refactor X" → "Ensure tests pass before and after"

For multi-step tasks, state a brief plan:
```
1. [Step] → verify: [check]
2. [Step] → verify: [check]
3. [Step] → verify: [check]
```

Strong success criteria let you loop independently. Weak criteria ("make it work") require constant clarification.

## 5. Fail Explicitly

**If a step was skipped, claiming "done" is itself an error.**

- If you cannot complete a step, say so explicitly — never silently skip and proceed.
- If a test was skipped, reporting "tests passed" is a lie.
- If an error occurred mid-task, report the failure and what remains — don't paper over it.
- When uncertain about correctness, surface the uncertainty. Never hide it behind a confident summary.

The principle: proactively expose uncertainty and failure. Concealing problems is worse than the problems themselves.

---

## Anti-Patterns（反模式）

| 反模式 | 正确做法 | 为什么 |
|--------|----------|--------|
| "顺便"重构相邻代码 | 只改用户要求的 | 相邻代码有隐式依赖，改了可能引入新bug |
| 为未来需求预留抽象 | 只做当前需要的 | YAGNI — 未来需求90%不会来，抽象反而增加理解成本 |
| 添加"防御性"错误处理 | 只在系统边界验证 | 内部代码信任调用者，多余的校验掩盖真正的问题 |
| 复制粘贴相似逻辑再改 | 提取共享函数后再用 | 重复代码看似安全，但后续改一处忘另一处更危险 |
| 200行实现50行能解决的事 | 重写为50行 | 代码行数与bug数正相关，简洁即安全 |
| 跳过无法完成的步骤却宣称"已完成" | 显式报告失败及剩余待办 | 静默跳步比失败本身更危险，掩盖问题延误发现时机 |

---

## Quick Reference（快速参考）

### 修改前自检 3 问

1. **这行代码与用户请求有直接关系吗？** → 否则不改
2. **有更简单的实现方式吗？** → 有则用简单的
3. **怎么验证改对了？** → 定义可执行的验证步骤

### 修改后自检 4 问

1. **每个 changed line 都能追溯到用户请求吗？** → 否则回退
2. **留下了我制造的无用代码（orphan imports/vars）吗？** → 清理
3. **预先存在的死代码被我删了吗？** → 恢复（除非用户要求）
4. **有步骤被跳过或未完成吗？** → 显式报告，不可宣称"已完成"
