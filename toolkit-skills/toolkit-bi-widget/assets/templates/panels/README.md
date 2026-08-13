# 面板组件模板

适用于大屏科技感面板组件，包括点阵面板、四角装饰面板、渐变头部面板等。

## 支持的模板

| 模板文件 | 说明 | 触发词 |
|----------|------|--------|
| `dot-matrix.md` | 点阵面板，深蓝科技风格，头部带点阵装饰 | 点阵面板、DotMatrixPanel、科技感面板 |
| `corner-decorated.md` | 四角装饰面板，四角带装饰线条 | 四角装饰面板、CornerDecoratedPanel、发光边框面板 |
| `gradient-header.md` | 渐变头部面板，浅色主题，蓝色渐变标题栏 | 渐变头部面板、GradientHeaderPanel、浅色面板 |

## 通用特点

- 所有面板组件均提供标题、图标、主题切换功能
- 支持 slot 插槽嵌入子组件内容
- 提供 header-extra 插槽用于头部右侧扩展
- 支持 dark（深蓝科技）/ red（党建红金）/ light（浅色商务）三种主题

## Props 通用规范

所有面板组件遵循相同的 Props 定义规范：

```javascript
// 基础配置 (groupKey: 'basic')
title: { type: String, default: '面板标题' },
icon: { type: String, default: '' },
iconUrl: { type: String, default: '' },

// 样式配置 (groupKey: 'style')
width: { type: [String, Number], default: '100%' },
height: { type: [String, Number], default: 'auto' },
theme: { type: String, default: 'dark' },
```

## 完整参考

所有面板组件完整代码请参考 `references/component-templates.md` 中对应的章节。