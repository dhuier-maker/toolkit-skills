# 交互组件模板

适用于大屏交互类组件，包括弹窗、导航标签、天气面板、日历面板等。

## 支持的模板

| 模板文件 | 说明 | 触发词 |
|----------|------|--------|
| `tech-modal.md` | 科幻风格弹窗，clip-path边框 + 发光角标 + 毛玻璃背景，支持3级下钻 | 科幻弹窗、TechModal、详情弹窗、下钻弹窗、科技弹窗 |
| `bottom-nav-tabs.md` | 底部导航标签，胶囊样式/图标文字模式，发光高亮 | 底部导航、BottomNavTabs、标签切换、底部Tab、导航标签 |
| `weather-panel.md` | 天气面板，当前天气 + 3日预报卡片 | 天气面板、WeatherPanel、天气组件、天气预报 |
| `calendar-panel.md` | 日历面板，月历网格 + 事件列表 | 日历面板、CalendarPanel、日历组件、日程面板 |

## 通用特点

- 所有交互组件均支持 techBlue（深蓝科技）/ partyRed（党建红金）/ lightBusiness（浅色商务）三种主题
- 通过 `theme` prop 切换主题，内部使用 CSS 变量映射实现主题色切换
- 组件均使用 Vue 3 `<script setup>` + Composition API 风格
- 样式使用 SCSS scoped，主题变量通过 `:root` 级 CSS 变量控制

## Props 通用规范

所有交互组件遵循相同的 Props 定义规范：

```javascript
// 主题配置
theme: {
  type: String,
  default: 'techBlue',
  desc: '主题风格：techBlue-深蓝科技/partyRed-党建红金/lightBusiness-浅色商务',
  name: '主题',
  groupKey: 'style',
  groupName: '样式配置',
  sort: 99,
  configurationTemplate: [
    { value: 'techBlue', label: '深蓝科技' },
    { value: 'partyRed', label: '党建红金' },
    { value: 'lightBusiness', label: '浅色商务' },
    { value: 'deepPurple', label: '紫蓝深邃' },
  ],
},
```

## 完整参考

所有交互组件完整代码请参考 `references/component-templates.md` 中对应的章节。
