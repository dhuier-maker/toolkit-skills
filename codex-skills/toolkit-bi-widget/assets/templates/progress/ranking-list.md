# 排名列表模板 (CityRankingList)

完整参考：`references/component-templates.md` CityRankingList 章节

## 功能介绍

带横向进度条的城市排名列表组件，支持标签切换、自动计算进度百分比。适用于客流来源排名、数据排名等场景。

## Props 定义

### 数据配置 (groupKey: 'data')

```javascript
data: {
  type: Array,
  default: () => [
    { name: '上海', value: 62398 },
    { name: '重庆', value: 56535 },
    { name: '广东', value: 50121 },
  ],
  desc: '排名数据数组',
  name: '数据',
  groupKey: 'data',
  groupName: '数据配置',
  sort: 1,
},

tabs: {
  type: Array,
  default: () => [
    { label: '省内', value: 'in' },
    { label: '省外', value: 'out' },
  ],
  desc: '标签切换选项',
  name: '标签',
  groupKey: 'data',
  groupName: '数据配置',
  sort: 2,
},

defaultTab: {
  type: String,
  default: 'out',
  desc: '默认选中标签',
  name: '默认标签',
  groupKey: 'data',
  groupName: '数据配置',
  sort: 3,
},
};
```

## 核心逻辑

```javascript
const listData = computed(() => {
  const maxValue = Math.max(...props.data.map(item => item.value));
  return props.data.map(item => ({
    ...item,
    percent: (item.value / maxValue) * 100,
  }));
});
```

## 模板结构

```html
<div class="city-ranking-list">
  <!-- 顶部标签切换 -->
  <div v-if="tabs.length > 0" class="tab-header">
    <span v-for="tab in tabs" :key="tab.value" class="tab-item"
      :class="{ active: activeTab === tab.value }"
      @click="activeTab = tab.value">
      {{ tab.label }}
    </span>
  </div>

  <!-- 排名列表 -->
  <div class="ranking-list">
    <div v-for="(item, index) in listData" :key="item.name" class="ranking-item">
      <div class="item-header">
        <span class="rank-number" :class="`rank-${index + 1}`">{{ index + 1 }}</span>
        <span class="city-name">{{ item.name }}</span>
        <span class="city-value">{{ item.value.toLocaleString() }}</span>
      </div>
      <div class="progress-bar">
        <div class="progress-fill" :style="{ width: `${item.percent}%` }"></div>
      </div>
    </div>
  </div>
</div>
```

## 完整代码

完整代码请参考 `references/component-templates.md` 中 CityRankingList 章节。
