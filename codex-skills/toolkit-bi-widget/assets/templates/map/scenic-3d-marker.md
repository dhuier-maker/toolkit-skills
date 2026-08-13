# 3D景区标记模板 (Scenic3DMarker)

完整参考：`references/component-templates.md` Scenic3DMarker 章节

## 功能介绍

地图上的3D景区标记组件，支持多点标记显示。每个标记包含图标、名称、脉冲动画效果，点击可弹出详情面板。适用于文旅大屏景区分布展示、智慧乡村景点标注等场景。

## 目录结构

```
Scenic3DMarker/
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
markers: {
  type: Array,
  default: () => [
    { lng: 119.55, lat: 26.67, name: '湄洲岛', icon: 'scenic', type: 'scenic', value: 12500 },
    { lng: 119.02, lat: 25.50, name: '九鲤湖', icon: 'water', type: 'natural', value: 8500 },
    { lng: 118.90, lat: 25.30, name: '广化寺', icon: 'temple', type: 'cultural', value: 6200 },
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
showPulse: {
  type: Boolean,
  default: true,
  desc: '是否显示脉冲动画',
  name: '脉冲动画',
  groupKey: 'style',
  groupName: '样式配置',
  sort: 2,
},

popupWidth: {
  type: Number,
  default: 300,
  desc: '详情弹窗宽度（像素）',
  name: '弹窗宽度',
  groupKey: 'style',
  groupName: '样式配置',
  sort: 3,
  min: 200,
  max: 600,
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
  <div class="scenic-3d-marker-container" :class="`theme-${props.theme}`" :style="cssVars">
    <div
      v-for="(marker, index) in props.markers"
      :key="index"
      class="marker-item"
      @click="handleMarkerClick(marker)"
    >
      <!-- 3D 标记模型 -->
      <div class="marker-model" :class="`model-${marker.type || 'scenic'}`">
        <!-- 圆柱底座 -->
        <div class="cylinder-base"></div>
        <!-- 锥形/地标主体 -->
        <div class="cone-body"></div>
        <!-- 顶部光点 -->
        <div class="top-dot"></div>
      </div>
      <!-- 脉冲发光环 -->
      <div v-if="props.showPulse" class="glow-ring"></div>
      <!-- 名称标签 -->
      <div class="name-label">{{ marker.name }}</div>
      <!-- 数值标签 -->
      <div v-if="marker.value" class="value-label">{{ marker.value.toLocaleString() }}</div>
    </div>

    <!-- 详情弹窗 -->
    <div v-if="activeMarker" class="detail-popup" :style="{ width: props.popupWidth + 'px' }">
      <div class="popup-header">
        <span class="popup-title">{{ activeMarker.name }}</span>
        <span class="popup-close" @click="activeMarker = null">&times;</span>
      </div>
      <div class="popup-body">
        <div class="popup-type">{{ getTypeLabel(activeMarker.type) }}</div>
        <div v-if="activeMarker.value" class="popup-value">
          <span class="popup-number">{{ activeMarker.value.toLocaleString() }}</span>
          <span class="popup-unit">人次</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue';
import i18n from './locale/index';

const props = defineProps({
  markers: {
    type: Array,
    default: () => [
      { lng: 119.55, lat: 26.67, name: '湄洲岛', icon: 'scenic', type: 'scenic', value: 12500 },
      { lng: 119.02, lat: 25.50, name: '九鲤湖', icon: 'water', type: 'natural', value: 8500 },
      { lng: 118.90, lat: 25.30, name: '广化寺', icon: 'temple', type: 'cultural', value: 6200 },
    ],
    desc: i18n.global.t('dataSpecification'),
    name: i18n.global.t('displayContent'),
    groupKey: 'data',
    groupName: i18n.global.t('dataConfiguration'),
    useDynamic: true,
    sort: 1,
  },
  showPulse: {
    type: Boolean,
    default: true,
    desc: '是否显示脉冲动画',
    name: '脉冲动画',
    groupKey: 'style',
    groupName: '样式配置',
    sort: 2,
  },
  popupWidth: {
    type: Number,
    default: 300,
    desc: '详情弹窗宽度（像素）',
    name: '弹窗宽度',
    groupKey: 'style',
    groupName: '样式配置',
    sort: 3,
    min: 200,
    max: 600,
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

const emit = defineEmits(['marker-click']);

const activeMarker = ref(null);

const cssVars = computed(() => {
  const themeColors = {
    techBlue: { primary: '#00D4FF', glow: '#00D4FF80', glowSoft: '#00D4FF30' },
    ecoGreen: { primary: '#00E5C3', glow: '#00E5C380', glowSoft: '#00E5C330' },
    partyRed: { primary: '#FF4D4F', glow: '#FF4D4F80', glowSoft: '#FF4D4F30' },
    warmOrange: { primary: '#FF8C42', glow: '#FF8C4280', glowSoft: '#FF8C4230' },
    deepPurple: { primary: '#A855F7', glow: '#A855F780', glowSoft: '#A855F730' },
    lightBusiness: { primary: '#1890FF', glow: '#1890FF80', glowSoft: '#1890FF30' },
  };
  const colors = themeColors[props.theme] || themeColors.techBlue;
  return {
    '--marker-color': colors.primary,
    '--marker-glow': colors.glow,
    '--marker-glow-soft': colors.glowSoft,
  };
});

const typeLabels = {
  scenic: '景区',
  natural: '自然景观',
  cultural: '文化古迹',
  hotel: '酒店',
  restaurant: '餐饮',
};

const getTypeLabel = (type) => typeLabels[type] || '景点';

const handleMarkerClick = (marker) => {
  activeMarker.value = marker;
  emit('marker-click', marker);
};
</script>

<style lang="scss" scoped>
.scenic-3d-marker-container {
  position: relative;
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.marker-item {
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
  cursor: pointer;
  transition: transform 0.3s;
  &:hover { transform: scale(1.1); }
}

.marker-model {
  position: relative;
  width: 24px;
  height: 48px;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.cylinder-base {
  width: 20px;
  height: 8px;
  background: var(--marker-color);
  border-radius: 50%;
  opacity: 0.9;
}

.cone-body {
  width: 0;
  height: 0;
  border-left: 10px solid transparent;
  border-right: 10px solid transparent;
  border-bottom: 32px solid var(--marker-color);
  filter: drop-shadow(0 0 6px var(--marker-glow));
}

.top-dot {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: #fff;
  box-shadow: 0 0 8px var(--marker-color), 0 0 16px var(--marker-glow);
  margin-top: -38px;
}

.glow-ring {
  width: 36px;
  height: 12px;
  border-radius: 50%;
  background: var(--marker-glow-soft);
  box-shadow: 0 0 12px var(--marker-glow), 0 0 24px var(--marker-glow-soft);
  animation: pulse-ring 2s ease-in-out infinite;
  margin-top: -4px;
}

.name-label {
  margin-top: 4px;
  font-size: 12px;
  color: #fff;
  text-shadow: 0 0 6px rgba(0, 0, 0, 0.8);
  white-space: nowrap;
}

.value-label {
  font-size: 14px;
  font-weight: bold;
  color: var(--marker-color);
  font-family: 'DIN', 'Orbitron', monospace;
}

.detail-popup {
  position: absolute;
  top: 0;
  left: 40px;
  background: rgba(5, 25, 55, 0.9);
  border: 1px solid var(--marker-color);
  border-radius: 4px;
  z-index: 100;
  backdrop-filter: blur(8px);
  box-shadow: 0 0 20px var(--marker-glow);
}

.popup-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 10px 14px;
  border-bottom: 1px solid rgba(0, 168, 232, 0.3);
}

.popup-title {
  font-size: 14px;
  font-weight: 500;
  color: #fff;
}

.popup-close {
  font-size: 18px;
  color: rgba(255, 255, 255, 0.6);
  cursor: pointer;
  &:hover { color: #fff; }
}

.popup-body {
  padding: 12px 14px;
}

.popup-type {
  font-size: 12px;
  color: rgba(255, 255, 255, 0.6);
  margin-bottom: 8px;
}

.popup-value {
  display: flex;
  align-items: baseline;
  gap: 4px;
}

.popup-number {
  font-size: 24px;
  font-weight: bold;
  color: var(--marker-color);
  font-family: 'DIN', 'Orbitron', monospace;
}

.popup-unit {
  font-size: 12px;
  color: rgba(255, 255, 255, 0.6);
}

@keyframes pulse-ring {
  0%, 100% { transform: scale(1); opacity: 0.6; }
  50% { transform: scale(1.4); opacity: 0.2; }
}

// 主题变体
.theme-partyRed {
  .name-label { color: #FFD700; }
  .popup-header { border-bottom-color: rgba(255, 77, 79, 0.3); }
}

.theme-warmOrange {
  .name-label { color: #FFB347; }
  .popup-header { border-bottom-color: rgba(255, 140, 66, 0.3); }
}

.theme-deepPurple {
  .name-label { color: #C084FC; }
  .popup-header { border-bottom-color: rgba(168, 85, 247, 0.3); }
}

.theme-lightBusiness {
  .name-label { color: #333; text-shadow: none; }
  .detail-popup {
    background: rgba(255, 255, 255, 0.95);
    box-shadow: 0 2px 12px rgba(0, 0, 0, 0.15);
  }
  .popup-title { color: #333; }
  .popup-type { color: rgba(0, 0, 0, 0.5); }
  .popup-unit { color: rgba(0, 0, 0, 0.5); }
  .popup-close { color: rgba(0, 0, 0, 0.4); }
}

.theme-ecoGreen {
  .name-label { color: #00E5C3; }
}
</style>
```

## 主题变量支持 (theme prop)

### 主题值表

| theme 值 | 中文名 | 主色 | 发光色 | 适用场景 |
|-----------|--------|------|--------|----------|
| techBlue | 深蓝科技 | #00D4FF | #00D4FF80 | 智慧乡村/社区大屏 |
| ecoGreen | 青绿生态 | #00E5C3 | #00E5C380 | 生态/文旅大屏 |
| partyRed | 党建红金 | #FF4D4F | #FF4D4F80 | 党建大屏 |
| warmOrange | 暖橙数据 | #FF8C42 | #FF8C4280 | 暖色数据大屏 |
| deepPurple | 紫蓝深邃 | #A855F7 | #A855F780 | 紫蓝科技大屏 |
| lightBusiness | 浅色商务 | #1890FF | #1890FF80 | 智慧街道/浅色大屏 |

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
| --marker-color | #00D4FF | #00E5C3 | #FF4D4F | #FF8C42 | #A855F7 | #1890FF |
| --marker-glow | #00D4FF80 | #00E5C380 | #FF4D4F80 | #FF8C4280 | #A855F780 | #1890FF80 |
| --marker-glow-soft | #00D4FF30 | #00E5C330 | #FF4D4F30 | #FF8C4230 | #A855F730 | #1890FF30 |