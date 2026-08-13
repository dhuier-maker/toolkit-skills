# 日历面板组件 (CalendarPanel)

## 概述
日历面板组件，显示月度日历网格 + 事件列表。适用于 BI 大屏侧边栏，展示日程、活动、会议等信息。

## 使用场景
- 智慧社区活动日历
- 会议日程展示
- 事件提醒面板

## Props 定义

| 属性 | 类型 | 默认值 | 说明 | groupKey | sort |
|------|------|--------|------|----------|------|
| currentMonth | String | '' | 当前月份 (YYYY-MM)，空则取当前月 | data | 1 |
| events | Array | [{date:'2025-01-15',title:'社区活动',type:'activity'},{date:'2025-01-20',title:'业主会议',type:'meeting'}] | 事件列表 | data | 2 |
| theme | String | 'techBlue' | 主题风格 | style | 99 |

### Props 元数据

```javascript
currentMonth: {
  type: String,
  default: '',
  desc: '当前月份 (YYYY-MM)',
  name: '月份',
  groupKey: 'data',
  groupName: i18n.global.t('dataConfiguration'),
  sort: 1,
},
events: {
  type: Array,
  default: () => [
    { date: '2025-01-15', title: '社区活动', type: 'activity' },
    { date: '2025-01-20', title: '业主会议', type: 'meeting' },
  ],
  desc: i18n.global.t('dataSpecification'),
  name: i18n.global.t('displayContent'),
  groupKey: 'data',
  groupName: i18n.global.t('dataConfiguration'),
  useDynamic: true,
  sort: 2,
},
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

## 完整组件代码

```vue
<template>
  <div class="calendar-panel" :style="themeVars">
    <div class="calendar-header">
      <span class="month-title">{{ monthLabel }}</span>
    </div>
    <div class="calendar-grid">
      <div v-for="d in weekDays" :key="d" class="week-day">{{ d }}</div>
      <div
        v-for="(day, i) in calendarDays"
        :key="i"
        class="day-cell"
        :class="{ 'has-event': day.hasEvent, 'is-today': day.isToday, 'other-month': !day.currentMonth }"
        @click="day.hasEvent && $emit('eventClick', day.events)"
      >
        <span class="day-num">{{ day.day }}</span>
        <div v-if="day.hasEvent" class="event-dot"></div>
      </div>
    </div>
    <div class="event-list">
      <div v-for="(evt, i) in monthEvents" :key="i" class="event-item" :class="evt.type">
        <span class="event-date">{{ evt.date.slice(5) }}</span>
        <span class="event-title">{{ evt.title }}</span>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  currentMonth: { type: String, default: '' },
  events: { type: Array, default: () => [] },
  theme: { type: String, default: 'techBlue' },
})

defineEmits(['eventClick'])

const weekDays = ['日', '一', '二', '三', '四', '五', '六']

const now = new Date()
const [year, month] = props.currentMonth
  ? props.currentMonth.split('-').map(Number)
  : [now.getFullYear(), now.getMonth() + 1]

const monthLabel = `${year}年${month}月`

const firstDay = new Date(year, month - 1, 1).getDay()
const daysInMonth = new Date(year, month, 0).getDate()
const prevDays = new Date(year, month - 1, 0).getDate()

const calendarDays = computed(() => {
  const days = []
  for (let i = firstDay - 1; i >= 0; i--) {
    days.push({ day: prevDays - i, currentMonth: false, hasEvent: false, isToday: false, events: [] })
  }
  for (let d = 1; d <= daysInMonth; d++) {
    const dateStr = `${year}-${String(month).padStart(2, '0')}-${String(d).padStart(2, '0')}`
    const dayEvents = props.events.filter(e => e.date === dateStr)
    const isToday = d === now.getDate() && month === now.getMonth() + 1 && year === now.getFullYear()
    days.push({ day: d, currentMonth: true, hasEvent: dayEvents.length > 0, isToday, events: dayEvents })
  }
  const remaining = 42 - days.length
  for (let d = 1; d <= remaining; d++) {
    days.push({ day: d, currentMonth: false, hasEvent: false, isToday: false, events: [] })
  }
  return days
})

const monthEvents = computed(() => {
  return props.events.filter(e => e.date.startsWith(`${year}-${String(month).padStart(2, '0')}`))
})

const themeVariables = {
  techBlue: {
    panelBg: 'rgba(13,25,41,0.85)', borderColor: 'rgba(0,212,255,0.18)',
    textPrimary: '#ffffff', textSecondary: 'rgba(255,255,255,0.7)',
    accentColor: '#00d4ff', headerBg: 'rgba(0,212,255,0.08)',
  },
  partyRed: {
    panelBg: 'rgba(30,10,10,0.85)', borderColor: 'rgba(220,50,50,0.18)',
    textPrimary: '#ffffff', textSecondary: 'rgba(255,255,255,0.7)',
    accentColor: '#dc3232', headerBg: 'rgba(220,50,50,0.08)',
  },
  lightBusiness: {
    panelBg: 'rgba(255,255,255,0.92)', borderColor: 'rgba(0,100,200,0.12)',
    textPrimary: '#333333', textSecondary: 'rgba(0,0,0,0.5)',
    accentColor: '#0078d4', headerBg: 'rgba(0,100,200,0.06)',
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

const themeVars = computed(() => {
  const vars = themeVariables[props.theme] || themeVariables.techBlue
  return {
    '--panel-bg': vars.panelBg, '--border-color': vars.borderColor,
    '--text-primary': vars.textPrimary, '--text-secondary': vars.textSecondary,
    '--accent-color': vars.accentColor, '--header-bg': vars.headerBg,
  }
})
</script>

<style scoped lang="scss">
.calendar-panel {
  background: var(--panel-bg);
  border: 1px solid var(--border-color);
  border-radius: 8px;
  padding: 12px;
  color: var(--text-primary);
}
.calendar-header {
  text-align: center;
  padding: 4px 0 8px;
  font-size: 14px;
  font-weight: 600;
  border-bottom: 1px solid var(--border-color);
}
.calendar-grid {
  display: grid;
  grid-template-columns: repeat(7, 1fr);
  gap: 2px;
  margin: 8px 0;
}
.week-day { text-align: center; font-size: 10px; color: var(--text-secondary); padding: 2px; }
.day-cell {
  text-align: center; padding: 4px 2px; font-size: 11px;
  border-radius: 4px; cursor: pointer; position: relative;
  &.other-month { color: var(--text-secondary); opacity: 0.4; }
  &.is-today { background: var(--accent-color); color: #fff; border-radius: 50%; }
  &.has-event { background: var(--header-bg); }
  &:hover { background: var(--header-bg); }
}
.event-dot {
  width: 4px; height: 4px; border-radius: 50%;
  background: var(--accent-color);
  position: absolute; bottom: 2px; left: 50%; transform: translateX(-50%);
}
.event-list { border-top: 1px solid var(--border-color); padding-top: 8px; max-height: 120px; overflow-y: auto; }
.event-item {
  display: flex; gap: 8px; padding: 4px 0; font-size: 11px;
  &.activity .event-date { color: var(--accent-color); }
  &.meeting .event-date { color: #ffd700; }
}
.event-date { color: var(--text-secondary); min-width: 40px; }
.event-title { color: var(--text-primary); }
</style>
```

## 主题变量支持 (theme prop)

### 主题值

| 主题 | panelBg | borderColor | textPrimary | textSecondary | accentColor | headerBg |
|------|---------|-------------|-------------|---------------|-------------|----------|
| techBlue | rgba(13,25,41,0.85) | rgba(0,212,255,0.18) | #ffffff | rgba(255,255,255,0.7) | #00d4ff | rgba(0,212,255,0.08) |
| partyRed | rgba(30,10,10,0.85) | rgba(220,50,50,0.18) | #ffffff | rgba(255,255,255,0.7) | #dc3232 | rgba(220,50,50,0.08) |
| lightBusiness | rgba(255,255,255,0.92) | rgba(0,100,200,0.12) | #333333 | rgba(0,0,0,0.5) | #0078d4 | rgba(0,100,200,0.06) |
| ecoGreen | rgba(10,30,50,0.85) | rgba(0,180,150,0.18) | #ffffff | rgba(255,255,255,0.7) | #00b496 | rgba(0,180,150,0.08) |

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
    panelBg: 'rgba(13,25,41,0.85)',
    borderColor: 'rgba(0,212,255,0.18)',
    textPrimary: '#ffffff',
    textSecondary: 'rgba(255,255,255,0.7)',
    accentColor: '#00d4ff',
    headerBg: 'rgba(0,212,255,0.08)',
  },
  partyRed: {
    panelBg: 'rgba(30,10,10,0.85)',
    borderColor: 'rgba(220,50,50,0.18)',
    textPrimary: '#ffffff',
    textSecondary: 'rgba(255,255,255,0.7)',
    accentColor: '#dc3232',
    headerBg: 'rgba(220,50,50,0.08)',
  },
  lightBusiness: {
    panelBg: 'rgba(255,255,255,0.92)',
    borderColor: 'rgba(0,100,200,0.12)',
    textPrimary: '#333333',
    textSecondary: 'rgba(0,0,0,0.5)',
    accentColor: '#0078d4',
    headerBg: 'rgba(0,100,200,0.06)',
  },
}
```
