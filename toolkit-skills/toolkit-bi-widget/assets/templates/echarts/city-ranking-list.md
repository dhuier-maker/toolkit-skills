# 城市排名列表模板 (CityRankingList)

完整参考：`references/component-templates.md` CityRankingList 章节

## 功能介绍

带标签切换（省内/省外）和横向进度条的城市排名列表组件，前三名使用金银铜色标识，适配 techBlue/ecoGreen/partyRed/warmOrange/deepPurple/lightBusiness 六套主题。

## 目录结构

```
CityRankingList/
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
provinceData: {
  type: Array,
  default: () => [
    { name: '福州', value: 62398 },
    { name: '厦门', value: 56535 },
    { name: '泉州', value: 50121 },
    { name: '漳州', value: 43210 },
    { name: '莆田', value: 38765 },
  ],
  desc: '省内排名数据',
  name: '省内数据',
  groupKey: 'data',
  groupName: i18n.global.t('dataConfiguration'),
  useDynamic: true,
  sort: 1,
},

outsideData: {
  type: Array,
  default: () => [
    { name: '上海', value: 82398 },
    { name: '广东', value: 76535 },
    { name: '浙江', value: 60121 },
    { name: '江苏', value: 53210 },
    { name: '北京', value: 48765 },
  ],
  desc: '省外排名数据',
  name: '省外数据',
  groupKey: 'data',
  groupName: i18n.global.t('dataConfiguration'),
  useDynamic: true,
  sort: 2,
},

tabs: {
  type: Array,
  default: () => [
    { label: '省内', value: 'province' },
    { label: '省外', value: 'outside' },
  ],
  desc: '标签切换选项',
  name: '标签选项',
  groupKey: 'data',
  groupName: i18n.global.t('dataConfiguration'),
  sort: 3,
},
```

### 样式配置 (groupKey: 'style', groupName: '样式配置')

```javascript
progressColor: {
  type: String,
  default: '#00a8e8',
  desc: '进度条颜色',
  name: '进度条颜色',
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
},
```

## 完整代码

```vue
<template>
  <div class="city-ranking-list" :class="`theme-${props.theme}`">
    <!-- 标签切换 -->
    <div v-if="props.tabs.length > 0" class="tab-header">
      <span
        v-for="tab in props.tabs"
        :key="tab.value"
        class="tab-item"
        :class="{ active: activeTab === tab.value }"
        @click="activeTab = tab.value"
      >{{ tab.label }}</span>
    </div>

    <!-- 排名列表 -->
    <div class="ranking-list">
      <div v-for="(item, index) in listData" :key="item.name" class="ranking-item">
        <div class="item-header">
          <span class="rank-number" :class="rankClass(index)">{{ index + 1 }}</span>
          <span class="city-name">{{ item.name }}</span>
          <span class="city-value">{{ item.value.toLocaleString() }}</span>
        </div>
        <div class="progress-bar">
          <div class="progress-fill" :style="{ width: `${item.percent}%`, background: progressGradient }"></div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue';
import i18n from './locale/index';

const props = defineProps({
  provinceData: {
    type: Array,
    default: () => [
      { name: '福州', value: 62398 },
      { name: '厦门', value: 56535 },
      { name: '泉州', value: 50121 },
      { name: '漳州', value: 43210 },
      { name: '莆田', value: 38765 },
    ],
    desc: '省内排名数据',
    name: '省内数据',
    groupKey: 'data',
    groupName: i18n.global.t('dataConfiguration'),
    useDynamic: true,
    sort: 1,
  },
  outsideData: {
    type: Array,
    default: () => [
      { name: '上海', value: 82398 },
      { name: '广东', value: 76535 },
      { name: '浙江', value: 60121 },
      { name: '江苏', value: 53210 },
      { name: '北京', value: 48765 },
    ],
    desc: '省外排名数据',
    name: '省外数据',
    groupKey: 'data',
    groupName: i18n.global.t('dataConfiguration'),
    useDynamic: true,
    sort: 2,
  },
  tabs: {
    type: Array,
    default: () => [
      { label: '省内', value: 'province' },
      { label: '省外', value: 'outside' },
    ],
    desc: '标签切换选项',
    name: '标签选项',
    groupKey: 'data',
    groupName: i18n.global.t('dataConfiguration'),
    sort: 3,
  },
  progressColor: {
    type: String,
    default: '#00a8e8',
    desc: '进度条颜色',
    name: '进度条颜色',
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
  },
});

const activeTab = ref(props.tabs[0]?.value || 'province');

const currentData = computed(() => {
  return activeTab.value === 'province' ? props.provinceData : props.outsideData;
});

const listData = computed(() => {
  const data = currentData.value;
  const maxValue = Math.max(...data.map((item) => item.value), 1);
  return data.map((item) => ({
    ...item,
    percent: (item.value / maxValue) * 100,
  }));
});

const rankClass = (index) => {
  if (index === 0) return 'rank-gold';
  if (index === 1) return 'rank-silver';
  if (index === 2) return 'rank-bronze';
  return '';
};

const progressGradient = computed(() => {
  const c = props.progressColor;
  return `linear-gradient(90deg, ${c}cc, ${c})`;
});
</script>

<style lang="scss" scoped>
.city-ranking-list {
  width: 100%;
  height: 100%;
  padding: 12px;
  overflow: hidden;
}

.tab-header {
  display: flex;
  gap: 12px;
  margin-bottom: 12px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
  padding-bottom: 8px;
}

.tab-item {
  font-size: 13px;
  color: rgba(255, 255, 255, 0.5);
  cursor: pointer;
  padding: 2px 8px;
  transition: all 0.3s;
  &.active {
    color: #00a8e8;
    border-bottom: 2px solid #00a8e8;
  }
}

.ranking-item {
  margin-bottom: 10px;
}

.item-header {
  display: flex;
  align-items: center;
  margin-bottom: 4px;
}

.rank-number {
  width: 20px;
  height: 20px;
  border-radius: 4px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 12px;
  font-weight: bold;
  color: rgba(255, 255, 255, 0.5);
  background: rgba(255, 255, 255, 0.05);
  margin-right: 8px;
  &.rank-gold { color: #ffd700; background: rgba(255, 215, 0, 0.15); }
  &.rank-silver { color: #c0c0c0; background: rgba(192, 192, 192, 0.15); }
  &.rank-bronze { color: #cd7f32; background: rgba(205, 127, 50, 0.15); }
}

.city-name {
  flex: 1;
  font-size: 13px;
  color: rgba(255, 255, 255, 0.85);
}

.city-value {
  font-size: 13px;
  font-weight: bold;
  color: #fff;
  font-family: 'DIN', monospace;
}

.progress-bar {
  height: 6px;
  background: rgba(255, 255, 255, 0.06);
  border-radius: 3px;
  overflow: hidden;
}

.progress-fill {
  height: 100%;
  border-radius: 3px;
  transition: width 0.6s ease;
}

.theme-partyRed {
  .tab-item.active { color: #FF4D4F; border-bottom-color: #FF4D4F; }
  .rank-gold { color: #FFD700; }
  .city-value { color: #FFD700; }
}

.theme-ecoGreen {
  .tab-item.active { color: #00E5C3; border-bottom-color: #00E5C3; }
  .city-value { color: #00E5C3; }
}

.theme-warmOrange {
  .tab-item.active { color: #FF8C42; border-bottom-color: #FF8C42; }
  .rank-gold { color: #FFB347; }
  .city-value { color: #FFB347; }
}

.theme-deepPurple {
  .tab-item.active { color: #A855F7; border-bottom-color: #A855F7; }
  .city-value { color: #C084FC; }
}

.theme-lightBusiness {
  .tab-item { color: rgba(0, 0, 0, 0.4); &.active { color: #1890FF; border-bottom-color: #1890FF; } }
  .city-name { color: rgba(0, 0, 0, 0.75); }
  .city-value { color: #1890FF; }
  .progress-bar { background: rgba(0, 0, 0, 0.06); }
  .rank-number { color: rgba(0, 0, 0, 0.4); background: rgba(0, 0, 0, 0.04); }
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



### Theme CSS Variable Mapping


