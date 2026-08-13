# 日期时间组件模板 (DateTimeDisplay)

完整参考：`references/component-templates.md` 第八章 8.2 节

## Props 定义

### 样式配置 (groupKey: 'style', groupName: '样式配置')

| 属性名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| showDate | Boolean | true | 显示日期 |
| showTime | Boolean | true | 显示时间 |
| showWeek | Boolean | false | 显示星期 |
| dateFormat | String | 'YYYY-MM-DD' | 日期格式 |
| timeFormat | String | 'HH:mm:ss' | 时间格式 |
| fontSize | Number | 24 | 字体大小 12-72 |
| fontColor | String | '#00D9FF' | 字体颜色 |
| layout | String | 'horizontal' | 布局方向：horizontal/vertical |
| separator | String | ' ' | 分隔符 |

## 核心逻辑

```javascript
import dayjs from 'dayjs';

const updateDateTime = () => {
  const now = dayjs();
  if (props.showDate) dateText.value = now.format(props.dateFormat);
  if (props.showTime) timeText.value = now.format(props.timeFormat);
  if (props.showWeek) weekText.value = weekDays[now.day()];
};

watch(
  () => [props.showDate, props.showTime, props.showWeek, props.dateFormat, props.timeFormat],
  () => {
    clearInterval(timer.value);
    updateDateTime();
    timer.value = setInterval(updateDateTime, 1000);
  },
  { immediate: true }
);

onUnmounted(() => { clearInterval(timer.value); });
```

## 模板结构

```html
<div class="datetime-container" :data-layout="layout">
  <div v-if="showDate" class="date-text" :style="dateStyle">{{ dateText }}</div>
  <div v-if="showTime" class="time-text" :style="timeStyle">{{ timeText }}</div>
  <div v-if="showWeek" class="week-text" :style="weekStyle">{{ weekText }}</div>
</div>
```

完整日期时间组件代码请参考 `references/component-templates.md` 第八章 8.2 节。
