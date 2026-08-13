# 点阵面板模板 (DotMatrixPanel)

完整参考：`references/component-templates.md` DotMatrixPanel 章节

## 功能介绍

深蓝科技风格面板，头部带点阵装饰纹理，适用于智慧乡村、智慧民宗等深蓝科技主题大屏。

## Props 定义

### 基础配置 (groupKey: 'basic')

```javascript
title: {
  type: String,
  default: '面板标题',
  desc: '面板标题文字',
  name: '标题',
  groupKey: 'basic',
  groupName: '基础配置',
  sort: 1,
},
icon: {
  type: String,
  default: '',
  desc: '标题图标（文字或emoji）',
  name: '图标',
  groupKey: 'basic',
  groupName: '基础配置',
  sort: 2,
},
iconUrl: {
  type: String,
  default: '',
  desc: '图标图片URL',
  name: '图标URL',
  groupKey: 'basic',
  groupName: '基础配置',
  sort: 3,
},
```

### 样式配置 (groupKey: 'style', groupName: '样式配置')

| 属性名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| width | String/Number | '100%' | 面板宽度 |
| height | String/Number | 'auto' | 面板高度 |
| theme | String | 'dark' | 主题：dark/red/light |

## 模板结构

```html
<div class="dot-matrix-panel" :class="[`theme-${theme}`]" :style="panelStyle">
  <!-- 头部区域 -->
  <div class="panel-header">
    <div class="header-left">
      <!-- 点阵装饰 -->
      <div class="dot-matrix">
        <span v-for="i in 9" :key="i" class="dot"></span>
      </div>
      <!-- 图标 -->
      <div v-if="icon" class="header-icon">
        <img v-if="iconUrl" :src="iconUrl" class="icon-img" />
        <span v-else class="icon-default">{{ icon }}</span>
      </div>
      <!-- 标题 -->
      <span class="header-title">{{ title }}</span>
    </div>
    <div class="header-right">
      <slot name="header-extra"></slot>
    </div>
  </div>
  <!-- 内容区域 -->
  <div class="panel-content">
    <slot></slot>
  </div>
</div>
```

## 完整代码

完整点阵面板代码请参考 `references/component-templates.md` 中 DotMatrixPanel 章节。


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
