# AI识别卡片模板 (AIRecognitionCard)

完整参考：`references/component-templates.md` AIRecognitionCard 章节

## 功能介绍

显示AI识别类型和数据的卡片，带圆形AI图标。适用于智慧街道等包含AI识别功能的大屏。

## Props 定义

### 基础配置 (groupKey: 'basic')

```javascript
type: {
  type: String,
  default: '识别类型',
  desc: 'AI识别类型名称',
  name: '类型',
  groupKey: 'basic',
  groupName: '基础配置',
  sort: 1,
},
current: {
  type: Number,
  default: 0,
  desc: '当前识别数量',
  name: '当前数',
  groupKey: 'basic',
  groupName: '基础配置',
  sort: 2,
},
total: {
  type: Number,
  default: 0,
  desc: '总数量',
  name: '总数',
  groupKey: 'basic',
  groupName: '基础配置',
  sort: 3,
},
status: {
  type: String,
  default: 'normal',
  desc: '状态：success-成功/绿色, warning-警告/橙色, normal-普通/蓝色',
  name: '状态',
  groupKey: 'basic',
  groupName: '基础配置',
  sort: 4,
  configurationTemplate: [
    { value: 'success', label: '成功' },
    { value: 'warning', label: '警告' },
    { value: 'normal', label: '普通' },
  ],
},
```

## 状态颜色

```css
.data-current.status-success { color: #52c41a; }
.data-current.status-warning { color: #faad14; }
.data-current.status-normal { color: #4a90e2; }
```

## 模板结构

```html
<div class="ai-recognition-card">
  <div class="ai-icon">
    <span class="ai-text">AI</span>
  </div>
  <div class="card-content">
    <div class="recognition-type">{{ type }}</div>
    <div class="recognition-data">
      <span class="data-current" :class="'status-' + status">{{ current }}</span>
      <span class="data-separator">/</span>
      <span class="data-total">{{ total }}</span>
    </div>
  </div>
</div>
```

## 完整代码

完整AI识别卡片代码请参考 `references/component-templates.md` 中 AIRecognitionCard 章节。


## 主题变量支持 (theme prop)

### 主题值

| 主题 | panelBg | borderColor | borderGlow | textPrimary | textSecondary | accentColor | headerBg | dotColor |
|------|---------|-------------|------------|-------------|---------------|-------------|----------|----------|
| techBlue | rgba(6,30,93,0.8) | rgba(0,212,255,0.3) | rgba(0,212,255,0.6) | #E0E8FF | #6B7FA3 | #00D4FF | rgba(0,212,255,0.08) | rgba(0,212,255,0.3) |
| ecoGreen | rgba(6,42,42,0.8) | rgba(0,229,195,0.3) | rgba(0,229,195,0.6) | #E0FFF0 | #5A8A7A | #00E5C3 | rgba(0,229,195,0.08) | rgba(0,229,195,0.3) |
| partyRed | rgba(60,15,15,0.8) | rgba(255,77,79,0.4) | rgba(255,215,0,0.6) | #FFE0E0 | #8A6A6A | #FF4D4F | rgba(255,77,79,0.08) | rgba(255,77,79,0.3) |
| warmOrange | rgba(50,35,15,0.8) | rgba(255,140,66,0.3) | rgba(255,140,66,0.6) | #FFF0E0 | #8A7A6A | #FF8C42 | rgba(255,140,66,0.08) | rgba(255,140,66,0.3) |
| deepPurple | rgba(20,16,60,0.8) | rgba(168,85,247,0.3) | rgba(168,85,247,0.6) | #E8E0FF | #7A6A8A | #A855F7 | rgba(168,85,247,0.08) | rgba(168,85,247,0.3) |
| lightBusiness | rgba(255,255,255,0.95) | #E8E8E8 | transparent | #595959 | #8C8C8C | #1890FF | rgba(24,144,255,0.06) | rgba(24,144,255,0.2) |

### Theme Props Definition

```javascript
theme: {
  type: String,
  default: 'techBlue',
  desc: i18n.global.t('themeStyle'),
  name: i18n.global.t('themeStyle'),
  groupKey: 'style',
  groupName: i18n.global.t('styleConfiguration'),
  sort: 99,
},
```

### Theme CSS Variable Mapping

```javascript
const themeVariables = {
  techBlue: {
    panelBg: 'rgba(6,30,93,0.8)',
    borderColor: 'rgba(0,212,255,0.3)',
    borderGlow: 'rgba(0,212,255,0.6)',
    textPrimary: '#E0E8FF',
    textSecondary: '#6B7FA3',
    accentColor: '#00D4FF',
    headerBg: 'rgba(0,212,255,0.08)',
    dotColor: 'rgba(0,212,255,0.3)',
  },
  ecoGreen: {
    panelBg: 'rgba(6,42,42,0.8)',
    borderColor: 'rgba(0,229,195,0.3)',
    borderGlow: 'rgba(0,229,195,0.6)',
    textPrimary: '#E0FFF0',
    textSecondary: '#5A8A7A',
    accentColor: '#00E5C3',
    headerBg: 'rgba(0,229,195,0.08)',
    dotColor: 'rgba(0,229,195,0.3)',
  },
  partyRed: {
    panelBg: 'rgba(60,15,15,0.8)',
    borderColor: 'rgba(255,77,79,0.4)',
    borderGlow: 'rgba(255,215,0,0.6)',
    textPrimary: '#FFE0E0',
    textSecondary: '#8A6A6A',
    accentColor: '#FF4D4F',
    headerBg: 'rgba(255,77,79,0.08)',
    dotColor: 'rgba(255,77,79,0.3)',
  },
  warmOrange: {
    panelBg: 'rgba(50,35,15,0.8)',
    borderColor: 'rgba(255,140,66,0.3)',
    borderGlow: 'rgba(255,140,66,0.6)',
    textPrimary: '#FFF0E0',
    textSecondary: '#8A7A6A',
    accentColor: '#FF8C42',
    headerBg: 'rgba(255,140,66,0.08)',
    dotColor: 'rgba(255,140,66,0.3)',
  },
  deepPurple: {
    panelBg: 'rgba(20,16,60,0.8)',
    borderColor: 'rgba(168,85,247,0.3)',
    borderGlow: 'rgba(168,85,247,0.6)',
    textPrimary: '#E8E0FF',
    textSecondary: '#7A6A8A',
    accentColor: '#A855F7',
    headerBg: 'rgba(168,85,247,0.08)',
    dotColor: 'rgba(168,85,247,0.3)',
  },
  lightBusiness: {
    panelBg: 'rgba(255,255,255,0.95)',
    borderColor: '#E8E8E8',
    borderGlow: 'transparent',
    textPrimary: '#595959',
    textSecondary: '#8C8C8C',
    accentColor: '#1890FF',
    headerBg: 'rgba(24,144,255,0.06)',
    dotColor: 'rgba(24,144,255,0.2)',
  },
}
```
