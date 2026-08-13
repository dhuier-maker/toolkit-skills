# 渐变头部面板模板 (GradientHeaderPanel)

完整参考：`references/component-templates.md` GradientHeaderPanel 章节

## 功能介绍

浅色商务主题面板，头部为蓝色渐变背景条。适用于智慧街道等浅色主题大屏。

## Props 定义

### 基础配置 (groupKey: 'basic')

```javascript
title: { type: String, default: '面板标题' },
icon: { type: String, default: '' },
iconUrl: { type: String, default: '' },
tag: {
  type: String,
  default: '',
  desc: '头部右侧标签文字，如"本月"',
  name: '标签',
  groupKey: 'basic',
  groupName: '基础配置',
  sort: 4,
},
showMore: {
  type: Boolean,
  default: false,
  desc: '是否显示"更多"链接',
  name: '显示更多',
  groupKey: 'basic',
  groupName: '基础配置',
  sort: 5,
},
```

### 样式配置 (groupKey: 'style', groupName: '样式配置')

| 属性名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| width | String/Number | '100%' | 面板宽度 |
| height | String/Number | 'auto' | 面板高度 |
| theme | String | 'light' | 主题：light/dark |

## emit 事件

- `more` - 点击"更多"链接时触发

## 模板结构

```html
<div class="gradient-header-panel" :class="[`theme-${theme}`]" :style="panelStyle">
  <!-- 头部区域 - 渐变背景 -->
  <div class="panel-header">
    <div class="header-left">
      <span class="header-arrow">▶</span>
      <div v-if="icon" class="header-icon">...</div>
      <span class="header-title">{{ title }}</span>
    </div>
    <div class="header-right">
      <slot name="header-tag">
        <span v-if="tag" class="header-tag">{{ tag }}</span>
      </slot>
      <span v-if="showMore" class="more-link" @click="$emit('more')">更多 >>></span>
    </div>
  </div>

  <!-- 内容区域 -->
  <div class="panel-content">
    <slot></slot>
  </div>
</div>
```

## 完整代码

完整渐变头部面板代码请参考 `references/component-templates.md` 中 GradientHeaderPanel 章节。


## 主题变量支持 (theme prop)

### 主题值

| 主题 | panelBg | borderColor | borderGlow | textPrimary | textSecondary | accentColor | headerBg | dotColor |
|------|---------|-------------|------------|-------------|---------------|-------------|----------|----------|
| techBlue | rgba(6,30,93,0.8) | rgba(0,212,255,0.3) | rgba(0,212,255,0.6) | #E0E8FF | #6B7FA3 | #00D4FF | rgba(0,212,255,0.08) | rgba(0,212,255,0.3) |
| ecoGreen | rgba(6,42,42,0.8) | rgba(0,229,195,0.3) | rgba(0,229,195,0.6) | #E0FFF0 | #5A8A7A | #00E5C3 | rgba(0,229,195,0.08) | rgba(0,229,195,0.3) |
| partyRed | rgba(60,15,15,0.8) | rgba(255,77,79,0.4) | rgba(255,215,0,0.6) | #FFE0E0 | #8A6A6A | #FF4D4F | rgba(255,77,79,0.08) | rgba(255,77,79,0.3) |
| warmOrange | rgba(50,35,15,0.8) | rgba(255,140,66,0.3) | rgba(255,140,66,0.6) | #FFF0E0 | #8A7A6A | #FF8C42 | rgba(255,140,66,0.08) | rgba(255,140,66,0.3) |
| deepPurple | rgba(20,16,60,0.8) | rgba(168,85,247,0.3) | rgba(168,85,247,0.6) | #E8E0FF | #7A6A8A | #A855F7 | rgba(168,85,247,0.08) | rgba(168,85,247,0.3) |
| lightBusiness | rgba(255,255,255,0.95) | #E8E8E8 | transparent | #595959 | #8C8C8C | #1890FF | rgba(24,144,255,0.06) | rgba(24,144,255,0.2) |

### Theme Props Definition

```javascript
theme: {
  type: String,
  default: 'techBlue',
  desc: i18n.global.t('themeStyle'),
  name: i18n.global.t('themeStyle'),
  groupKey: 'style',
  groupName: i18n.global.t('styleConfiguration'),
  sort: 99,
},
```

### Theme CSS Variable Mapping

```javascript
const themeVariables = {
  techBlue: {
    panelBg: 'rgba(6,30,93,0.8)',
    borderColor: 'rgba(0,212,255,0.3)',
    borderGlow: 'rgba(0,212,255,0.6)',
    textPrimary: '#E0E8FF',
    textSecondary: '#6B7FA3',
    accentColor: '#00D4FF',
    headerBg: 'rgba(0,212,255,0.08)',
    dotColor: 'rgba(0,212,255,0.3)',
  },
  ecoGreen: {
    panelBg: 'rgba(6,42,42,0.8)',
    borderColor: 'rgba(0,229,195,0.3)',
    borderGlow: 'rgba(0,229,195,0.6)',
    textPrimary: '#E0FFF0',
    textSecondary: '#5A8A7A',
    accentColor: '#00E5C3',
    headerBg: 'rgba(0,229,195,0.08)',
    dotColor: 'rgba(0,229,195,0.3)',
  },
  partyRed: {
    panelBg: 'rgba(60,15,15,0.8)',
    borderColor: 'rgba(255,77,79,0.4)',
    borderGlow: 'rgba(255,215,0,0.6)',
    textPrimary: '#FFE0E0',
    textSecondary: '#8A6A6A',
    accentColor: '#FF4D4F',
    headerBg: 'rgba(255,77,79,0.08)',
    dotColor: 'rgba(255,77,79,0.3)',
  },
  warmOrange: {
    panelBg: 'rgba(50,35,15,0.8)',
    borderColor: 'rgba(255,140,66,0.3)',
    borderGlow: 'rgba(255,140,66,0.6)',
    textPrimary: '#FFF0E0',
    textSecondary: '#8A7A6A',
    accentColor: '#FF8C42',
    headerBg: 'rgba(255,140,66,0.08)',
    dotColor: 'rgba(255,140,66,0.3)',
  },
  deepPurple: {
    panelBg: 'rgba(20,16,60,0.8)',
    borderColor: 'rgba(168,85,247,0.3)',
    borderGlow: 'rgba(168,85,247,0.6)',
    textPrimary: '#E8E0FF',
    textSecondary: '#7A6A8A',
    accentColor: '#A855F7',
    headerBg: 'rgba(168,85,247,0.08)',
    dotColor: 'rgba(168,85,247,0.3)',
  },
  lightBusiness: {
    panelBg: 'rgba(255,255,255,0.95)',
    borderColor: '#E8E8E8',
    borderGlow: 'transparent',
    textPrimary: '#595959',
    textSecondary: '#8C8C8C',
    accentColor: '#1890FF',
    headerBg: 'rgba(24,144,255,0.06)',
    dotColor: 'rgba(24,144,255,0.2)',
  },
}
```
