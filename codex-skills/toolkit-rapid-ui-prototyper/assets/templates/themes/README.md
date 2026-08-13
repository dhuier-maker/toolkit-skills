# Theme Variables Overview

主题变量模板说明。本目录下的模板仅包含 CSS 变量定义，不涉及具体组件。用于快速为项目建立主题体系。

> **约定**：所有颜色必须走 CSS 变量，禁止在组件 CSS 类或内联样式中硬编码颜色值。

---

## 变量分组

```
:root {
  /* ===== 品牌色（跨视图共享） ===== */
  --brand-primary: ...;
  --brand-primary-hover: ...;

  /* ===== 管理后台（可切换亮暗） ===== */
  --admin-bg: ...;
  --admin-bg-card: ...;
  --admin-text: ...;
  --admin-border: ...;

  /* ===== 移动端（可切换亮暗） ===== */
  --mobile-bg: ...;
  --mobile-header-bg: ...;
  --mobile-card-bg: ...;

  /* ===== BI 大屏（固定暗色） ===== */
  --bi-bg: ...;
  --bi-card-bg: ...;
  --bi-text: ...;
}
```

---

## 使用方式

### 单个页面（单视图）

```html
<style>
  @import url('brand-colors.md');
  @import url('admin-theme.md');
</style>
```

推荐直接复制所需主题模板的完整 CSS 变量定义到页面的 `<style>` 块中。

### 多视图页面（管理后台 + BI 大屏）

```html
<style>
  :root {
    /* 品牌色（复制 brand-colors.md） */
    /* 管理后台变量（复制 admin-theme.md） */
    /* 移动端变量（复制 mobile-theme.md，可选） */
  }

  body.light-mode {
    /* 亮色模式覆盖（复制 admin-theme.md 的 light-mode 部分） */
  }

  /* BI 大屏视图 — 固定暗色（复制 bi-theme.md） */
  body.light-mode #view-bi {
    /* 重置关键变量，不受亮色模式影响 */
  }
</style>
```

---

## 各主题文件一览

| 文件 | 变量前缀 | 亮色模式 | 适用场景 |
|------|---------|---------|---------|
| `brand-colors.md` | `--brand-*` | 无影响 | 通用主色、辅助色 |
| `admin-theme.md` | `--admin-*` | body.light-mode 覆盖 | 后台管理、Web 应用 |
| `mobile-theme.md` | `--mobile-*` | body.light-mode 覆盖 | 移动端 H5 |
| `bi-theme.md` | `--bi-*` | 不受影响（固定暗色） | BI 大屏、数据可视化 |

---

## 关键规则

1. **品牌色永远不变** — `--brand-*` 不参与亮暗切换
2. **管理后台/移动端跟随亮暗** — 用 `body.light-mode` 覆盖
3. **BI 大屏固定暗色** — 用 `body.light-mode #view-bi { }` 隔离
4. **选择器隔离** — 多视图页面用 `#view-admin`、`#view-bi` 等 id 隔离作用域
