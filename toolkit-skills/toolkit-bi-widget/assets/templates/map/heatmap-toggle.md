# 热力图开关模板 (HeatmapToggle)

完整参考：`references/component-templates.md` HeatmapToggle 章节

## 功能介绍

地图热力图开关组件，支持显示/隐藏热力图图层。包含开关按钮、透明度滑块和配色方案选择器。适用于智慧乡村/社区大屏中热力图图层的交互控制，如人口密度、游客分布、事件热区等场景。

## 目录结构

```
HeatmapToggle/
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
visible: {
  type: Boolean,
  default: false,
  desc: '热力图是否可见',
  name: '显示热力图',
  groupKey: 'data',
  groupName: i18n.global.t('dataConfiguration'),
  sort: 1,
},
```

### 样式配置 (groupKey: 'style', groupName: '样式配置')

```javascript
opacity: {
  type: Number,
  default: 0.6,
  desc: '热力图透明度（0-1）',
  name: '透明度',
  groupKey: 'style',
  groupName: '样式配置',
  sort: 2,
  min: 0.1,
  max: 1,
  step: 0.1,
},

colorScheme: {
  type: String,
  default: 'blue-red',
  desc: '热力图配色方案',
  name: '配色方案',
  groupKey: 'style',
  groupName: '样式配置',
  sort: 3,
  configurationTemplate: [
    { value: 'blue-red', label: '蓝-红' },
    { value: 'green-yellow', label: '绿-黄' },
    { value: 'purple-orange', label: '紫-橙' },
  ],
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
  <div class="heatmap-toggle-container" :class="`theme-${props.theme}`" :style="cssVars">
    <!-- 开关按钮 -->
    <div class="toggle-row">
      <span class="toggle-label">热力图</span>
      <button
        class="toggle-btn"
        :class="{ active: localVisible }"
        @click="toggleVisible"
      >
        <span class="toggle-dot"></span>
      </button>
    </div>

    <!-- 透明度滑块 -->
    <div v-if="localVisible" class="slider-row">
      <span class="slider-label">透明度</span>
      <input
        type="range"
        class="opacity-slider"
        :value="localOpacity"
        min="0.1"
        max="1"
        step="0.1"
        @input="handleOpacityChange"
      />
      <span class="slider-value">{{ (localOpacity * 100).toFixed(0) }}%</span>
    </div>

    <!-- 配色方案选择 -->
    <div v-if="localVisible" class="scheme-row">
      <span class="scheme-label">配色</span>
      <div class="scheme-options">
        <div
          v-for="scheme in colorSchemes"
          :key="scheme.value"
          class="scheme-item"
          :class="{ active: localColorScheme === scheme.value }"
          @click="handleSchemeChange(scheme.value)"
        >
          <div class="scheme-preview" :style="{ background: scheme.gradient }"></div>
          <span class="scheme-name">{{ scheme.label }}</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, watch } from 'vue';
import i18n from './locale/index';

const props = defineProps({
  visible: {
    type: Boolean,
    default: false,
    desc: '热力图是否可见',
    name: '显示热力图',
    groupKey: 'data',
    groupName: i18n.global.t('dataConfiguration'),
    sort: 1,
  },
  opacity: {
    type: Number,
    default: 0.6,
    desc: '热力图透明度（0-1）',
    name: '透明度',
    groupKey: 'style',
    groupName: '样式配置',
    sort: 2,
    min: 0.1,
    max: 1,
    step: 0.1,
  },
  colorScheme: {
    type: String,
    default: 'blue-red',
    desc: '热力图配色方案',
    name: '配色方案',
    groupKey: 'style',
    groupName: '样式配置',
    sort: 3,
    configurationTemplate: [
      { value: 'blue-red', label: '蓝-红' },
      { value: 'green-yellow', label: '绿-黄' },
      { value: 'purple-orange', label: '紫-橙' },
    ],
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

const emit = defineEmits(['update:visible', 'update:opacity', 'update:colorScheme', 'change']);

const localVisible = ref(props.visible);
const localOpacity = ref(props.opacity);
const localColorScheme = ref(props.colorScheme);

const themeColors = {
  techBlue: { accent: '#00d4ff', accentSoft: '#00d4ff40', bg: 'rgba(5, 25, 55, 0.85)', border: 'rgba(0, 212, 255, 0.3)' },
  partyRed: { accent: '#e63946', accentSoft: '#e6394640', bg: 'rgba(60, 10, 15, 0.85)', border: 'rgba(230, 57, 70, 0.3)' },
  lightBusiness: { accent: '#4a90e2', accentSoft: '#4a90e240', bg: 'rgba(255, 255, 255, 0.9)', border: 'rgba(74, 144, 226, 0.3)' },
  ecoGreen: { accent: '#f5a623', accentSoft: '#f5a62340', bg: 'rgba(40, 25, 5, 0.85)', border: 'rgba(245, 166, 35, 0.3)' },
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
    '--ht-accent': colors.accent,
    '--ht-accent-soft': colors.accentSoft,
    '--ht-bg': colors.bg,
    '--ht-border': colors.border,
  };
});

const colorSchemes = [
  { value: 'blue-red', label: '蓝-红', gradient: 'linear-gradient(90deg, #0000ff, #00ffff, #00ff00, #ffff00, #ff0000)' },
  { value: 'green-yellow', label: '绿-黄', gradient: 'linear-gradient(90deg, #006400, #228b22, #7cfc00, #ffd700, #ff8c00)' },
  { value: 'purple-orange', label: '紫-橙', gradient: 'linear-gradient(90deg, #4b0082, #8a2be2, #ff69b4, #ff6347, #ff8c00)' },
];

watch(() => props.visible, (val) => { localVisible.value = val; });
watch(() => props.opacity, (val) => { localOpacity.value = val; });
watch(() => props.colorScheme, (val) => { localColorScheme.value = val; });

const toggleVisible = () => {
  localVisible.value = !localVisible.value;
  emit('update:visible', localVisible.value);
  emit('change', { visible: localVisible.value, opacity: localOpacity.value, colorScheme: localColorScheme.value });
};

const handleOpacityChange = (e) => {
  localOpacity.value = parseFloat(e.target.value);
  emit('update:opacity', localOpacity.value);
  emit('change', { visible: localVisible.value, opacity: localOpacity.value, colorScheme: localColorScheme.value });
};

const handleSchemeChange = (scheme) => {
  localColorScheme.value = scheme;
  emit('update:colorScheme', scheme);
  emit('change', { visible: localVisible.value, opacity: localOpacity.value, colorScheme: scheme });
};
</script>

<style lang="scss" scoped>
.heatmap-toggle-container {
  display: flex;
  flex-direction: column;
  gap: 12px;
  padding: 12px 16px;
  background: var(--ht-bg);
  border: 1px solid var(--ht-border);
  border-radius: 6px;
  backdrop-filter: blur(8px);
}

.toggle-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.toggle-label {
  font-size: 13px;
  color: rgba(255, 255, 255, 0.8);
}

.toggle-btn {
  position: relative;
  width: 40px;
  height: 20px;
  border-radius: 10px;
  border: none;
  background: rgba(255, 255, 255, 0.15);
  cursor: pointer;
  transition: background 0.3s;
  &.active { background: var(--ht-accent); }
}

.toggle-dot {
  position: absolute;
  top: 2px;
  left: 2px;
  width: 16px;
  height: 16px;
  border-radius: 50%;
  background: #fff;
  transition: transform 0.3s;
  .toggle-btn.active & { transform: translateX(20px); }
}

.slider-row {
  display: flex;
  align-items: center;
  gap: 8px;
}

.slider-label {
  font-size: 12px;
  color: rgba(255, 255, 255, 0.6);
  white-space: nowrap;
}

.opacity-slider {
  flex: 1;
  height: 4px;
  -webkit-appearance: none;
  appearance: none;
  background: rgba(255, 255, 255, 0.15);
  border-radius: 2px;
  outline: none;
  &::-webkit-slider-thumb {
    -webkit-appearance: none;
    width: 14px;
    height: 14px;
    border-radius: 50%;
    background: var(--ht-accent);
    cursor: pointer;
    box-shadow: 0 0 6px var(--ht-accent-soft);
  }
}

.slider-value {
  font-size: 12px;
  color: var(--ht-accent);
  font-family: 'DIN', monospace;
  min-width: 36px;
  text-align: right;
}

.scheme-row {
  display: flex;
  align-items: center;
  gap: 8px;
}

.scheme-label {
  font-size: 12px;
  color: rgba(255, 255, 255, 0.6);
  white-space: nowrap;
}

.scheme-options {
  display: flex;
  gap: 8px;
}

.scheme-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 4px;
  cursor: pointer;
  padding: 4px;
  border-radius: 4px;
  border: 1px solid transparent;
  transition: border-color 0.3s;
  &.active { border-color: var(--ht-accent); }
  &:hover { border-color: var(--ht-accent-soft); }
}

.scheme-preview {
  width: 60px;
  height: 12px;
  border-radius: 2px;
}

.scheme-name {
  font-size: 10px;
  color: rgba(255, 255, 255, 0.6);
}

// 主题变体
.theme-lightBusiness {
  .toggle-label { color: rgba(0, 0, 0, 0.7); }
  .slider-label { color: rgba(0, 0, 0, 0.5); }
  .scheme-label { color: rgba(0, 0, 0, 0.5); }
  .scheme-name { color: rgba(0, 0, 0, 0.5); }
  .toggle-btn { background: rgba(0, 0, 0, 0.1); }
  .opacity-slider { background: rgba(0, 0, 0, 0.1); }
}
</style>
```

## 主题变量支持 (theme prop)

### 主题值表

| theme 值 | 中文名 | 强调色 | 背景色 | 适用场景 |
|-----------|--------|--------|--------|----------|
| techBlue | 深蓝科技 | #00d4ff | rgba(5,25,55,0.85) | 智慧乡村/社区大屏 |
| partyRed | 党建红金 | #e63946 | rgba(60,10,15,0.85) | 党建大屏 |
| lightBusiness | 浅色商务 | #4a90e2 | rgba(255,255,255,0.9) | 智慧街道/浅色大屏 |
| ecoGreen | 青绿生态 | #f5a623 | rgba(40,25,5,0.85) | 文旅大数据大屏 |

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
| --ht-accent | #00d4ff | #e63946 | #4a90e2 | #f5a623 |
| --ht-accent-soft | #00d4ff40 | #e6394640 | #4a90e240 | #f5a62340 |
| --ht-bg | rgba(5,25,55,0.85) | rgba(60,10,15,0.85) | rgba(255,255,255,0.9) | rgba(40,25,5,0.85) |
| --ht-border | rgba(0,212,255,0.3) | rgba(230,57,70,0.3) | rgba(74,144,226,0.3) | rgba(245,166,35,0.3) |