# 适配后的来源指南

# toolkit-html-doc-site：Markdown → 纯静态 HTML 文档站点生成器

## 核心定位

将任意目录下的 Markdown 文件集合，转换为**纯静态 HTML 文档站点**。输出零依赖、零服务器、双击即用、可随意移动目录。

> **注意**：输出文件零依赖，但构建过程需要 Node.js 环境运行 `build.js`。

## 输入模式处理

| 输入类型 | 处理策略 |
|----------|----------|
| 多文件目录 | 完整站点模式：侧边栏 + 搜索 + 卡片首页 |
| 单个文件 | 简版模式：无侧边栏，仅保留目录面板和主题切换 |
| 空目录/无 md 文件 | 报错提示，终止执行 |
| 嵌套目录（>1级） | 递归映射：按目录层级生成多级折叠导航，面包屑自动计算层级路径 |

## 输出结构

```
output-dir/
├── index.html              # 汇总首页（卡片网格 + 搜索）
├── css/
│   └── style.css           # 统一样式（亮/暗主题 + 打印样式）
├── js/
│   ├── data.js             # 文档数据索引（搜索用）
│   └── app.js              # 交互逻辑（搜索、导航、主题、目录、复制按钮）
├── pages/                  # 根级文档页面
├── category/               # 子目录文档页面（按源目录层级映射）
└── build.js                # 构建脚本（Markdown → HTML）
```

## 生成流程

### Step 1: 分析源文档结构

1. **确认源目录**：若用户未指定，询问源目录路径
2. **扫描文件**：递归收集所有 `.md` 文件，统计数量
3. **判断模式**：单文件 → 简版模式（跳过 Step 5）；多文件 → 完整站点模式
4. **确认输出配置**：向用户确认输出目录（默认 `./html-site/`）

### Step 2: 生成 CSS 样式文件

生成 `css/style.css`，包含：
- CSS 变量体系（亮/暗双主题）
- 侧边栏样式（固定、可折叠）
- 主内容区样式（`.page-content` 使用 `max-width: 70%; margin: 0 auto;` 居中约束宽度）
- 右侧目录面板（固定定位、可收起、内部可滚动）
- 搜索组件样式
- 卡片网格（首页）
- 文档排版样式（标题、表格、代码块、引用、列表）
- **代码块复制按钮样式**（右上角悬浮按钮，hover 时显示）
- 响应式断点（1200px / 768px）
- **打印样式**（`@media print` 隐藏侧边栏、目录面板、搜索、主题切换）
- 滚动条美化

### Step 3: 生成 JS 数据与交互文件

#### data.js

```javascript
// SKILL_DATA — 多级嵌套结构
const SKILL_DATA = {
  categoryName: {
    name: 'DisplayName',
    icon: '📖',
    children: { /* 子目录 */ },
    items: [{ name, path, desc }]  // 该目录下的文档
  }
};

// ALL_SEARCH_DATA — 扁平化搜索数据
const ALL_SEARCH_DATA = [
  { title, path, desc, type: 'Category > Sub > Leaf', keywords: [] }
];
```

**生成规则**：扫描源目录，按子目录层级递归构建 `SKILL_DATA`；`ALL_SEARCH_DATA` 为所有文档的扁平化数组。

#### app.js

| 模块 | 职责 |
|------|------|
| ThemeManager | 亮/暗主题切换，localStorage 持久化 |
| SidebarManager | 侧边栏展开/收起，移动端点击外部关闭 |
| NavigationManager | 多级折叠导航，递归展开/收起，状态持久化，当前页高亮并自动展开父级、滚动到可视区域 |
| TocManager | 右侧目录面板收起/展开，ScrollSpy 高亮 |
| SearchManager | 前端模糊搜索，键盘导航，路径计算 |
| CopyButtonManager | 代码块复制按钮（每个 `<pre>` 右上角添加复制按钮，点击复制代码内容） |

### Step 4: 生成构建脚本 build.js

核心功能：
1. **动态扫描源目录**：递归扫描所有 `.md` 文件，提取元数据（标题、描述、触发词）
2. **动态生成**导航、搜索数据（`data.js`）、首页（`index.html`）— **禁止硬编码**
3. **Markdown → HTML 转换**（自定义解析器，不依赖外部库）
4. **为标题生成锚点 ID**（中文支持）
5. **提取目录（TOC）** 并生成右侧面板 HTML
6. **为代码块添加复制按钮** HTML
7. **生成 SEO meta 标签**（`<meta name="description">`、`<meta property="og:title">` 等）

### Step 5: 生成汇总首页 index.html

> 仅在多文件模式下执行

- Hero 区域（标题、描述、统计数字）
- 按分类展示文档卡片网格
- 每张卡片：图标、名称、类型标签、描述、关键词标签

### Step 6: 构建所有页面

运行 `node build.js`，生成所有 HTML 文件。

---

## 元数据提取规则

| 字段 | 提取优先级 |
|------|-----------|
| 标题 | ① YAML Frontmatter `title` → ② 第一个 `# ` 一级标题 → ③ 文件名（去 `.md`，`-` 换空格） |
| 描述 | ① YAML Frontmatter `description` → ② 首个非标题段落（截取前 120 字符） → ③ `"{标题} 的详细说明"` |
| 关键词 | ① YAML Frontmatter `keywords`/`tags` → ② 所有 `## ` 二级标题 → ③ 空数组 |

### 图标映射

| 类型/关键词 | 图标 |
|-------------|------|
| API、接口 | 🔌 | Guide、指南、教程 | 📖 | Config、配置 | ⚙️ |
| Skill、技能 | 🛠️ | Test、测试 | 🧪 | Design、设计 | 🎨 |
| Backend、后端 | 🏗️ | Frontend、前端 | 🖥️ | Security、安全 | 🔒 |
| Deploy、部署 | 🚀 | 默认 | 📄 |

---

## Markdown 转 HTML 解析器规则

### YAML Frontmatter

若文件**以 `---` 开头**（第一行就是 `---`），解析两个 `---` 之间为 YAML 元数据，不渲染到页面。文件中间的 `---` 视为水平线。

### 行级元素

| 元素 | 规则 |
|------|------|
| 代码块 ` ```lang ` | `<pre><code class="language-lang">` + **内容必须 HTML 转义**，右上角加复制按钮 |
| 表格 `|...|` | 跳过分隔行（`---`、`:---:`），首行 `<thead>`，其余 `<tbody>` |
| 标题 `# ~ ####` | `<h1>` ~ `<h4>` + 生成锚点 ID |
| 引用 `>` | `<blockquote>` |
| 无序/有序列表 | `<ul>/<ol>` + `<li>` |
| 水平线 `---` | `<hr>`（先关闭当前表格再处理） |
| 普通段落 | `<p>` |

### 行内元素

| 元素 | 规则 |
|------|------|
| 行内代码 `` `code` `` | `<code>` + **内容必须 HTML 转义** |
| 粗体 `**text**` | `<strong>` |
| 斜体 `*text*` | `<em>` |
| 链接 `[text](url)` | `<a href="url">` |

### 锚点 ID 生成

```javascript
function generateHeadingId(text) {
  return text.toLowerCase().replace(/[^\w一-龥]+/g, '-').replace(/^-+|-+$/g, '');
}
```

---

## 踩坑清单 — 必须遵守

### 1. HTML 转义（行内代码 & 代码块）

代码中包含 `<style>`、`<div>` 等标签时，直接放入 `<code>`/`<pre>` 会被浏览器解析为真实元素，破坏页面。

```javascript
text = text.replace(/`([^`]+)`/g, (m, code) => '<code>' + escapeHtml(code) + '</code>');
// 代码块：`<pre><code>${escapeHtml(content)}</code></pre>`
```

### 2. 表格分隔行过滤 & 水平线冲突

- 分隔行 `|---|---|` 必须跳过：`if (cells.every(c => /^[-:]+$/.test(c))) continue;`
- 处理水平线 `---` 前先关闭当前表格：`if (inTable && !line.startsWith('|')) { inTable = false; ... }`

### 3. 路径计算（file:// 协议 / 搜索结果 / 深层页面 / Windows）

**四个路径相关 Bug 合并**：
- `file://` 下 `window.location.pathname` 跨平台不一致 → 用 `href` + `split('/').pop()` 取文件名
- 搜索结果 404 → 路径需加深度前缀
- 深层页面 CSS/JS 丢失 → 构建时按深度生成资源引用前缀
- Windows `path.relative()` 返回反斜杠 → `.replace(/\\/g, '/')`

```javascript
function getResourcePrefix(currentPath) {
  return '../'.repeat(currentPath.split('/').length - 1);
}
```

### 4. 布局与响应式

**两个布局 Bug 合并**：
- 目录面板遮挡正文 → 使用 `position: fixed` 脱离文档流
- 固定宽度/内边距导致小屏错乱 → 用 flex 自适应 + `max-width` 约束

```css
.page-content { max-width: 70%; margin: 0 auto; }
.doc-content-wrapper { flex: 1; min-width: 0; }
.doc-toc-panel { position: fixed; right: 16px; top: 76px; width: 280px; height: calc(100vh - 92px); }
.doc-toc-panel .toc-content { flex: 1; overflow-y: auto; }  /* 面板内部可滚动 */
@media (max-width: 1200px) { .doc-toc-panel { display: none; } }
```

### 5. 导航高亮（选择器冲突 / 父级不展开 / 未滚动到可视区域）

**三个导航 Bug 合并**：
- `.nav-item` 匹配到折叠项 → 用 `:not(.nav-item-with-children)` 排除
- 深层页面父级未展开 → 高亮后递归 `expandAncestors()`
- 高亮项不在可视区域 → 高亮后 `scrollToNavItem()` 自动滚动

```javascript
document.querySelectorAll('.nav-item:not(.nav-item-with-children), .nav-child-item')
// 高亮后：expandAncestors(el) → scrollToNavItem(el)
```

### 6. 多级导航 ID 冲突

使用完整路径作为 section ID：`dirPath.replace(/\//g, '-')` → `data-section="guides-tutorials-beginner"`

### 7. 导航/搜索数据/首页禁止硬编码

`build.js` 必须动态扫描源目录并生成导航、`data.js`、`index.html`。新增 MD 文件后重新 `node build.js` 即可自动更新。

### 8. 收起/展开状态持久化

所有可折叠组件（导航、目录面板）状态保存到 `localStorage`，初始化时恢复。

### 9. 连续列表项合并

解析器逐行生成 `<li>` 时，后处理合并：`finalHtml.replace(/(<li>.*?<\/li>\n?)+/g, m => '<ul>\n' + m + '</ul>\n');`

### 10. YAML Frontmatter 误识别

只有文件**以 `---` 开头**时才是 frontmatter。文件中间的 `---` 是水平线。

### 11. 目录面板收起后无法重新展开

**问题**：目录面板收起时使用 `transform: translateX(300px); opacity: 0; pointer-events: none;` 将整个面板移出屏幕并禁用点击，用户无法再点击面板内的按钮来展开。

**修复**：在页面中额外放置一个 `.toc-expand-btn` 按钮，面板收起时显示、展开时隐藏。面板内收起按钮的文字也要同步切换（收起/展开）。

```html
<!-- 目录面板 -->
<div class="doc-toc-panel" id="tocPanel">
  <div class="toc-header"><span>目录</span><button class="toc-toggle">收起</button></div>
  <div class="toc-content">...</div>
</div>
<!-- 独立展开按钮（面板收起时可见） -->
<button class="toc-expand-btn">📖 展开目录</button>
```

```css
.toc-expand-btn { display: none; position: fixed; right: 16px; top: calc(var(--header-height) + 16px); }
.doc-toc-panel.collapsed ~ .toc-expand-btn { display: block; }
```

```javascript
// 收起时：toggleBtn.textContent = '展开'; expandBtn.classList.add('visible');
// 展开时：toggleBtn.textContent = '收起'; expandBtn.classList.remove('visible');
```

---

## 页面模板

### 完整站点模式

```html
<body>
  <div class="app-container">
    <aside class="sidebar" id="sidebar">
      <div class="sidebar-header">Logo</div>
      <div class="sidebar-search">搜索框</div>
      <nav class="sidebar-nav" id="sidebarNav">
        <div class="nav-section">
          <div class="nav-section-title">Category</div>
          <a href="pages/doc.html" class="nav-item">Doc</a>
          <div class="nav-item nav-item-with-children" data-section="cat-sub">
            <span>Sub Category</span><svg class="nav-item-arrow">▸</svg>
          </div>
          <div class="nav-children" id="nav-cat-sub">
            <a href="cat/sub/doc.html" class="nav-child-item">Sub Doc</a>
          </div>
        </div>
      </nav>
    </aside>
    <main class="main-content">
      <header class="page-header">
        <div class="breadcrumb">
          <a href="../index.html">Home</a><span class="breadcrumb-separator">/</span>
          <a href="../pages/cat.html">Category</a><span class="breadcrumb-separator">/</span>
          <span>Current Page</span>
        </div>
        <button class="theme-toggle">主题切换</button>
      </header>
      <div class="page-content">
        <h1 class="doc-title">页面标题</h1>
        <div class="doc-content">
          <div class="page-with-toc">
            <div class="doc-content-wrapper">正文内容（标题带锚点 ID）</div>
            <div class="doc-toc-panel" id="tocPanel">目录面板</div>
          </div>
        </div>
      </div>
    </main>
  </div>
  <script src="../js/data.js"></script>
  <script src="../js/app.js"></script>
</body>
```

### 简版模式（单文件）

与完整模式的差异：无 `.app-container`、无 `.sidebar`，使用 `.single-page-container` 直接包裹，无 `data.js` 引用。

```html
<body>
  <div class="single-page-container">
    <header class="page-header">
      <h1 class="doc-title">文档标题</h1>
      <button class="theme-toggle">主题切换</button>
    </header>
    <div class="page-with-toc">
      <div class="doc-content-wrapper">正文内容</div>
      <div class="doc-toc-panel">目录面板</div>
    </div>
  </div>
  <script src="js/app.js"></script>
</body>
```

### 多级导航 CSS

```css
.nav-children { display: none; padding-left: 12px; }
.nav-children.expanded { display: block; }
.nav-child-item { display: block; padding: 6px 20px 6px 32px; color: var(--text-secondary); font-size: 13px; }
.nav-children-level-2 .nav-child-item { padding-left: 44px; }
.nav-children-level-3 .nav-child-item { padding-left: 56px; }
.nav-item.nav-child-item { display: flex; align-items: center; justify-content: space-between; cursor: pointer; }
```

### 面包屑生成

```javascript
function generateBreadcrumb(currentPath) {
  const parts = currentPath.replace('.html', '').split('/');
  const crumbs = [{ name: 'Home', path: 'index.html' }];
  let acc = '';
  for (let i = 0; i < parts.length - 1; i++) {
    acc += parts[i] + '/';
    crumbs.push({ name: formatTitle(parts[i]), path: acc + 'index.html' });
  }
  crumbs.push({ name: formatTitle(parts[parts.length - 1]), path: null });
  return crumbs;
}
```

---

## 质量检查清单

构建完成后，逐项验证：

- [ ] 双击 `index.html` 可正常打开
- [ ] 侧边栏导航可折叠/展开
- [ ] 侧边栏导航高亮当前页并自动展开父级
- [ ] 从首页和子页面搜索，点击结果均可正确跳转
- [ ] 右侧目录面板显示在屏幕右侧，可收起/展开，内容多时可滚动
- [ ] 点击目录锚点可跳转，滚动时高亮跟随（ScrollSpy）
- [ ] 亮/暗主题切换正常，刷新后状态保留
- [ ] 代码块右上角有复制按钮，点击可复制代码
- [ ] 表格渲染正常（无分隔行噪点）
- [ ] 行内代码和代码块中的 HTML 标签显示为文本（不被解析）
- [ ] 响应式布局正常（窄屏侧边栏可收起，目录面板自动隐藏）
- [ ] 页面内容完整无截断，YAML Frontmatter 不显示
- [ ] 打印样式正常（隐藏侧边栏、目录面板、搜索等非内容元素）
