# 地图悬浮数字模板 (MapFloatNumber)

完整参考：`references/component-templates.md` MapFloatNumber 章节

## 功能介绍

地图上悬浮显示的大号数字组件，支持多区域数据展示。数字带 count-up 滚动动画效果（requestAnimationFrame 驱动），下方显示区域名称和单位标签，底部渐变基线装饰。适用于文旅大数据地图核心指标展示、智慧乡村区域数据对比等场景。

## 目录结构

```
MapFloatNumber/
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
data: {
  type: Array,
  default: () => [
    { region: '莆田市', value: 125000, unit: '人次' },
    { region: '湄洲岛', value: 85000, unit: '人次' },
    { region: '仙游县', value: 62000, unit: '人次' },
  ],
  desc: i18n.global.t('dataSpecification'),
  name: i18n.global.t('displayContent'),
  groupKey: 'data',
  groupName: i18n.global.t('dataConfiguration'),
  useDynamic: true,
  sort: 1,
},
```

### 样式配置 (groupKey: 'style', groupName: '样式配置')

```javascript
fontSize: {
  type: Number,
  default: 48,
  desc: '数字字号（像素）',
  name: '数字字号',
  groupKey: 'style',
  groupName: '样式配置',
  sort: 2,
  min: 24,
  max: 96,
},

animationDuration: {
  type: Number,
  default: 1000,
  desc: '数字滚动动画时长（毫秒）',
  name: '动画时长',
  groupKey: 'style',
  groupName: '样式配置',
  sort: 3,
  min: 500,
  max: 3000,
},

theme: {
  type: String,
  default: 'techBlue',
  desc: i18n.global.t('themeStyle'),
  name: i18n.global.t('themeStyle'),
  groupKey: 'style',
  groupName: '样式配置',
  sort: 4,
},
```

## 完整代码

```vue
<template>
  <div class="map-float-number-container" :class="`theme-${props.theme}`" :style="cssVars">
    <div
      v-for="(item, index) in props.data"
      :key="index"
      class="float-number-item"
    >
      <div class="number-display">
        <span class="number-value">{{ getDisplayValue(index) }}</span>
        <span v-if="item.unit" class="number-unit">{{ item.unit }}</span>
      </div>
      <div class="number-label">{{ item.region }}</div>
      <div class="base-line"></div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, watch, onMounted, onUnmounted } from 'vue';
import i18n from './locale/index';

const props = defineProps({
  data: {
    type: Array,
    default: () => [
      { region: '莆田市', value: 125000, unit: '人次' },
      { region: '湄洲岛', value: 85000, unit: '人次' },
      { region: '仙游县', value: 62000, unit: '人次' },
    ],
    desc: i18n.global.t('dataSpecification'),
    name: i18n.global.t('displayContent'),
    groupKey: 'data',
    groupName: i18n.global.t('dataConfiguration'),
    useDynamic: true,
    sort: 1,
  },
  fontSize: {
    type: Number,
    default: 48,
    desc: '数字字号（像素）',
    name: '数字字号',
    groupKey: 'style',
    groupName: '样式配置',
    sort: 2,
    min: 24,
    max: 96,
  },
  animationDuration: {
    type: Number,
    default: 1000,
    desc: '数字滚动动画时长（毫秒）',
    name: '动画时长',
    groupKey: 'style',
    groupName: '样式配置',
    sort: 3,
    min: 500,
    max: 3000,
  },
  theme: {
    type: String,
    default: 'techBlue',
    desc: i18n.global.t('themeStyle'),
    name: i18n.global.t('themeStyle'),
    groupKey: 'style',
    groupName: '样式配置',
    sort: 4,
  },
});

const currentValues = ref(props.data.map(() => 0));
const animationFrames = ref([]);

const themeColors = {
  techBlue: { primary: '#00d4aa', glow: '#00d4aacc', glowSoft: '#00d4aa60' },
  partyRed: { primary: '#e63946', glow: '#e63946cc', glowSoft: '#e6394660' },
  lightBusiness: { primary: '#4a90e2', glow: '#4a90e2cc', glowSoft: '#4a90e260' },
  ecoGreen: { primary: '#f5a623', glow: '#f5a623cc', glowSoft: '#f5a62360' },
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
};

const cssVars = computed(() => {
  const colors = themeColors[props.theme] || themeColors.techBlue;
  return {
    '--num-color': colors.primary,
    '--num-glow': colors.glow,
    '--num-glow-soft': colors.glowSoft,
    '--num-font-size': `${props.fontSize}px`,
  };
});

const getDisplayValue = (index) => {
  return Math.round(currentValues.value[index]).toLocaleString();
};

const animateValue = (index, from, to) => {
  const duration = props.animationDuration;
  const startTime = performance.now();
  const step = (timestamp) => {
    const progress = Math.min((timestamp - startTime) / duration, 1);
    const eased = 1 - Math.pow(1 - progress, 3); // easeOutCubic
    currentValues.value[index] = from + (to - from) * eased;
    if (progress < 1) {
      animationFrames.value[index] = requestAnimationFrame(step);
    }
  };
  if (animationFrames.value[index]) cancelAnimationFrame(animationFrames.value[index]);
  animationFrames.value[index] = requestAnimationFrame(step);
};

watch(() => props.data, (newData, oldData) => {
  newData.forEach((item, index) => {
    const oldVal = oldData?.[index]?.value ?? 0;
    animateValue(index, oldVal, item.value);
  });
}, { deep: true });

onMounted(() => {
  props.data.forEach((item, index) => {
    animateValue(index, 0, item.value);
  });
});

onUnmounted(() => {
  animationFrames.value.forEach((frame) => {
    if (frame) cancelAnimationFrame(frame);
  });
});
</script>

<style lang="scss" scoped>
.map-float-number-container {
  position: absolute;
  display: flex;
  flex-direction: column;
  gap: 20px;
  pointer-events: none;
  z-index: 100;
}

.float-number-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 12px 20px;
}

.number-display {
  display: flex;
  align-items: baseline;
  .number-value {
    font-size: var(--num-font-size);
    font-weight: bold;
    font-family: 'DIN', 'Orbitron', monospace;
    color: var(--num-color);
    text-shadow: 0 0 12px var(--num-glow), 0 0 24px var(--num-glow-soft);
    line-height: 1;
  }
  .number-unit {
    font-size: 16px;
    color: var(--num-color);
    margin-left: 4px;
    opacity: 0.8;
  }
}

.number-label {
  font-size: 14px;
  color: rgba(255, 255, 255, 0.7);
  margin-top: 4px;
  letter-spacing: 2px;
}

.base-line {
  width: 80%;
  height: 2px;
  margin-top: 8px;
  background: linear-gradient(90deg, transparent, var(--num-color), transparent);
  opacity: 0.6;
}

// 主题变体
.theme-partyRed {
  .number-label { color: rgba(255, 215, 0, 0.7); }
}

.theme-lightBusiness {
  .number-value { text-shadow: none; }
  .number-label { color: rgba(0, 0, 0, 0.6); }
  .base-line { opacity: 0.4; }
}

.theme-ecoGreen {
  .number-label { color: rgba(245, 166, 35, 0.7); }
}
</style>
```

## 主题变量支持 (theme prop)

### 主题值表

| theme 值 | 中文名 | 主色 | 发光色 | 适用场景 |
|-----------|--------|------|--------|----------|
| techBlue | 深蓝科技 | #00d4aa | #00d4aacc | 智慧乡村/社区大屏 |
| partyRed | 党建红金 | #e63946 | #e63946cc | 党建大屏 |
| lightBusiness | 浅色商务 | #4a90e2 | #4a90e2cc | 智慧街道/浅色大屏 |
| ecoGreen | 青绿生态 | #f5a623 | #f5a623cc | 文旅大数据大屏 |

### Props 定义

```javascript
theme: {
  type: String,
  default: 'techBlue',
  desc: '主题风格',
  name: '主题',
  groupKey: 'style',
  groupName: '样式配置',
  sort: 4,
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
| --num-color | #00d4aa | #e63946 | #4a90e2 | #f5a623 |
| --num-glow | #00d4aacc | #e63946cc | #4a90e2cc | #f5a623cc |
| --num-glow-soft | #00d4aa60 | #e6394660 | #4a90e260 | #f5a62360 |