# 3D浮动标注模板 (FloatingLabel3D)

完整参考：`references/component-templates.md` FloatingLabel3D 章节

## 功能介绍

3D浮动标注组件，使用 Three.js CSS2DRenderer 在3D场景中渲染HTML标签。标签浮动于3D对象上方，显示标题、数值、单位和趋势箭头。适用于3D城市模型数据标注、3D地球区域指标展示、数字孪生场景数据叠加等场景。

## 目录结构

```
FloatingLabel3D/
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
labels: {
  type: Array,
  default: () => [
    { position: { x: 0, y: 2, z: 0 }, title: '主楼A', value: 1280, unit: '人', trend: 'up' },
    { position: { x: 3, y: 1.5, z: 2 }, title: '副楼B', value: 860, unit: '人', trend: 'down' },
    { position: { x: -2, y: 1, z: -1 }, title: '广场C', value: 2400, unit: 'm²', trend: 'up' },
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
  default: 14,
  desc: '标签字号（像素）',
  name: '标签字号',
  groupKey: 'style',
  groupName: '样式配置',
  sort: 2,
  min: 10,
  max: 24,
},

theme: {
  type: String,
  default: 'techBlue',
  desc: i18n.global.t('themeStyle'),
  name: i18n.global.t('themeStyle'),
  groupKey: 'style',
  groupName: '样式配置',
  sort: 3,
},
```

## 完整代码

```vue
<template>
  <div class="floating-label-3d" :class="`theme-${props.theme}`" :style="cssVars">
    <div
      v-for="(label, index) in props.labels"
      :key="index"
      class="float-label"
      :data-label-index="index"
    >
      <div class="label-connector"></div>
      <div class="label-card">
        <div class="label-title">{{ label.title }}</div>
        <div class="label-value-row">
          <span class="label-value">{{ label.value.toLocaleString() }}</span>
          <span v-if="label.unit" class="label-unit">{{ label.unit }}</span>
          <span v-if="label.trend" class="label-trend" :class="`trend-${label.trend}`">
            <template v-if="label.trend === 'up'">&#9650;</template>
            <template v-else>&#9660;</template>
          </span>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed, onMounted, onUnmounted, watch, ref } from 'vue';
import { CSS2DRenderer, CSS2DObject } from 'three/examples/jsm/renderers/CSS2DRenderer.js';
import * as THREE from 'three';
import i18n from './locale/index';

const props = defineProps({
  labels: {
    type: Array,
    default: () => [
      { position: { x: 0, y: 2, z: 0 }, title: '主楼A', value: 1280, unit: '人', trend: 'up' },
      { position: { x: 3, y: 1.5, z: 2 }, title: '副楼B', value: 860, unit: '人', trend: 'down' },
      { position: { x: -2, y: 1, z: -1 }, title: '广场C', value: 2400, unit: 'm²', trend: 'up' },
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
    default: 14,
    desc: '标签字号（像素）',
    name: '标签字号',
    groupKey: 'style',
    groupName: '样式配置',
    sort: 2,
    min: 10,
    max: 24,
  },
  theme: {
    type: String,
    default: 'techBlue',
    desc: i18n.global.t('themeStyle'),
    name: i18n.global.t('themeStyle'),
    groupKey: 'style',
    groupName: '样式配置',
    sort: 3,
  },
});

const emit = defineEmits(['label-click']);

const themeColors = {
  techBlue: {
    cardBg: 'rgba(5, 25, 55, 0.85)',
    cardBorder: 'rgba(0, 212, 255, 0.4)',
    titleColor: 'rgba(255, 255, 255, 0.7)',
    valueColor: '#00d4ff',
    unitColor: 'rgba(255, 255, 255, 0.5)',
    connectorColor: '#00d4ff',
    trendUp: '#00d4aa',
    trendDown: '#e63946',
  },
  partyRed: {
    cardBg: 'rgba(60, 10, 15, 0.85)',
    cardBorder: 'rgba(230, 57, 70, 0.4)',
    titleColor: 'rgba(255, 215, 0, 0.7)',
    valueColor: '#ffd700',
    unitColor: 'rgba(255, 215, 0, 0.5)',
    connectorColor: '#e63946',
    trendUp: '#ffd700',
    trendDown: '#ff6b81',
  },
  lightBusiness: {
    cardBg: 'rgba(255, 255, 255, 0.92)',
    cardBorder: 'rgba(74, 144, 226, 0.3)',
    titleColor: 'rgba(0, 0, 0, 0.55)',
    valueColor: '#4a90e2',
    unitColor: 'rgba(0, 0, 0, 0.4)',
    connectorColor: '#4a90e2',
    trendUp: '#52c41a',
    trendDown: '#f5222d',
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
    cardBg: 'rgba(40, 25, 5, 0.85)',
    cardBorder: 'rgba(245, 166, 35, 0.4)',
    titleColor: 'rgba(245, 166, 35, 0.7)',
    valueColor: '#f5a623',
    unitColor: 'rgba(245, 166, 35, 0.5)',
    connectorColor: '#f5a623',
    trendUp: '#00d4aa',
    trendDown: '#e63946',
  },
};

const cssVars = computed(() => {
  const colors = themeColors[props.theme] || themeColors.techBlue;
  return {
    '--fl-card-bg': colors.cardBg,
    '--fl-card-border': colors.cardBorder,
    '--fl-title-color': colors.titleColor,
    '--fl-value-color': colors.valueColor,
    '--fl-unit-color': colors.unitColor,
    '--fl-connector-color': colors.connectorColor,
    '--fl-trend-up': colors.trendUp,
    '--fl-trend-down': colors.trendDown,
    '--fl-font-size': `${props.fontSize}px`,
  };
});

// CSS2DRenderer 集成方法（供父组件调用）
const css2DLabels = ref([]);
const css2DRenderer = ref(null);

const createCSS2DObjects = (scene) => {
  // 清除旧标签
  css2DLabels.value.forEach((obj) => scene.remove(obj));
  css2DLabels.value = [];

  props.labels.forEach((label, index) => {
    const labelDiv = document.createElement('div');
    labelDiv.className = `float-label-3d-item theme-${props.theme}`;
    labelDiv.innerHTML = `
      <div class="label-connector"></div>
      <div class="label-card">
        <div class="label-title">${label.title}</div>
        <div class="label-value-row">
          <span class="label-value">${label.value.toLocaleString()}</span>
          ${label.unit ? `<span class="label-unit">${label.unit}</span>` : ''}
          ${label.trend ? `<span class="label-trend trend-${label.trend}">${label.trend === 'up' ? '&#9650;' : '&#9660;'}</span>` : ''}
        </div>
      </div>
    `;
    labelDiv.addEventListener('click', () => emit('label-click', label, index));

    const css2DObject = new CSS2DObject(labelDiv);
    css2DObject.position.set(label.position.x, label.position.y, label.position.z);
    scene.add(css2DObject);
    css2DLabels.value.push(css2DObject);
  });
};

const initCSS2DRenderer = (container, width, height) => {
  const renderer = new CSS2DRenderer();
  renderer.setSize(width, height);
  renderer.domElement.style.position = 'absolute';
  renderer.domElement.style.top = '0';
  renderer.domElement.style.pointerEvents = 'none';
  container.appendChild(renderer.domElement);
  css2DRenderer.value = renderer;
  return renderer;
};

const updateCSS2DRenderer = (scene, camera) => {
  css2DRenderer.value?.render(scene, camera);
};

const resizeCSS2DRenderer = (width, height) => {
  css2DRenderer.value?.setSize(width, height);
};

defineExpose({
  createCSS2DObjects,
  initCSS2DRenderer,
  updateCSS2DRenderer,
  resizeCSS2DRenderer,
});
</script>

<style lang="scss" scoped>
.floating-label-3d {
  display: none; // 3D场景中由CSS2DRenderer渲染，此处仅作样式模板
}

// 以下样式供 CSS2DRenderer 渲染的标签使用（需全局或通过 :deep 暴露）
:global(.float-label-3d-item) {
  display: flex;
  flex-direction: column;
  align-items: center;
  pointer-events: auto;
  cursor: pointer;
  transform: translateY(-20px);
}

:global(.float-label-3d-item .label-connector) {
  width: 1px;
  height: 16px;
  background: var(--fl-connector-color, #00d4ff);
  opacity: 0.6;
}

:global(.float-label-3d-item .label-card) {
  background: var(--fl-card-bg, rgba(5, 25, 55, 0.85));
  border: 1px solid var(--fl-card-border, rgba(0, 212, 255, 0.4));
  border-radius: 4px;
  padding: 6px 10px;
  backdrop-filter: blur(6px);
  white-space: nowrap;
}

:global(.float-label-3d-item .label-title) {
  font-size: var(--fl-font-size, 14px);
  color: var(--fl-title-color, rgba(255, 255, 255, 0.7));
  margin-bottom: 2px;
}

:global(.float-label-3d-item .label-value-row) {
  display: flex;
  align-items: baseline;
  gap: 3px;
}

:global(.float-label-3d-item .label-value) {
  font-size: calc(var(--fl-font-size, 14px) + 2px);
  font-weight: bold;
  color: var(--fl-value-color, #00d4ff);
  font-family: 'DIN', 'Orbitron', monospace;
}

:global(.float-label-3d-item .label-unit) {
  font-size: calc(var(--fl-font-size, 14px) - 2px);
  color: var(--fl-unit-color, rgba(255, 255, 255, 0.5));
}

:global(.float-label-3d-item .label-trend) {
  font-size: 10px;
  &.trend-up { color: var(--fl-trend-up, #00d4aa); }
  &.trend-down { color: var(--fl-trend-down, #e63946); }
}

// 主题变体
:global(.float-label-3d-item.theme-lightBusiness .label-card) {
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

:global(.float-label-3d-item.theme-partyRed .label-title) {
  color: rgba(255, 215, 0, 0.7);
}

:global(.float-label-3d-item.theme-ecoGreen .label-title) {
  color: rgba(245, 166, 35, 0.7);
}
</style>
```

## 主题变量支持 (theme prop)

### 主题值表

| theme 值 | 中文名 | 卡片背景 | 数值色 | 连接线色 | 适用场景 |
|-----------|--------|----------|--------|----------|----------|
| techBlue | 深蓝科技 | rgba(5,25,55,0.85) | #00d4ff | #00d4ff | 智慧乡村/社区大屏 |
| partyRed | 党建红金 | rgba(60,10,15,0.85) | #ffd700 | #e63946 | 党建大屏 |
| lightBusiness | 浅色商务 | rgba(255,255,255,0.92) | #4a90e2 | #4a90e2 | 智慧街道/浅色大屏 |
| ecoGreen | 青绿生态 | rgba(40,25,5,0.85) | #f5a623 | #f5a623 | 文旅大数据大屏 |

### Props 定义

```javascript
theme: {
  type: String,
  default: 'techBlue',
  desc: '主题风格',
  name: '主题',
  groupKey: 'style',
  groupName: '样式配置',
  sort: 3,
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
| --fl-card-bg | rgba(5,25,55,0.85) | rgba(60,10,15,0.85) | rgba(255,255,255,0.92) | rgba(40,25,5,0.85) |
| --fl-card-border | rgba(0,212,255,0.4) | rgba(230,57,70,0.4) | rgba(74,144,226,0.3) | rgba(245,166,35,0.4) |
| --fl-title-color | rgba(255,255,255,0.7) | rgba(255,215,0,0.7) | rgba(0,0,0,0.55) | rgba(245,166,35,0.7) |
| --fl-value-color | #00d4ff | #ffd700 | #4a90e2 | #f5a623 |
| --fl-unit-color | rgba(255,255,255,0.5) | rgba(255,215,0,0.5) | rgba(0,0,0,0.4) | rgba(245,166,35,0.5) |
| --fl-connector-color | #00d4ff | #e63946 | #4a90e2 | #f5a623 |
| --fl-trend-up | #00d4aa | #ffd700 | #52c41a | #00d4aa |
| --fl-trend-down | #e63946 | #ff6b81 | #f5222d | #e63946 |