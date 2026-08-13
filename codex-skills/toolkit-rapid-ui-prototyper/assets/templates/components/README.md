# Components Overview

基础组件模板。可复用的 UI 组件片段，可直接嵌入到布局中使用。

> **约定**：每种组件提供主题变量版（使用 CSS 变量）和硬编码版两种形态。多视图/明暗切换页面必须使用主题变量版。

---

## 组件文件一览

| 文件 | 主题变量版 | 硬编码版 | 特殊要求 |
|------|-----------|---------|---------|
| `button.md` | 是 | 是 | 主按钮使用品牌色渐变 |
| `input.md` | 是 | 是 | focus 环、验证状态（error/success） |
| `card.md` | 是 | 是 | 悬停上浮效果可配置 |
| `badge.md` | 是 | 是 | 状态色（success/warning/danger/info） |
| `table.md` | 是（强制） | 否 | 斑马纹行可选 |
| `modal.md` | 是（强制） | 否 | 必须使用 `.modal-content` 主题类 |
| `pagination.md` | 是（强制） | 否 | 活跃页使用品牌色 |

---

## 组件使用原则

1. **多视图/明暗切换必须使用主题变量版** — 颜色走 CSS 变量
2. **单主题/原型快速验证可使用硬编码版** — 直接使用 Tailwind 工具类
3. **弹窗必须使用 `.modal-content` 类** — 禁止内联 style 写死背景
4. **分页必须使用 `.page-btn` 类** — 确保亮暗模式颜色正确

---

## 引入方式

主题变量版需要配合对应的 CSS 类定义：

```html
<style>
  /* 从对应组件模板复制 CSS 类定义 */
  .btn-primary { background: linear-gradient(135deg, var(--brand-primary) 0%, var(--brand-primary-hover) 100%); color: white; }
</style>
```
