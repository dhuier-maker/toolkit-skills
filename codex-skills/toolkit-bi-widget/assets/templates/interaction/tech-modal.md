# 科幻风格弹窗模板 (TechModal)

完整参考：`references/component-templates.md` TechModal 章节

## 功能介绍

科幻风格弹窗组件，使用 clip-path polygon 实现斜切边框，四角带发光角标装饰，毛玻璃背景效果。支持3级详情下钻（level 1/2/3 逐级深入），适用于智慧乡村、智慧民宗等深色科技大屏的详情展示、数据下钻场景。

## 使用场景

- 数据卡片点击后的详情弹窗
- 多级数据下钻展示（如：总览 -> 区域 -> 详情）
- 大屏信息浮层展示

## Props 定义

### 基础配置 (groupKey: 'basic')

```javascript
visible: {
  type: Boolean,
  default: false,
  desc: i18n.global.t('visibility'),
  name: i18n.global.t('visibility'),
  groupKey: 'basic',
  groupName: '基础配置',
  sort: 1,
},
title: {
  type: String,
  default: '详情',
  desc: i18n.global.t('panelTitle'),
  name: i18n.global.t('panelTitle'),
  groupKey: 'basic',
  groupName: '基础配置',
  sort: 2,
},
width: {
  type: Number,
  default: 400,
  desc: i18n.global.t('width'),
  name: i18n.global.t('width'),
  groupKey: 'basic',
  groupName: '基础配置',
  sort: 3,
  min: 200,
  max: 1200,
},
level: {
  type: Number,
  default: 1,
  desc: '下钻层级（1/2/3），控制标题栏样式和返回按钮显示',
  name: i18n.global.t('drillLevel'),
  groupKey: 'basic',
  groupName: '基础配置',
  sort: 4,
  min: 1,
  max: 3,
},
data: {
  type: Object,
  default: () => ({}),
  desc: '弹窗展示数据',
  name: '数据',
  groupKey: 'basic',
  groupName: '基础配置',
  sort: 5,
  useDynamic: true,
},
```

### 样式配置 (groupKey: 'style', groupName: '样式配置')

```javascript
theme: {
  type: String,
  default: 'techBlue',
  desc: '主题风格：techBlue-深蓝科技/partyRed-党建红金/ecoGreen-青绿生态/warmOrange-暖橙数据/deepPurple-紫蓝深邃/lightBusiness-浅色商务',
  name: i18n.global.t('themeStyle'),
  groupKey: 'style',
  groupName: '样式配置',
  sort: 1,
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

## emit 事件

- `update:visible` - 关闭弹窗时触发（支持 v-model:visible）
- `back` - 点击返回按钮时触发（level > 1 时显示）
- `drill-down` - 下钻操作时触发，参数: `{ level, data }`

## 完整代码

```vue
<template>
  <Transition name="modal-fade">
    <div v-if="visible" class="tech-modal-overlay" @click.self="handleClose">
      <div
        class="tech-modal"
        :class="[`theme-${theme}`, `level-${level}`]"
        :style="{ '--modal-width': width + 'px' }"
      >
        <!-- 四角发光角标 -->
        <div class="corner-glow corner-tl"></div>
        <div class="corner-glow corner-tr"></div>
        <div class="corner-glow corner-bl"></div>
        <div class="corner-glow corner-br"></div>

        <!-- 斜切边框装饰 -->
        <div class="clip-border"></div>

        <!-- 标题栏 -->
        <div class="modal-header">
          <div class="header-left">
            <span v-if="level > 1" class="back-btn" @click="handleBack">
              <svg width="16" height="16" viewBox="0 0 16 16" fill="none">
                <path d="M10 3L5 8L10 13" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </span>
            <span class="level-indicator" v-if="level > 1">L{{ level }}</span>
            <span class="modal-title">{{ title }}</span>
          </div>
          <div class="header-right">
            <span class="close-btn" @click="handleClose">
              <svg width="14" height="14" viewBox="0 0 14 14" fill="none">
                <path d="M1 1L13 13M13 1L1 13" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
              </svg>
            </span>
          </div>
        </div>

        <!-- 内容区域 -->
        <div class="modal-content">
          <slot :level="level" :data="data">
            <div class="default-content">
              <div v-for="(value, key) in data" :key="key" class="data-row">
                <span class="data-label">{{ key }}</span>
                <span class="data-value">{{ value }}</span>
              </div>
            </div>
          </slot>
        </div>

        <!-- 底部操作栏 -->
        <div v-if="$slots.footer" class="modal-footer">
          <slot name="footer" :level="level" :data="data"></slot>
        </div>
      </div>
    </div>
  </Transition>
</template>

<script setup>
import { computed, watch } from 'vue'

const props = defineProps({
  visible: {
    type: Boolean,
    default: false,
    desc: i18n.global.t('visibility'),
    name: i18n.global.t('visibility'),
    groupKey: 'basic',
    groupName: '基础配置',
    sort: 1,
  },
  title: {
    type: String,
    default: '详情',
    desc: i18n.global.t('panelTitle'),
    name: i18n.global.t('panelTitle'),
    groupKey: 'basic',
    groupName: '基础配置',
    sort: 2,
  },
  width: {
    type: Number,
    default: 400,
    desc: i18n.global.t('width'),
    name: i18n.global.t('width'),
    groupKey: 'basic',
    groupName: '基础配置',
    sort: 3,
    min: 200,
    max: 1200,
  },
  level: {
    type: Number,
    default: 1,
    desc: '下钻层级（1/2/3），控制标题栏样式和返回按钮显示',
    name: i18n.global.t('drillLevel'),
    groupKey: 'basic',
    groupName: '基础配置',
    sort: 4,
    min: 1,
    max: 3,
  },
  data: {
    type: Object,
    default: () => ({}),
    desc: '弹窗展示数据',
    name: '数据',
    groupKey: 'basic',
    groupName: '基础配置',
    sort: 5,
    useDynamic: true,
  },
  theme: {
    type: String,
    default: 'techBlue',
    desc: '主题风格：techBlue-深蓝科技/partyRed-党建红金/ecoGreen-青绿生态/warmOrange-暖橙数据/deepPurple-紫蓝深邃/lightBusiness-浅色商务',
    name: i18n.global.t('themeStyle'),
    groupKey: 'style',
    groupName: '样式配置',
    sort: 1,
    configurationTemplate: [
      { value: 'techBlue', label: '深蓝科技' },
      { value: 'ecoGreen', label: '青绿生态' },
      { value: 'partyRed', label: '党建红金' },
      { value: 'warmOrange', label: '暖橙数据' },
      { value: 'deepPurple', label: '紫蓝深邃' },
      { value: 'lightBusiness', label: '浅色商务' },
    ],
  },
})

const emit = defineEmits(['update:visible', 'back', 'drill-down'])

const handleClose = () => {
  emit('update:visible', false)
}

const handleBack = () => {
  emit('back', { level: props.level, data: props.data })
}

// 锁定滚动
watch(() => props.visible, (val) => {
  document.body.style.overflow = val ? 'hidden' : ''
})
</script>

<style lang="scss" scoped>
.tech-modal-overlay {
  position: fixed;
  inset: 0;
  z-index: 9999;
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(0, 0, 0, 0.6);
  backdrop-filter: blur(4px);
}

.tech-modal {
  position: relative;
  width: var(--modal-width);
  max-height: 80vh;
  display: flex;
  flex-direction: column;
  background: var(--modal-bg);
  border: 1px solid var(--modal-border-color);
  clip-path: polygon(
    0 12px, 12px 0,
    calc(100% - 12px) 0, 100% 12px,
    100% calc(100% - 12px), calc(100% - 12px) 100%,
    12px 100%, 0 calc(100% - 12px)
  );
  box-shadow: 0 0 30px var(--modal-glow-color);
  overflow: hidden;
}

/* 斜切边框装饰线 */
.clip-border {
  position: absolute;
  inset: 0;
  clip-path: polygon(
    0 12px, 12px 0,
    calc(100% - 12px) 0, 100% 12px,
    100% calc(100% - 12px), calc(100% - 12px) 100%,
    12px 100%, 0 calc(100% - 12px)
  );
  border: 1px solid var(--modal-border-accent);
  pointer-events: none;
  z-index: 1;
}

/* 四角发光角标 */
.corner-glow {
  position: absolute;
  width: 24px;
  height: 24px;
  z-index: 2;
  pointer-events: none;

  &::before, &::after {
    content: '';
    position: absolute;
    background: var(--modal-corner-color);
    box-shadow: 0 0 8px var(--modal-corner-glow);
  }

  &::before {
    width: 16px;
    height: 2px;
  }

  &::after {
    width: 2px;
    height: 16px;
  }
}

.corner-tl {
  top: 4px; left: 4px;
  &::before { top: 0; left: 0; }
  &::after { top: 0; left: 0; }
}

.corner-tr {
  top: 4px; right: 4px;
  &::before { top: 0; right: 0; }
  &::after { top: 0; right: 0; }
}

.corner-bl {
  bottom: 4px; left: 4px;
  &::before { bottom: 0; left: 0; }
  &::after { bottom: 0; left: 0; }
}

.corner-br {
  bottom: 4px; right: 4px;
  &::before { bottom: 0; right: 0; }
  &::after { bottom: 0; right: 0; }
}

/* 标题栏 */
.modal-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 14px 20px;
  border-bottom: 1px solid var(--modal-border-color);
  background: var(--modal-header-bg);
  position: relative;
  z-index: 3;

  .header-left {
    display: flex;
    align-items: center;
    gap: 8px;
  }

  .back-btn {
    cursor: pointer;
    color: var(--modal-accent-color);
    transition: color 0.2s;
    display: flex;
    align-items: center;

    &:hover {
      color: var(--modal-accent-hover);
    }
  }

  .level-indicator {
    font-size: 11px;
    padding: 1px 6px;
    border-radius: 3px;
    background: var(--modal-accent-color);
    color: #fff;
    font-weight: 600;
  }

  .modal-title {
    font-size: 16px;
    font-weight: 600;
    color: var(--modal-title-color);
    letter-spacing: 1px;
  }

  .close-btn {
    cursor: pointer;
    color: var(--modal-text-secondary);
    transition: all 0.2s;
    display: flex;
    align-items: center;
    padding: 4px;

    &:hover {
      color: var(--modal-accent-color);
      transform: rotate(90deg);
    }
  }
}

/* 层级样式 */
.level-2 .modal-header {
  border-bottom-color: var(--modal-accent-color);
  box-shadow: inset 0 -1px 0 var(--modal-glow-color);
}

.level-3 .modal-header {
  background: var(--modal-header-deep-bg);
  border-bottom-color: var(--modal-accent-color);
  box-shadow: inset 0 -2px 0 var(--modal-accent-color), 0 2px 10px var(--modal-glow-color);
}

/* 内容区域 */
.modal-content {
  flex: 1;
  padding: 20px;
  overflow-y: auto;
  position: relative;
  z-index: 3;

  &::-webkit-scrollbar {
    width: 4px;
  }

  &::-webkit-scrollbar-thumb {
    background: var(--modal-accent-color);
    border-radius: 2px;
  }

  &::-webkit-scrollbar-track {
    background: transparent;
  }
}

.default-content {
  .data-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 8px 0;
    border-bottom: 1px solid var(--modal-border-color);

    &:last-child {
      border-bottom: none;
    }
  }

  .data-label {
    color: var(--modal-text-secondary);
    font-size: 13px;
  }

  .data-value {
    color: var(--modal-text-primary);
    font-size: 14px;
    font-weight: 500;
  }
}

/* 底部操作栏 */
.modal-footer {
  padding: 12px 20px;
  border-top: 1px solid var(--modal-border-color);
  display: flex;
  justify-content: flex-end;
  gap: 10px;
  position: relative;
  z-index: 3;
}

/* 过渡动画 */
.modal-fade-enter-active,
.modal-fade-leave-active {
  transition: opacity 0.3s ease;

  .tech-modal {
    transition: transform 0.3s ease, opacity 0.3s ease;
  }
}

.modal-fade-enter-from,
.modal-fade-leave-to {
  opacity: 0;

  .tech-modal {
    transform: scale(0.9) translateY(20px);
    opacity: 0;
  }
}

/* ========== 主题变量 ========== */

/* techBlue 深蓝科技 */
.theme-techBlue {
  --modal-bg: rgba(6, 30, 65, 0.92);
  --modal-border-color: rgba(0, 168, 232, 0.25);
  --modal-border-accent: rgba(0, 168, 232, 0.5);
  --modal-glow-color: rgba(0, 168, 232, 0.15);
  --modal-corner-color: #00D4FF;
  --modal-corner-glow: rgba(0, 212, 255, 0.6);
  --modal-header-bg: rgba(0, 168, 232, 0.08);
  --modal-header-deep-bg: rgba(0, 168, 232, 0.15);
  --modal-title-color: #E0E8FF;
  --modal-accent-color: #00D4FF;
  --modal-accent-hover: #33c5f5;
  --modal-text-primary: #E0E8FF;
  --modal-text-secondary: rgba(224, 244, 255, 0.6);
}

/* partyRed 党建红金 */
.theme-partyRed {
  --modal-bg: rgba(60, 10, 10, 0.92);
  --modal-border-color: rgba(255, 77, 79, 0.4);
  --modal-border-accent: rgba(255, 77, 79, 0.5);
  --modal-glow-color: rgba(255, 77, 79, 0.15);
  --modal-corner-color: #FF4D4F;
  --modal-corner-glow: rgba(255, 215, 0, 0.6);
  --modal-header-bg: rgba(255, 77, 79, 0.08);
  --modal-header-deep-bg: rgba(255, 77, 79, 0.15);
  --modal-title-color: #FFE0E0;
  --modal-accent-color: #FF4D4F;
  --modal-accent-hover: #f05050;
  --modal-text-primary: #FFE0E0;
  --modal-text-secondary: rgba(255, 224, 224, 0.6);
}

/* lightBusiness 浅色商务 */
.theme-lightBusiness {
  --modal-bg: rgba(255, 255, 255, 0.95);
  --modal-border-color: #E8E8E8;
  --modal-border-accent: rgba(24, 144, 255, 0.3);
  --modal-glow-color: transparent;
  --modal-corner-color: #1890FF;
  --modal-corner-glow: transparent;
  --modal-header-bg: rgba(24, 144, 255, 0.04);
  --modal-header-deep-bg: rgba(24, 144, 255, 0.08);
  --modal-title-color: #595959;
  --modal-accent-color: #1890FF;
  --modal-accent-hover: #40a9ff;
  --modal-text-primary: #595959;
  --modal-text-secondary: rgba(89, 89, 89, 0.5);
}

/* ecoGreen 青绿生态 */
.theme-ecoGreen {
  --modal-bg: rgba(6, 42, 42, 0.92);
  --modal-border-color: rgba(0, 229, 195, 0.3);
  --modal-border-accent: rgba(0, 229, 195, 0.5);
  --modal-glow-color: rgba(0, 229, 195, 0.15);
  --modal-corner-color: #00E5C3;
  --modal-corner-glow: rgba(0, 229, 195, 0.6);
  --modal-header-bg: rgba(0, 229, 195, 0.08);
  --modal-header-deep-bg: rgba(0, 229, 195, 0.15);
  --modal-title-color: #E0FFF0;
  --modal-accent-color: #00E5C3;
  --modal-accent-hover: #33f5d5;
  --modal-text-primary: #E0FFF0;
  --modal-text-secondary: rgba(224, 255, 240, 0.6);
}

/* warmOrange 暖橙数据 */
.theme-warmOrange {
  --modal-bg: rgba(50, 35, 15, 0.92);
  --modal-border-color: rgba(255, 140, 66, 0.3);
  --modal-border-accent: rgba(255, 140, 66, 0.5);
  --modal-glow-color: rgba(255, 140, 66, 0.15);
  --modal-corner-color: #FF8C42;
  --modal-corner-glow: rgba(255, 140, 66, 0.6);
  --modal-header-bg: rgba(255, 140, 66, 0.08);
  --modal-header-deep-bg: rgba(255, 140, 66, 0.15);
  --modal-title-color: #FFF0E0;
  --modal-accent-color: #FF8C42;
  --modal-accent-hover: #ffa366;
  --modal-text-primary: #FFF0E0;
  --modal-text-secondary: rgba(255, 240, 224, 0.6);
}

/* deepPurple 紫蓝深邃 */
.theme-deepPurple {
  --modal-bg: rgba(20, 16, 60, 0.92);
  --modal-border-color: rgba(168, 85, 247, 0.3);
  --modal-border-accent: rgba(168, 85, 247, 0.5);
  --modal-glow-color: rgba(168, 85, 247, 0.15);
  --modal-corner-color: #A855F7;
  --modal-corner-glow: rgba(168, 85, 247, 0.6);
  --modal-header-bg: rgba(168, 85, 247, 0.08);
  --modal-header-deep-bg: rgba(168, 85, 247, 0.15);
  --modal-title-color: #E8E0FF;
  --modal-accent-color: #A855F7;
  --modal-accent-hover: #c084fc;
  --modal-text-primary: #E8E0FF;
  --modal-text-secondary: rgba(232, 224, 255, 0.6);
}

</style>
```

## 主题变量支持 (theme prop)

### 主题色值对照表

| CSS 变量 | techBlue (深蓝科技) | ecoGreen (青绿生态) | partyRed (党建红金) | warmOrange (暖橙数据) | deepPurple (紫蓝深邃) | lightBusiness (浅色商务) |
|----------|---------------------|---------------------|---------------------|----------------------|----------------------|-------------------------|
| --modal-bg | rgba(6,30,65,0.92) | rgba(6,42,42,0.92) | rgba(60,10,10,0.92) | rgba(50,35,15,0.92) | rgba(20,16,60,0.92) | rgba(255,255,255,0.95) |
| --modal-border-color | rgba(0,168,232,0.25) | rgba(0,229,195,0.3) | rgba(255,77,79,0.4) | rgba(255,140,66,0.3) | rgba(168,85,247,0.3) | #E8E8E8 |
| --modal-border-accent | rgba(0,168,232,0.5) | rgba(0,229,195,0.5) | rgba(255,77,79,0.5) | rgba(255,140,66,0.5) | rgba(168,85,247,0.5) | rgba(24,144,255,0.3) |
| --modal-glow-color | rgba(0,168,232,0.15) | rgba(0,229,195,0.15) | rgba(255,77,79,0.15) | rgba(255,140,66,0.15) | rgba(168,85,247,0.15) | transparent |
| --modal-corner-color | #00D4FF | #00E5C3 | #FF4D4F | #FF8C42 | #A855F7 | #1890FF |
| --modal-corner-glow | rgba(0,212,255,0.6) | rgba(0,229,195,0.6) | rgba(255,215,0,0.6) | rgba(255,140,66,0.6) | rgba(168,85,247,0.6) | transparent |
| --modal-header-bg | rgba(0,168,232,0.08) | rgba(0,229,195,0.08) | rgba(255,77,79,0.08) | rgba(255,140,66,0.08) | rgba(168,85,247,0.08) | rgba(24,144,255,0.04) |
| --modal-title-color | #E0E8FF | #E0FFF0 | #FFE0E0 | #FFF0E0 | #E8E0FF | #595959 |
| --modal-accent-color | #00D4FF | #00E5C3 | #FF4D4F | #FF8C42 | #A855F7 | #1890FF |
| --modal-text-primary | #E0E8FF | #E0FFF0 | #FFE0E0 | #FFF0E0 | #E8E0FF | #595959 |
| --modal-text-secondary | rgba(224,244,255,0.6) | rgba(224,255,240,0.6) | rgba(255,224,224,0.6) | rgba(255,240,224,0.6) | rgba(232,224,255,0.6) | rgba(89,89,89,0.5) |

### 主题 Props 定义

```javascript
theme: {
  type: String,
  default: 'techBlue',
  desc: '主题风格：techBlue-深蓝科技/partyRed-党建红金/ecoGreen-青绿生态/warmOrange-暖橙数据/deepPurple-紫蓝深邃/lightBusiness-浅色商务',
  name: i18n.global.t('themeStyle'),
  groupKey: 'style',
  groupName: '样式配置',
  sort: 1,
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

### 主题 CSS 变量映射

```javascript
const themeVariables = {
  techBlue: {
    '--modal-bg': 'rgba(6,30,65,0.92)',
    '--modal-border-color': 'rgba(0,168,232,0.25)',
    '--modal-border-accent': 'rgba(0,168,232,0.5)',
    '--modal-glow-color': 'rgba(0,168,232,0.15)',
    '--modal-corner-color': '#00D4FF',
    '--modal-corner-glow': 'rgba(0,212,255,0.6)',
    '--modal-header-bg': 'rgba(0,168,232,0.08)',
    '--modal-header-deep-bg': 'rgba(0,168,232,0.15)',
    '--modal-title-color': '#E0E8FF',
    '--modal-accent-color': '#00D4FF',
    '--modal-accent-hover': '#33c5f5',
    '--modal-text-primary': '#E0E8FF',
    '--modal-text-secondary': 'rgba(224,244,255,0.6)',
  },
  ecoGreen: {
    '--modal-bg': 'rgba(6,42,42,0.92)',
    '--modal-border-color': 'rgba(0,229,195,0.3)',
    '--modal-border-accent': 'rgba(0,229,195,0.5)',
    '--modal-glow-color': 'rgba(0,229,195,0.15)',
    '--modal-corner-color': '#00E5C3',
    '--modal-corner-glow': 'rgba(0,229,195,0.6)',
    '--modal-header-bg': 'rgba(0,229,195,0.08)',
    '--modal-header-deep-bg': 'rgba(0,229,195,0.15)',
    '--modal-title-color': '#E0FFF0',
    '--modal-accent-color': '#00E5C3',
    '--modal-accent-hover': '#33f5d5',
    '--modal-text-primary': '#E0FFF0',
    '--modal-text-secondary': 'rgba(224,255,240,0.6)',
  },
  partyRed: {
    '--modal-bg': 'rgba(60,10,10,0.92)',
    '--modal-border-color': 'rgba(255,77,79,0.4)',
    '--modal-border-accent': 'rgba(255,77,79,0.5)',
    '--modal-glow-color': 'rgba(255,77,79,0.15)',
    '--modal-corner-color': '#FF4D4F',
    '--modal-corner-glow': 'rgba(255,215,0,0.6)',
    '--modal-header-bg': 'rgba(255,77,79,0.08)',
    '--modal-header-deep-bg': 'rgba(255,77,79,0.15)',
    '--modal-title-color': '#FFE0E0',
    '--modal-accent-color': '#FF4D4F',
    '--modal-accent-hover': '#f05050',
    '--modal-text-primary': '#FFE0E0',
    '--modal-text-secondary': 'rgba(255,224,224,0.6)',
  },
  warmOrange: {
    '--modal-bg': 'rgba(50,35,15,0.92)',
    '--modal-border-color': 'rgba(255,140,66,0.3)',
    '--modal-border-accent': 'rgba(255,140,66,0.5)',
    '--modal-glow-color': 'rgba(255,140,66,0.15)',
    '--modal-corner-color': '#FF8C42',
    '--modal-corner-glow': 'rgba(255,140,66,0.6)',
    '--modal-header-bg': 'rgba(255,140,66,0.08)',
    '--modal-header-deep-bg': 'rgba(255,140,66,0.15)',
    '--modal-title-color': '#FFF0E0',
    '--modal-accent-color': '#FF8C42',
    '--modal-accent-hover': '#ffa366',
    '--modal-text-primary': '#FFF0E0',
    '--modal-text-secondary': 'rgba(255,240,224,0.6)',
  },
  deepPurple: {
    '--modal-bg': 'rgba(20,16,60,0.92)',
    '--modal-border-color': 'rgba(168,85,247,0.3)',
    '--modal-border-accent': 'rgba(168,85,247,0.5)',
    '--modal-glow-color': 'rgba(168,85,247,0.15)',
    '--modal-corner-color': '#A855F7',
    '--modal-corner-glow': 'rgba(168,85,247,0.6)',
    '--modal-header-bg': 'rgba(168,85,247,0.08)',
    '--modal-header-deep-bg': 'rgba(168,85,247,0.15)',
    '--modal-title-color': '#E8E0FF',
    '--modal-accent-color': '#A855F7',
    '--modal-accent-hover': '#c084fc',
    '--modal-text-primary': '#E8E0FF',
    '--modal-text-secondary': 'rgba(232,224,255,0.6)',
  },
  lightBusiness: {
    '--modal-bg': 'rgba(255,255,255,0.95)',
    '--modal-border-color': '#E8E8E8',
    '--modal-border-accent': 'rgba(24,144,255,0.3)',
    '--modal-glow-color': 'transparent',
    '--modal-corner-color': '#1890FF',
    '--modal-corner-glow': 'transparent',
    '--modal-header-bg': 'rgba(24,144,255,0.04)',
    '--modal-header-deep-bg': 'rgba(24,144,255,0.08)',
    '--modal-title-color': '#595959',
    '--modal-accent-color': '#1890FF',
    '--modal-accent-hover': '#40a9ff',
    '--modal-text-primary': '#595959',
    '--modal-text-secondary': 'rgba(89,89,89,0.5)',
  },
}
```
