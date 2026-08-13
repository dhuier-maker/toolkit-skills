# 底部导航标签模板 (BottomNavTabs)

完整参考：`references/component-templates.md` BottomNavTabs 章节

## 功能介绍

底部导航标签组件，提供胶囊样式（capsule）和图标+文字（icon-text）两种模式。胶囊模式下标签呈圆角胶囊形状，选中项带发光高亮效果；图标+文字模式下标签垂直排列图标和文字。适用于大屏底部区域的功能切换、模块导航等场景。

## 使用场景

- 大屏底部功能模块切换
- 数据视图切换（如：实时/历史/对比）
- 多维度数据展示的 Tab 导航

## Props 定义

### 基础配置 (groupKey: 'basic', groupName: '基础配置')

```javascript
tabs: {
  type: Array,
  default: () => [],
  desc: '标签列表，每项包含 key/label/icon 字段',
  name: i18n.global.t('displayContent'),
  groupKey: 'basic',
  groupName: '基础配置',
  sort: 1,
  useDynamic: true,
  childConfig: [
    { field: 'key', label: '唯一标识', type: 'String' },
    { field: 'label', label: '显示文字', type: 'String' },
    { field: 'icon', label: '图标名称（可选）', type: 'String' },
  ],
},
activeTab: {
  type: String,
  default: '',
  desc: '当前激活的标签 key，为空时默认激活第一个',
  name: i18n.global.t('activeTab'),
  groupKey: 'basic',
  groupName: '基础配置',
  sort: 2,
},
```

### 样式配置 (groupKey: 'style', groupName: '样式配置')

```javascript
mode: {
  type: String,
  default: 'capsule',
  desc: i18n.global.t('displayMode'),
  name: i18n.global.t('displayMode'),
  groupKey: 'style',
  groupName: '样式配置',
  sort: 1,
  configurationTemplate: [
    { value: 'capsule', label: '胶囊样式' },
    { value: 'icon-text', label: '图标文字' },
  ],
},
theme: {
  type: String,
  default: 'techBlue',
  desc: '主题风格：techBlue-深蓝科技/partyRed-党建红金/lightBusiness-浅色商务',
  name: i18n.global.t('themeStyle'),
  groupKey: 'style',
  groupName: '样式配置',
  sort: 2,
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

## emit 事件

- `update:activeTab` - 切换标签时触发（支持 v-model:activeTab）
- `change` - 切换标签时触发，参数: `{ key, label, index }`

## 完整代码

```vue
<template>
  <div class="bottom-nav-tabs" :class="[`theme-${theme}`, `mode-${mode}`]">
    <div class="tabs-container">
      <div
        v-for="(tab, index) in tabs"
        :key="tab.key"
        class="tab-item"
        :class="{ active: currentTab === tab.key }"
        @click="handleTabClick(tab, index)"
      >
        <!-- 胶囊模式 -->
        <template v-if="mode === 'capsule'">
          <span class="tab-label">{{ tab.label }}</span>
          <span class="tab-glow"></span>
        </template>

        <!-- 图标+文字模式 -->
        <template v-else>
          <span v-if="tab.icon" class="tab-icon">
            <svg class="icon-svg" aria-hidden="true">
              <use :xlink:href="`#${tab.icon}`" />
            </svg>
          </span>
          <span class="tab-label">{{ tab.label }}</span>
        </template>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  tabs: {
    type: Array,
    default: () => [],
    desc: '标签列表，每项包含 key/label/icon 字段',
    name: i18n.global.t('displayContent'),
    groupKey: 'basic',
    groupName: '基础配置',
    sort: 1,
    useDynamic: true,
    childConfig: [
      { field: 'key', label: '唯一标识', type: 'String' },
      { field: 'label', label: '显示文字', type: 'String' },
      { field: 'icon', label: '图标名称（可选）', type: 'String' },
    ],
  },
  activeTab: {
    type: String,
    default: '',
    desc: '当前激活的标签 key，为空时默认激活第一个',
    name: i18n.global.t('activeTab'),
    groupKey: 'basic',
    groupName: '基础配置',
    sort: 2,
  },
  mode: {
    type: String,
    default: 'capsule',
    desc: i18n.global.t('displayMode'),
    name: i18n.global.t('displayMode'),
    groupKey: 'style',
    groupName: '样式配置',
    sort: 1,
    configurationTemplate: [
      { value: 'capsule', label: '胶囊样式' },
      { value: 'icon-text', label: '图标文字' },
    ],
  },
  theme: {
    type: String,
    default: 'techBlue',
    desc: '主题风格：techBlue-深蓝科技/partyRed-党建红金/lightBusiness-浅色商务',
    name: i18n.global.t('themeStyle'),
    groupKey: 'style',
    groupName: '样式配置',
    sort: 2,
    configurationTemplate: [
      { value: 'techBlue', label: '深蓝科技' },
      { value: 'partyRed', label: '党建红金' },
    { value: 'warmOrange', label: '暖橙数据' },
      { value: 'lightBusiness', label: '浅色商务' },
    { value: 'deepPurple', label: '紫蓝深邃' },
      { value: 'ecoGreen', label: '青绿生态' },
    ],
  },
})

const emit = defineEmits(['update:activeTab', 'change'])

const currentTab = computed(() => {
  if (props.activeTab) return props.activeTab
  return props.tabs.length > 0 ? props.tabs[0].key : ''
})

const handleTabClick = (tab, index) => {
  emit('update:activeTab', tab.key)
  emit('change', { key: tab.key, label: tab.label, index })
}
</script>

<style lang="scss" scoped>
.bottom-nav-tabs {
  width: 100%;
  padding: 8px 0;
}

.tabs-container {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
}

/* ========== 胶囊模式 ========== */
.mode-capsule .tab-item {
  position: relative;
  padding: 8px 24px;
  border-radius: 20px;
  cursor: pointer;
  transition: all 0.3s ease;
  background: var(--tab-bg);
  border: 1px solid var(--tab-border-color);
  overflow: hidden;

  .tab-label {
    position: relative;
    z-index: 2;
    font-size: 13px;
    color: var(--tab-text-color);
    transition: color 0.3s;
    white-space: nowrap;
  }

  .tab-glow {
    position: absolute;
    inset: 0;
    opacity: 0;
    background: var(--tab-active-bg);
    border-radius: inherit;
    transition: opacity 0.3s;
    z-index: 1;
  }

  &:hover {
    border-color: var(--tab-active-border);

    .tab-label {
      color: var(--tab-active-text);
    }
  }

  &.active {
    border-color: var(--tab-active-border);
    box-shadow: 0 0 12px var(--tab-glow-color), inset 0 0 12px var(--tab-glow-inner);

    .tab-label {
      color: var(--tab-active-text);
      font-weight: 600;
    }

    .tab-glow {
      opacity: 1;
    }
  }
}

/* ========== 图标+文字模式 ========== */
.mode-icon-text .tabs-container {
  gap: 16px;
}

.mode-icon-text .tab-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 4px;
  cursor: pointer;
  padding: 6px 16px;
  border-radius: 8px;
  transition: all 0.3s ease;
  background: transparent;
  position: relative;

  .tab-icon {
    .icon-svg {
      width: 22px;
      height: 22px;
      fill: var(--tab-text-color);
      transition: fill 0.3s;
    }
  }

  .tab-label {
    font-size: 11px;
    color: var(--tab-text-color);
    transition: color 0.3s;
    white-space: nowrap;
  }

  &::after {
    content: '';
    position: absolute;
    bottom: 0;
    left: 50%;
    transform: translateX(-50%) scaleX(0);
    width: 60%;
    height: 2px;
    background: var(--tab-active-border);
    border-radius: 1px;
    transition: transform 0.3s;
    box-shadow: 0 0 6px var(--tab-glow-color);
  }

  &:hover {
    background: var(--tab-hover-bg);

    .tab-icon .icon-svg {
      fill: var(--tab-active-text);
    }

    .tab-label {
      color: var(--tab-active-text);
    }
  }

  &.active {
    background: var(--tab-hover-bg);

    .tab-icon .icon-svg {
      fill: var(--tab-active-text);
    }

    .tab-label {
      color: var(--tab-active-text);
      font-weight: 600;
    }

    &::after {
      transform: translateX(-50%) scaleX(1);
    }
  }
}

/* ========== 主题变量 ========== */

/* techBlue 深蓝科技 */
.theme-techBlue {
  --tab-bg: rgba(0, 168, 232, 0.06);
  --tab-border-color: rgba(0, 168, 232, 0.2);
  --tab-text-color: rgba(224, 244, 255, 0.6);
  --tab-hover-bg: rgba(0, 168, 232, 0.1);
  --tab-active-bg: rgba(0, 168, 232, 0.15);
  --tab-active-border: #00a8e8;
  --tab-active-text: #e0f4ff;
  --tab-glow-color: rgba(0, 168, 232, 0.4);
  --tab-glow-inner: rgba(0, 168, 232, 0.08);
}

/* partyRed 党建红金 */
.theme-partyRed {
  --tab-bg: rgba(220, 50, 50, 0.06);
  --tab-border-color: rgba(220, 50, 50, 0.2);
  --tab-text-color: rgba(255, 224, 224, 0.6);
  --tab-hover-bg: rgba(220, 50, 50, 0.1);
  --tab-active-bg: rgba(220, 50, 50, 0.15);
  --tab-active-border: #dc3232;
  --tab-active-text: #ffe0e0;
  --tab-glow-color: rgba(220, 50, 50, 0.4);
  --tab-glow-inner: rgba(220, 50, 50, 0.08);
}

/* lightBusiness 浅色商务 */
.theme-lightBusiness {
  --tab-bg: rgba(0, 120, 200, 0.04);
  --tab-border-color: rgba(0, 120, 200, 0.15);
  --tab-text-color: rgba(26, 26, 46, 0.5);
  --tab-hover-bg: rgba(0, 120, 200, 0.06);
  --tab-active-bg: rgba(0, 120, 200, 0.1);
  --tab-active-border: #0078c8;
  --tab-active-text: #0078c8;
  --tab-glow-color: rgba(0, 120, 200, 0.2);
  --tab-glow-inner: rgba(0, 120, 200, 0.04);
}
/* ecoGreen 青绿生态 */
.theme-ecoGreen {
  --panel-bg: rgba(10,30,50,0.85);
  --border-color: rgba(0,180,150,0.18);
  --border-glow: rgba(0,180,150,0.4);
  --text-primary: #ffffff;
  --text-secondary: rgba(255,255,255,0.7);
  --accent-color: #00b496;
  --header-bg: rgba(0,180,150,0.08);
  --dot-color: rgba(0,180,150,0.3);
}

</style>
```

## 主题变量支持 (theme prop)

### 主题色值对照表

| CSS 变量 | techBlue (深蓝科技) | partyRed (党建红金) | lightBusiness (浅色商务) | ecoGreen (青绿生态) |
|----------|---------------------|---------------------|------------------------|
| --tab-bg | rgba(0,168,232,0.06) | rgba(220,50,50,0.06) | rgba(0,120,200,0.04) |
| --tab-border-color | rgba(0,168,232,0.2) | rgba(220,50,50,0.2) | rgba(0,120,200,0.15) |
| --tab-text-color | rgba(224,244,255,0.6) | rgba(255,224,224,0.6) | rgba(26,26,46,0.5) |
| --tab-hover-bg | rgba(0,168,232,0.1) | rgba(220,50,50,0.1) | rgba(0,120,200,0.06) |
| --tab-active-bg | rgba(0,168,232,0.15) | rgba(220,50,50,0.15) | rgba(0,120,200,0.1) |
| --tab-active-border | #00a8e8 | #dc3232 | #0078c8 |
| --tab-active-text | #e0f4ff | #ffe0e0 | #0078c8 |
| --tab-glow-color | rgba(0,168,232,0.4) | rgba(220,50,50,0.4) | rgba(0,120,200,0.2) |
| --tab-glow-inner | rgba(0,168,232,0.08) | rgba(220,50,50,0.08) | rgba(0,120,200,0.04) |

### 主题 Props 定义

```javascript
theme: {
  type: String,
  default: 'techBlue',
  desc: '主题风格：techBlue-深蓝科技/partyRed-党建红金/lightBusiness-浅色商务',
  name: i18n.global.t('themeStyle'),
  groupKey: 'style',
  groupName: '样式配置',
  sort: 2,
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

### 主题 CSS 变量映射

```javascript
const themeVariables = {
  techBlue: {
    '--tab-bg': 'rgba(0,168,232,0.06)',
    '--tab-border-color': 'rgba(0,168,232,0.2)',
    '--tab-text-color': 'rgba(224,244,255,0.6)',
    '--tab-hover-bg': 'rgba(0,168,232,0.1)',
    '--tab-active-bg': 'rgba(0,168,232,0.15)',
    '--tab-active-border': '#00a8e8',
    '--tab-active-text': '#e0f4ff',
    '--tab-glow-color': 'rgba(0,168,232,0.4)',
    '--tab-glow-inner': 'rgba(0,168,232,0.08)',
  },
  partyRed: {
    '--tab-bg': 'rgba(220,50,50,0.06)',
    '--tab-border-color': 'rgba(220,50,50,0.2)',
    '--tab-text-color': 'rgba(255,224,224,0.6)',
    '--tab-hover-bg': 'rgba(220,50,50,0.1)',
    '--tab-active-bg': 'rgba(220,50,50,0.15)',
    '--tab-active-border': '#dc3232',
    '--tab-active-text': '#ffe0e0',
    '--tab-glow-color': 'rgba(220,50,50,0.4)',
    '--tab-glow-inner': 'rgba(220,50,50,0.08)',
  },
  lightBusiness: {
    '--tab-bg': 'rgba(0,120,200,0.04)',
    '--tab-border-color': 'rgba(0,120,200,0.15)',
    '--tab-text-color': 'rgba(26,26,46,0.5)',
    '--tab-hover-bg': 'rgba(0,120,200,0.06)',
    '--tab-active-bg': 'rgba(0,120,200,0.1)',
    '--tab-active-border': '#0078c8',
    '--tab-active-text': '#0078c8',
    '--tab-glow-color': 'rgba(0,120,200,0.2)',
    '--tab-glow-inner': 'rgba(0,120,200,0.04)',
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
}
```
