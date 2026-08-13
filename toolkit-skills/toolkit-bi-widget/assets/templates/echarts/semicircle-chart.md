# 半圆环形图模板 (SemicircleChart)

完整参考：`references/component-templates.md` SemicircleChart 章节

## 功能介绍

半圆环形图组件，基于 ECharts 饼图实现。startAngle: 180, endAngle: 360（开口朝上），center 定位在底部。支持多色分段、标签显示、中心数值显示。适用于智慧街道党建民生、人口结构、资金分配等占比展示场景。

## 目录结构

```
SemicircleChart/
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
chartData: {
  type: Array,
  default: () => [
    { name: '分类A', value: 40 },
    { name: '分类B', value: 30 },
    { name: '分类C', value: 20 },
    { name: '分类D', value: 10 },
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
radius: {
  type: Array,
  default: () => ['40%', '70%'],
  desc: '环图半径 [内径, 外径]',
  name: '环图半径',
  groupKey: 'style',
  groupName: '样式配置',
  sort: 2,
},

centerColor: {
  type: String,
  default: '#00d4ff',
  desc: '中心数值颜色',
  name: '中心颜色',
  groupKey: 'style',
  groupName: '样式配置',
  sort: 3,
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
  <div class="semicircle-chart" :class="`theme-${props.theme}`" :style="cssVars">
    <div ref="chartRef" class="chart-container"></div>
    <!-- 中心数值 -->
    <div class="center-info">
      <span class="center-value">{{ totalValue }}</span>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, watch, onMounted, onUnmounted, nextTick } from 'vue';
import * as echarts from 'echarts';
import i18n from './locale/index';

const props = defineProps({
  chartData: {
    type: Array,
    default: () => [
      { name: '分类A', value: 40 },
      { name: '分类B', value: 30 },
      { name: '分类C', value: 20 },
      { name: '分类D', value: 10 },
    ],
    desc: i18n.global.t('dataSpecification'),
    name: i18n.global.t('displayContent'),
    groupKey: 'data',
    groupName: i18n.global.t('dataConfiguration'),
    useDynamic: true,
    sort: 1,
  },
  radius: {
    type: Array,
    default: () => ['40%', '70%'],
    desc: '环图半径 [内径, 外径]',
    name: '环图半径',
    groupKey: 'style',
    groupName: '样式配置',
    sort: 2,
  },
  centerColor: {
    type: String,
    default: '#00d4ff',
    desc: '中心数值颜色',
    name: '中心颜色',
    groupKey: 'style',
    groupName: '样式配置',
    sort: 3,
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

const chartRef = ref(null);
let chartInstance = null;

const themeConfig = {
  techBlue: {
    labelColor: '#fff',
    labelColorInner: 'rgba(255,255,255,0.7)',
    colors: ['#00D4FF', '#0088FF', '#FF6B6B', '#FFD93D', '#44FFAA'],
  },
  ecoGreen: {
    labelColor: '#fff',
    labelColorInner: 'rgba(255,255,255,0.7)',
    colors: ['#00E5C3', '#00FF88', '#44FFAA', '#26C6DA', '#FFD93D'],
  },
  partyRed: {
    labelColor: '#FFD700',
    labelColorInner: 'rgba(255,215,0,0.7)',
    colors: ['#FF4D4F', '#FFD700', '#FF8C00', '#FFFFFF', '#FF69B4'],
  },
  warmOrange: {
    labelColor: '#FFF0E0',
    labelColorInner: 'rgba(255,240,224,0.7)',
    colors: ['#FF8C42', '#FFB347', '#FFD93D', '#FF6B6B', '#44FFAA'],
  },
  deepPurple: {
    labelColor: '#E8E0FF',
    labelColorInner: 'rgba(232,224,255,0.7)',
    colors: ['#A855F7', '#6366F1', '#C084FC', '#00D4FF', '#FF6B6B'],
  },
  lightBusiness: {
    labelColor: '#333',
    labelColorInner: 'rgba(0,0,0,0.5)',
    colors: ['#1890FF', '#52C41A', '#FAAD14', '#F5222D', '#722ED1'],
  },
};

const cssVars = computed(() => ({
  '--center-color': props.centerColor,
}));

const totalValue = computed(() => {
  return props.chartData.reduce((sum, item) => sum + item.value, 0);
});

const option = computed(() => {
  const tc = themeConfig[props.theme] || themeConfig.techBlue;
  return {
    tooltip: {
      trigger: 'item',
      confine: true,
      backgroundColor: 'rgba(0,0,0,0.8)',
      textStyle: { color: '#fff' },
    },
    series: [{
      type: 'pie',
      startAngle: 180,
      endAngle: 360,
      center: ['50%', '70%'],
      radius: props.radius,
      avoidLabelOverlap: false,
      label: {
        show: true,
        color: tc.labelColor,
        fontSize: 12,
        formatter: '{b}\n{d}%',
      },
      labelLine: {
        show: true,
        lineStyle: { color: tc.labelColorInner },
      },
      data: props.chartData.map((item, index) => ({
        name: item.name,
        value: item.value,
        itemStyle: {
          color: tc.colors[index % tc.colors.length],
        },
      })),
      emphasis: {
        itemStyle: {
          shadowBlur: 10,
          shadowOffsetX: 0,
          shadowColor: 'rgba(0,0,0,0.5)',
        },
      },
    }],
  };
});

const initChart = () => {
  if (!chartRef.value) return;
  chartInstance = echarts.init(chartRef.value);
  chartInstance.setOption(option.value);
};

const resizeObserver = new ResizeObserver(() => {
  chartInstance?.resize();
});

watch(option, (val) => {
  chartInstance?.setOption(val);
}, { deep: true });

onMounted(async () => {
  await nextTick();
  initChart();
  if (chartRef.value) resizeObserver.observe(chartRef.value);
});

onUnmounted(() => {
  resizeObserver.disconnect();
  chartInstance?.dispose();
  chartInstance = null;
});
</script>

<style lang="scss" scoped>
.semicircle-chart {
  position: relative;
  width: 100%;
  height: 100%;
  min-height: 180px;
}

.chart-container {
  width: 100%;
  height: 100%;
}

.center-info {
  position: absolute;
  bottom: 10%;
  left: 50%;
  transform: translateX(-50%);
  text-align: center;
  pointer-events: none;
}

.center-value {
  font-size: 24px;
  font-weight: bold;
  color: var(--center-color);
  font-family: 'DIN', 'Orbitron', monospace;
  text-shadow: 0 0 8px var(--center-color);
}

// 主题变体
.theme-lightBusiness {
  .center-value { text-shadow: none; }
}
</style>
```

## 主题变量支持 (theme prop)

### 主题值表

| theme 值 | 中文名 | 标签色 | 配色序列 | 适用场景 |
|-----------|--------|--------|----------|----------|
| techBlue | 深蓝科技 | #fff | #00D4FF, #0088FF, #FF6B6B, #FFD93D, #44FFAA | 智慧乡村/社区大屏 |
| ecoGreen | 青绿生态 | #fff | #00E5C3, #00FF88, #44FFAA, #26C6DA, #FFD93D | 文旅/生态大屏 |
| partyRed | 党建红金 | #FFD700 | #FF4D4F, #FFD700, #FF8C00, #FFFFFF, #FF69B4 | 党建大屏 |
| warmOrange | 暖橙数据 | #FFF0E0 | #FF8C42, #FFB347, #FFD93D, #FF6B6B, #44FFAA | 暖色数据大屏 |
| deepPurple | 紫蓝深邃 | #E8E0FF | #A855F7, #6366F1, #C084FC, #00D4FF, #FF6B6B | 紫蓝科技大屏 |
| lightBusiness | 浅色商务 | #333 | #1890FF, #52C41A, #FAAD14, #F5222D, #722ED1 | 智慧街道/浅色大屏 |

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
    { value: 'ecoGreen', label: '青绿生态' },
    { value: 'partyRed', label: '党建红金' },
    { value: 'warmOrange', label: '暖橙数据' },
    { value: 'deepPurple', label: '紫蓝深邃' },
    { value: 'lightBusiness', label: '浅色商务' },
  ],
},
```

### CSS 变量映射

| CSS 变量 | techBlue | ecoGreen | partyRed | warmOrange | deepPurple | lightBusiness |
|----------|----------|----------|----------|------------|------------|---------------|
| --center-color | #00D4FF | #00E5C3 | #FF4D4F | #FF8C42 | #A855F7 | #1890FF |