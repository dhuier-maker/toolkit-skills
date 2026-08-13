# 性别比例图模板 (GenderRatioChart)

完整参考：`references/component-templates.md` GenderRatioChart 章节

## 功能介绍

性别比例展示组件，使用简化 SVG 火柴人图标表示男女比例，男性蓝色（#2196f3），女性橙色（#ff9800），显示总人数及底部百分比条，适配 techBlue/ecoGreen/partyRed/warmOrange/deepPurple/lightBusiness 六套主题。

## 目录结构

```
GenderRatioChart/
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
maleCount: {
  type: Number,
  default: 0,
  desc: i18n.global.t('maleCount'),
  name: i18n.global.t('maleCount'),
  groupKey: 'data',
  groupName: i18n.global.t('dataConfiguration'),
  useDynamic: true,
  sort: 1,
},

femaleCount: {
  type: Number,
  default: 0,
  desc: i18n.global.t('femaleCount'),
  name: i18n.global.t('femaleCount'),
  groupKey: 'data',
  groupName: i18n.global.t('dataConfiguration'),
  useDynamic: true,
  sort: 2,
},
```

### 样式配置 (groupKey: 'style', groupName: '样式配置')

```javascript
showPercentage: {
  type: Boolean,
  default: true,
  desc: '是否显示百分比条',
  name: '显示百分比',
  groupKey: 'style',
  groupName: '样式配置',
  sort: 1,
},

theme: {
  type: String,
  default: 'techBlue',
  desc: i18n.global.t('themeStyle'),
  name: i18n.global.t('themeStyle'),
  groupKey: 'style',
  groupName: '样式配置',
  sort: 2,
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

## 完整代码

```vue
<template>
  <div class="gender-ratio-chart" :class="`theme-${props.theme}`">
    <!-- 男性区域 -->
    <div class="gender-section male">
      <div class="icon-row">
        <svg v-for="i in maleIcons" :key="'m'+i" class="person-icon male-icon" viewBox="0 0 20 40">
          <circle cx="10" cy="6" r="4" fill="#2196f3"/>
          <line x1="10" y1="10" x2="10" y2="26" stroke="#2196f3" stroke-width="2"/>
          <line x1="4" y1="18" x2="16" y2="18" stroke="#2196f3" stroke-width="2"/>
          <line x1="10" y1="26" x2="5" y2="36" stroke="#2196f3" stroke-width="2"/>
          <line x1="10" y1="26" x2="15" y2="36" stroke="#2196f3" stroke-width="2"/>
        </svg>
      </div>
      <div class="gender-count">{{ props.maleCount }}</div>
      <div class="gender-label">{{ i18n.global.t('male') }}</div>
    </div>

    <!-- 总人数 -->
    <div class="total-section">
      <div class="total-value">{{ totalCount }}</div>
      <div class="total-label">{{ i18n.global.t('totalPeople') }}</div>
    </div>

    <!-- 女性区域 -->
    <div class="gender-section female">
      <div class="icon-row">
        <svg v-for="i in femaleIcons" :key="'f'+i" class="person-icon female-icon" viewBox="0 0 20 40">
          <circle cx="10" cy="6" r="4" fill="#ff9800"/>
          <line x1="10" y1="10" x2="10" y2="26" stroke="#ff9800" stroke-width="2"/>
          <line x1="4" y1="18" x2="16" y2="18" stroke="#ff9800" stroke-width="2"/>
          <line x1="10" y1="26" x2="5" y2="36" stroke="#ff9800" stroke-width="2"/>
          <line x1="10" y1="26" x2="15" y2="36" stroke="#ff9800" stroke-width="2"/>
        </svg>
      </div>
      <div class="gender-count">{{ props.femaleCount }}</div>
      <div class="gender-label">{{ i18n.global.t('female') }}</div>
    </div>

    <!-- 百分比条 -->
    <div v-if="props.showPercentage && totalCount > 0" class="percentage-bar">
      <div class="male-fill" :style="{ width: malePercent + '%' }"></div>
      <div class="female-fill" :style="{ width: femalePercent + '%' }"></div>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue';
import i18n from './locale/index';

const props = defineProps({
  maleCount: {
    type: Number,
    default: 0,
    desc: i18n.global.t('maleCount'),
    name: i18n.global.t('maleCount'),
    groupKey: 'data',
    groupName: i18n.global.t('dataConfiguration'),
    useDynamic: true,
    sort: 1,
  },
  femaleCount: {
    type: Number,
    default: 0,
    desc: i18n.global.t('femaleCount'),
    name: i18n.global.t('femaleCount'),
    groupKey: 'data',
    groupName: i18n.global.t('dataConfiguration'),
    useDynamic: true,
    sort: 2,
  },
  showPercentage: {
    type: Boolean,
    default: true,
    desc: '是否显示百分比条',
    name: '显示百分比',
    groupKey: 'style',
    groupName: '样式配置',
    sort: 1,
  },
  theme: {
    type: String,
    default: 'techBlue',
    desc: i18n.global.t('themeStyle'),
    name: i18n.global.t('themeStyle'),
    groupKey: 'style',
    groupName: '样式配置',
    sort: 2,
    configurationTemplate: [
      { value: 'techBlue', label: '深蓝科技' },
      { value: 'ecoGreen', label: '青绿生态' },
      { value: 'partyRed', label: '党建红金' },
      { value: 'warmOrange', label: '暖橙数据' },
      { value: 'deepPurple', label: '紫蓝深邃' },
      { value: 'lightBusiness', label: '浅色商务' },
    ],
  },
});

const totalCount = computed(() => props.maleCount + props.femaleCount);

const malePercent = computed(() => {
  if (totalCount.value === 0) return 50;
  return (props.maleCount / totalCount.value) * 100;
});

const femalePercent = computed(() => 100 - malePercent.value);

const maxIcons = 5;
const maleIcons = computed(() => Math.min(Math.round(malePercent.value / 20), maxIcons) || 1);
const femaleIcons = computed(() => Math.min(Math.round(femalePercent.value / 20), maxIcons) || 1);
</script>

<style lang="scss" scoped>
.gender-ratio-chart {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 24px;
  width: 100%;
  height: 100%;
  padding: 12px;
}

.gender-section {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 4px;
}

.icon-row {
  display: flex;
  gap: 2px;
}

.person-icon {
  width: 16px;
  height: 32px;
}

.gender-count {
  font-size: 22px;
  font-weight: bold;
  font-family: 'DIN', monospace;
}

.male .gender-count { color: #2196f3; }
.female .gender-count { color: #ff9800; }

.gender-label {
  font-size: 12px;
  color: rgba(255, 255, 255, 0.6);
}

.total-section {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 0 8px;
}

.total-value {
  font-size: 28px;
  font-weight: bold;
  color: #fff;
  font-family: 'DIN', monospace;
}

.total-label {
  font-size: 12px;
  color: rgba(255, 255, 255, 0.5);
}

.percentage-bar {
  position: absolute;
  bottom: 8px;
  left: 12px;
  right: 12px;
  height: 6px;
  border-radius: 3px;
  overflow: hidden;
  display: flex;
}

.male-fill {
  height: 100%;
  background: #2196f3;
  transition: width 0.6s ease;
}

.female-fill {
  height: 100%;
  background: #ff9800;
  transition: width 0.6s ease;
}

.theme-ecoGreen {
  .male .gender-count { color: #2196f3; }
  .female .gender-count { color: #ff9800; }
  .total-value { color: #00E5C3; }
}

.theme-partyRed {
  .male .gender-count { color: #2196f3; }
  .female .gender-count { color: #e63946; }
  .total-value { color: #FFD700; }
}

.theme-warmOrange {
  .male .gender-count { color: #2196f3; }
  .female .gender-count { color: #ff9800; }
  .total-value { color: #FFB347; }
}

.theme-deepPurple {
  .male .gender-count { color: #2196f3; }
  .female .gender-count { color: #ff9800; }
  .total-value { color: #C084FC; }
}

.theme-lightBusiness {
  .gender-label { color: rgba(0, 0, 0, 0.5); }
  .total-label { color: rgba(0, 0, 0, 0.4); }
  .total-value { color: #333; }
}
</style>
```


## 主题变量支持 (theme prop)

### 主题值

| 主题 | panelBg | borderColor | borderGlow | textPrimary | textSecondary | accentColor | headerBg | dotColor |
|------|---------|-------------|------------|-------------|---------------|-------------|----------|----------|
| techBlue | rgba(13,25,41,0.85) | rgba(0,212,255,0.18) | rgba(0,212,255,0.4) | #ffffff | rgba(255,255,255,0.7) | #00D4FF | rgba(0,212,255,0.08) | rgba(0,212,255,0.3) |
| ecoGreen | rgba(10,30,50,0.85) | rgba(0,229,195,0.18) | rgba(0,229,195,0.4) | #ffffff | rgba(255,255,255,0.7) | #00E5C3 | rgba(0,229,195,0.08) | rgba(0,229,195,0.3) |
| partyRed | rgba(30,10,10,0.85) | rgba(255,77,79,0.18) | rgba(255,77,79,0.4) | #ffffff | rgba(255,255,255,0.7) | #FF4D4F | rgba(255,77,79,0.08) | rgba(255,77,79,0.3) |
| warmOrange | rgba(26,18,16,0.85) | rgba(255,140,66,0.18) | rgba(255,140,66,0.4) | #ffffff | rgba(255,255,255,0.7) | #FF8C42 | rgba(255,140,66,0.08) | rgba(255,140,66,0.3) |
| deepPurple | rgba(14,10,32,0.85) | rgba(168,85,247,0.18) | rgba(168,85,247,0.4) | #ffffff | rgba(255,255,255,0.7) | #A855F7 | rgba(168,85,247,0.08) | rgba(168,85,247,0.3) |
| lightBusiness | rgba(255,255,255,0.92) | rgba(0,100,200,0.12) | rgba(0,100,200,0.2) | #333333 | rgba(0,0,0,0.5) | #1890FF | rgba(0,100,200,0.06) | rgba(0,100,200,0.2) |

### Theme Props Definition

```javascript
theme: {
  type: String,
  default: 'techBlue',
  desc: '主题风格',
  name: '主题',
  groupKey: 'style',
  groupName: '样式配置',
  sort: 2,
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

### Theme CSS Variable Mapping

| CSS 变量 | techBlue | ecoGreen | partyRed | warmOrange | deepPurple | lightBusiness |
|----------|----------|----------|----------|------------|------------|---------------|
| --male-color | #2196f3 | #2196f3 | #2196f3 | #2196f3 | #2196f3 | #2196f3 |
| --female-color | #ff9800 | #ff9800 | #e63946 | #ff9800 | #ff9800 | #ff9800 |
| --total-color | #00D4FF | #00E5C3 | #FFD700 | #FFB347 | #C084FC | #333 |
| --label-color | rgba(255,255,255,0.6) | rgba(255,255,255,0.6) | rgba(255,255,255,0.6) | rgba(255,255,255,0.6) | rgba(255,255,255,0.6) | rgba(0,0,0,0.5) |

