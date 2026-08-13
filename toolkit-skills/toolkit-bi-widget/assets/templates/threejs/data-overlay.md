# 数据叠加层模板 (DataOverlay)

完整参考：`references/component-templates.md` DataOverlay 章节

## 功能介绍

数据叠加层组件，在3D场景上叠加固定位置的数据面板。面板采用半透明背景+模糊效果(backdrop-filter)，显示标题和多组数据指标。可选显示迷你趋势折线图(sparkline)。适用于3D城市/地球场景的数据面板叠加、数字孪生场景指标展示、3D模型数据信息面板等场景。

## 目录结构

```
DataOverlay/
├── index.js
└── src/
    ├── index.vue
    ├── components/
    │   └── style/
    ├── locale/
    │   ├── index.js
    │   └── lang/
    │       ├── zh-cn.json
    │       └── en.json
    └── static/
        └── img/
```

## Props 定义

### 数据配置 (groupKey: 'data')

```javascript
title: {
  type: String,
  default: '区域数据',
  desc: '面板标题',
  name: '标题',
  groupKey: 'data',
  groupName: i18n.global.t('dataConfiguration'),
  sort: 1,
},

data: {
  type: Array,
  default: () => [
    { label: '总人口', value: 12580, unit: '人', color: '#00d4ff' },
    { label: '面积', value: 36.5, unit: 'km²', color: '#00d4aa' },
    { label: '增长率', value: 12.3, unit: '%', color: '#f5a623' },
  ],
  desc: i18n.global.t('dataSpecification'),
  name: i18n.global.t('displayContent'),
  groupKey: 'data',
  groupName: i18n.global.t('dataConfiguration'),
  useDynamic: true,
  sort: 2,
},
```

### 样式配置 (groupKey: 'style', groupName: '样式配置')

```javascript
position: {
  type: String,
  default: 'top-right',
  desc: '面板位置：top-left/top-right/bottom-left/bottom-right',
  name: '面板位置',
  groupKey: 'style',
  groupName: '样式配置',
  sort: 3,
  configurationTemplate: [
    { value: 'top-left', label: '左上' },
    { value: 'top-right', label: '右上' },
    { value: 'bottom-left', label: '左下' },
    { value: 'bottom-right', label: '右下' },
  ],
},

showSparkline: {
  type: Boolean,
  default: false,
  desc: '是否显示迷你趋势折线',
  name: '趋势折线',
  groupKey: 'style',
  groupName: '样式配置',
  sort: 4,
},

theme: {
  type: String,
  default: 'techBlue',
  desc: i18n.global.t('themeStyle'),
  name: i18n.global.t('themeStyle'),
  groupKey: 'style',
  groupName: '样式配置',
  sort: 5,
},
```

## 完整代码

```vue
<template>
  <div class="data-overlay" :class="[`pos-${props.position}`, `theme-${props.theme}`]" :style="cssVars">
    <!-- 面板标题 -->
    <div class="overlay-header">
      <div class="header-indicator"></div>
      <span class="header-title">{{ props.title }}</span>
    </div>

    <!-- 数据列表 -->
    <div class="overlay-data-list">
      <div
        v-for="(item, index) in props.data"
        :key="index"
        class="data-item"
      >
        <span class="data-label">{{ item.label }}</span>
        <div class="data-value-row">
          <span class="data-value" :style="{ color: item.color }">{{ formatValue(item.value) }}</span>
          <span v-if="item.unit" class="data-unit">{{ item.unit }}</span>
        </div>
        <!-- 迷你趋势折线 -->
        <svg v-if="props.showSparkline" class="sparkline" viewBox="0 0 60 20" preserveAspectRatio="none">
          <polyline
            :points="getSparklinePoints(index)"
            fill="none"
            :stroke="item.color"
            stroke-width="1.5"
            stroke-linecap="round"
            stroke-linejoin="round"
          />
        </svg>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue';
import i18n from './locale/index';

const props = defineProps({
  title: {
    type: String,
    default: '区域数据',
    desc: '面板标题',
    name: '标题',
    groupKey: 'data',
    groupName: i18n.global.t('dataConfiguration'),
    sort: 1,
  },
  data: {
    type: Array,
    default: () => [
      { label: '总人口', value: 12580, unit: '人', color: '#00d4ff' },
      { label: '面积', value: 36.5, unit: 'km²', color: '#00d4aa' },
      { label: '增长率', value: 12.3, unit: '%', color: '#f5a623' },
    ],
    desc: i18n.global.t('dataSpecification'),
    name: i18n.global.t('displayContent'),
    groupKey: 'data',
    groupName: i18n.global.t('dataConfiguration'),
    useDynamic: true,
    sort: 2,
  },
  position: {
    type: String,
    default: 'top-right',
    desc: '面板位置：top-left/top-right/bottom-left/bottom-right',
    name: '面板位置',
    groupKey: 'style',
    groupName: '样式配置',
    sort: 3,
    configurationTemplate: [
      { value: 'top-left', label: '左上' },
      { value: 'top-right', label: '右上' },
      { value: 'bottom-left', label: '左下' },
      { value: 'bottom-right', label: '右下' },
    ],
  },
  showSparkline: {
    type: Boolean,
    default: false,
    desc: '是否显示迷你趋势折线',
    name: '趋势折线',
    groupKey: 'style',
    groupName: '样式配置',
    sort: 4,
  },
  theme: {
    type: String,
    default: 'techBlue',
    desc: i18n.global.t('themeStyle'),
    name: i18n.global.t('themeStyle'),
    groupKey: 'style',
    groupName: '样式配置',
    sort: 5,
  },
});

const themeColors = {
  techBlue: {
    panelBg: 'rgba(5, 25, 55, 0.75)',
    panelBorder: 'rgba(0, 212, 255, 0.3)',
    headerBorder: 'rgba(0, 212, 255, 0.2)',
    indicatorColor: '#00d4ff',
    titleColor: '#fff',
    labelColor: 'rgba(255, 255, 255, 0.6)',
    unitColor: 'rgba(255, 255, 255, 0.45)',
  },
  partyRed: {
    panelBg: 'rgba(60, 10, 15, 0.75)',
    panelBorder: 'rgba(230, 57, 70, 0.3)',
    headerBorder: 'rgba(230, 57, 70, 0.2)',
    indicatorColor: '#e63946',
    titleColor: '#ffd700',
    labelColor: 'rgba(255, 215, 0, 0.6)',
    unitColor: 'rgba(255, 215, 0, 0.45)',
  },
  lightBusiness: {
    panelBg: 'rgba(255, 255, 255, 0.88)',
    panelBorder: 'rgba(74, 144, 226, 0.25)',
    headerBorder: 'rgba(74, 144, 226, 0.15)',
    indicatorColor: '#4a90e2',
    titleColor: '#333',
    labelColor: 'rgba(0, 0, 0, 0.55)',
    unitColor: 'rgba(0, 0, 0, 0.4)',
  },
  ecoGreen: {
    '--tab-bg': 'rgba(0,229,195,0.06)',
    '--tab-border-color': 'rgba(0,229,195,0.2)',
    '--tab-text-color': 'rgba(224,255,240,0.6)',
    '--tab-hover-bg': 'rgba(0,229,195,0.1)',
    '--tab-active-bg': 'rgba(0,229,195,0.15)',
    '--tab-active-border': '#00E5C3',
    '--tab-active-text': '#E0FFF0',
    '--tab-glow-color': 'rgba(0,229,195,0.4)',
    '--tab-glow-inner': 'rgba(0,229,195,0.08)',
  },
  warmOrange: {
    '--tab-bg': 'rgba(255,140,66,0.06)',
    '--tab-border-color': 'rgba(255,140,66,0.2)',
    '--tab-text-color': 'rgba(255,240,224,0.6)',
    '--tab-hover-bg': 'rgba(255,140,66,0.1)',
    '--tab-active-bg': 'rgba(255,140,66,0.15)',
    '--tab-active-border': '#FF8C42',
    '--tab-active-text': '#FFF0E0',
    '--tab-glow-color': 'rgba(255,140,66,0.4)',
    '--tab-glow-inner': 'rgba(255,140,66,0.08)',
  },
  deepPurple: {
    '--tab-bg': 'rgba(168,85,247,0.06)',
    '--tab-border-color': 'rgba(168,85,247,0.2)',
    '--tab-text-color': 'rgba(232,224,255,0.6)',
    '--tab-hover-bg': 'rgba(168,85,247,0.1)',
    '--tab-active-bg': 'rgba(168,85,247,0.15)',
    '--tab-active-border': '#A855F7',
    '--tab-active-text': '#E8E0FF',
    '--tab-glow-color': 'rgba(168,85,247,0.4)',
    '--tab-glow-inner': 'rgba(168,85,247,0.08)',
  },
  ecoGreen: {
    panelBg: 'rgba(40, 25, 5, 0.75)',
    panelBorder: 'rgba(245, 166, 35, 0.3)',
    headerBorder: 'rgba(245, 166, 35, 0.2)',
    indicatorColor: '#f5a623',
    titleColor: '#f5a623',
    labelColor: 'rgba(245, 166, 35, 0.6)',
    unitColor: 'rgba(245, 166, 35, 0.45)',
  },
};

const cssVars = computed(() => {
  const colors = themeColors[props.theme] || themeColors.techBlue;
  return {
    '--do-panel-bg': colors.panelBg,
    '--do-panel-border': colors.panelBorder,
    '--do-header-border': colors.headerBorder,
    '--do-indicator-color': colors.indicatorColor,
    '--do-title-color': colors.titleColor,
    '--do-label-color': colors.labelColor,
    '--do-unit-color': colors.unitColor,
  };
});

const formatValue = (value) => {
  if (typeof value === 'number' && value >= 10000) {
    return (value / 10000).toFixed(1) + '万';
  }
  if (typeof value === 'number') {
    return value.toLocaleString();
  }
  return value;
};

// 生成迷你折线图的模拟数据点
const getSparklinePoints = (index) => {
  const points = [];
  const seed = index * 7 + 3;
  for (let i = 0; i <= 6; i++) {
    const x = i * 10;
    const y = 10 + Math.sin(seed + i * 0.8) * 8;
    points.push(`${x},${y.toFixed(1)}`);
  }
  return points.join(' ');
};
</script>

<style lang="scss" scoped>
.data-overlay {
  position: absolute;
  z-index: 50;
  min-width: 180px;
  max-width: 280px;
  background: var(--do-panel-bg);
  border: 1px solid var(--do-panel-border);
  border-radius: 6px;
  backdrop-filter: blur(12px);
  overflow: hidden;

  &.pos-top-left { top: 16px; left: 16px; }
  &.pos-top-right { top: 16px; right: 16px; }
  &.pos-bottom-left { bottom: 16px; left: 16px; }
  &.pos-bottom-right { bottom: 16px; right: 16px; }
}

.overlay-header {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 10px 14px;
  border-bottom: 1px solid var(--do-header-border);
}

.header-indicator {
  width: 3px;
  height: 14px;
  border-radius: 2px;
  background: var(--do-indicator-color);
}

.header-title {
  font-size: 13px;
  font-weight: 500;
  color: var(--do-title-color);
}

.overlay-data-list {
  padding: 10px 14px;
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.data-item {
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.data-label {
  font-size: 11px;
  color: var(--do-label-color);
}

.data-value-row {
  display: flex;
  align-items: baseline;
  gap: 3px;
}

.data-value {
  font-size: 18px;
  font-weight: bold;
  font-family: 'DIN', 'Orbitron', monospace;
  line-height: 1;
}

.data-unit {
  font-size: 11px;
  color: var(--do-unit-color);
}

.sparkline {
  width: 100%;
  height: 16px;
  margin-top: 2px;
  opacity: 0.7;
}

// 主题变体
.theme-lightBusiness {
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.08);
}
</style>
```

## 主题变量支持 (theme prop)

### 主题值表

| theme 值 | 中文名 | 面板背景 | 标题色 | 指示器色 | 适用场景 |
|-----------|--------|----------|--------|----------|----------|
| techBlue | 深蓝科技 | rgba(5,25,55,0.75) | #fff | #00d4ff | 智慧乡村/社区大屏 |
| partyRed | 党建红金 | rgba(60,10,15,0.75) | #ffd700 | #e63946 | 党建大屏 |
| lightBusiness | 浅色商务 | rgba(255,255,255,0.88) | #333 | #4a90e2 | 智慧街道/浅色大屏 |
| ecoGreen | 青绿生态 | rgba(40,25,5,0.75) | #f5a623 | #f5a623 | 文旅大数据大屏 |

### Props 定义

```javascript
theme: {
  type: String,
  default: 'techBlue',
  desc: '主题风格',
  name: '主题',
  groupKey: 'style',
  groupName: '样式配置',
  sort: 5,
  configurationTemplate: [
    { value: 'techBlue', label: '深蓝科技' },
    { value: 'partyRed', label: '党建红金' },
    { value: 'warmOrange', label: '暖橙数据' },
    { value: 'lightBusiness', label: '浅色商务' },
    { value: 'deepPurple', label: '紫蓝深邃' },
    { value: 'ecoGreen', label: '青绿生态' },
  ],
},
```

### CSS 变量映射

| CSS 变量 | techBlue | partyRed | lightBusiness | ecoGreen |
|----------|----------|----------|-------------|---------|
| --do-panel-bg | rgba(5,25,55,0.75) | rgba(60,10,15,0.75) | rgba(255,255,255,0.88) | rgba(40,25,5,0.75) |
| --do-panel-border | rgba(0,212,255,0.3) | rgba(230,57,70,0.3) | rgba(74,144,226,0.25) | rgba(245,166,35,0.3) |
| --do-header-border | rgba(0,212,255,0.2) | rgba(230,57,70,0.2) | rgba(74,144,226,0.15) | rgba(245,166,35,0.2) |
| --do-indicator-color | #00d4ff | #e63946 | #4a90e2 | #f5a623 |
| --do-title-color | #fff | #ffd700 | #333 | #f5a623 |
| --do-label-color | rgba(255,255,255,0.6) | rgba(255,215,0,0.6) | rgba(0,0,0,0.55) | rgba(245,166,35,0.6) |
| --do-unit-color | rgba(255,255,255,0.45) | rgba(255,215,0,0.45) | rgba(0,0,0,0.4) | rgba(245,166,35,0.45) |