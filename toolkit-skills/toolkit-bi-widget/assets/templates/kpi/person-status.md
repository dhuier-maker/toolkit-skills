# 人员状态卡片模板 (PersonStatusCard)

完整参考：`references/component-templates.md` PersonStatusCard 章节

## 功能介绍

显示人员头像、姓名、状态信息的卡片组件。适用于智慧党建、智慧养老等需要展示人员信息的大屏。

## Props 定义

### 基础配置 (groupKey: 'basic')

```javascript
name: {
  type: String,
  default: '姓名',
  desc: '人员姓名',
  name: '姓名',
  groupKey: 'basic',
  groupName: '基础配置',
  sort: 1,
},
avatarUrl: { type: String, default: '' },
role: { type: String, default: '' },
extraInfo: { type: String, default: '' },
status: {
  type: String,
  default: 'online',
  desc: '状态：online-在线, offline-离线, busy-忙碌, normal-正常',
  name: '状态',
  groupKey: 'basic',
  groupName: '基础配置',
  sort: 5,
  configurationTemplate: [
    { value: 'online', label: '在线' },
    { value: 'offline', label: '离线' },
    { value: 'busy', label: '忙碌' },
    { value: 'normal', label: '正常' },
  ],
},
statusText: { type: String, default: '' },
```

## 状态点颜色

```css
.status-online .status-dot { background: #52c41a; box-shadow: 0 0 6px #52c41a; }
.status-offline .status-dot { background: #f5222d; }
.status-busy .status-dot { background: #faad14; }
.status-normal .status-dot { background: #00a8e8; }
```

## 模板结构

```html
<div class="person-status-card" :class="[`status-${status}`]">
  <div class="avatar-wrapper">
    <img v-if="avatarUrl" :src="avatarUrl" class="avatar-img" />
    <div v-else class="avatar-placeholder">
      <span>{{ name.charAt(0) }}</span>
    </div>
    <div class="status-dot"></div>
  </div>
  <div class="person-info">
    <div class="person-name">{{ name }}</div>
    <div v-if="role" class="person-role">{{ role }}</div>
    <div v-if="extraInfo" class="person-extra">{{ extraInfo }}</div>
  </div>
  <div v-if="statusText" class="status-tag">{{ statusText }}</div>
</div>
```

## 完整代码

完整人员状态卡片代码请参考 `references/component-templates.md` 中 PersonStatusCard 章节。


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
