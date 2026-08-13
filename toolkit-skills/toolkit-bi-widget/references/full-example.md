## 十一、完整开发示例

### 示例：创建柱状图组件（BarChartComponent）

以下是一个完整的柱状图组件开发示例，包含所有必需文件。

#### 1. 创建目录结构

```
front/the project's visualization component library/src/packages/BarChartComponent/
├── index.js
└── src/
    ├── index.vue
    ├── components/
    │   └── BarWidth.vue
    ├── locale/
    │   ├── index.js
    │   └── lang/
    │       ├── zh-cn.json
    │       └── en.json
    └── static/
        └── img/
```

#### 2. index.js（入口文件）

```javascript
// eslint-disable-next-line
__webpack_public_path__ = window[process.env.VUE_APP_PROCESS_ENV_KEY][process.env.VUE_EXTEND_COMPONENT_PUBLIC_PATH_KEY]
import comp from './src/index.vue';
export default comp;
```

#### 3. src/index.vue（主组件）

```vue
<template>
  <div ref="chartRef" class="chart-container"></div>
</template>

<script setup>
import { markRaw, defineProps, defineExpose, ref, watch, onUnmounted, onMounted } from 'vue';
import * as echarts from 'echarts';
import i18n from './locale/index';

const props = defineProps({
  // ========== 数据配置 ==========
  chartData: {
    type: Object,
    default: () => ({
      categories: ['类别1', '类别2', '类别3'],
      values: [100, 200, 150],
    }),
    desc: i18n.global.t('dataSpecification'),
    name: i18n.global.t('displayContent'),
    groupKey: 'data',
    groupName: i18n.global.t('dataConfiguration'),
    useDynamic: true,
    sort: 1,
  },

  // ========== 样式配置 ==========
  barWidth: {
    type: Number,
    default: 30,
    desc: '柱体宽度',
    name: '柱体宽度',
    groupKey: 'style',
    groupName: '样式配置',
    sort: 2,
    min: 10,
    max: 100,
    configurationTemplate: () => import('./components/BarWidth.vue'),
  },

  barColor: {
    type: String,
    default: '#00D9FF',
    desc: '柱体颜色',
    name: '柱体颜色',
    groupKey: 'style',
    groupName: '样式配置',
    sort: 3,
  },
});

const chartRef = ref(null);
const chart = ref(null);

// 颜色转换函数
const convertColor = (colorConfig) => {
  if (typeof colorConfig === 'string') return colorConfig;
  if (colorConfig.type === 'linear') {
    return new echarts.graphic.LinearGradient(
      colorConfig.x || 0, colorConfig.y || 0,
      colorConfig.x2 || 0, colorConfig.y2 || 1,
      colorConfig.colorStops || []
    );
  }
  return colorConfig;
};

// 初始化图表
const initChart = () => {
  if (!chartRef.value) return;
  if (chart.value) chart.value.dispose();

  chart.value = markRaw(echarts.init(chartRef.value));

  const option = {
    backgroundColor: 'transparent',
    tooltip: {
      trigger: 'axis',
      axisPointer: { type: 'shadow' },
    },
    grid: {
      left: '3%', right: '4%', top: '10%', bottom: '3%',
      containLabel: true,
    },
    xAxis: {
      type: 'category',
      data: props.chartData.categories,
      axisLine: { show: false },
      axisTick: { show: false },
      axisLabel: { color: '#87ceeb' },
    },
    yAxis: {
      type: 'value',
      axisLine: { show: false },
      axisTick: { show: false },
      axisLabel: { color: '#87ceeb' },
      splitLine: { lineStyle: { color: 'rgba(0, 212, 255, 0.1)' } },
    },
    series: [{
      type: 'bar',
      data: props.chartData.values,
      barWidth: props.barWidth,
      itemStyle: {
        color: convertColor(props.barColor),
        borderRadius: [4, 4, 0, 0],
      },
    }],
  };

  chart.value.setOption(option, true);
};

// 监听配置变化
watch(
  () => [props.chartData, props.barWidth, props.barColor],
  () => { setTimeout(() => initChart(), 300); },
  { deep: true }
);

// 窗口resize处理
const handleResize = () => chart.value?.resize();

onMounted(() => {
  initChart();
  window.addEventListener('resize', handleResize);
  const resizeObserver = new ResizeObserver(() => handleResize());
  if (chartRef.value) resizeObserver.observe(chartRef.value);
});

onUnmounted(() => {
  window.removeEventListener('resize', handleResize);
  chart.value?.dispose();
});

defineExpose({ chart, initChart });
</script>

<style lang="scss" scoped>
.chart-container {
  width: 100%;
  height: 100%;
}
</style>
```

#### 4. components/BarWidth.vue（配置面板）

```vue
<template>
  <CommonLayout title="柱体宽度">
    <template v-slot:content>
      <CommonContent>
        <template v-slot:content-detail>
          <div class="config-item">
            <div class="label">宽度范围：10-100</div>
            <el-input-number
              v-model="localValue"
              :min="10"
              :max="100"
              :step="5"
              style="width: 100%"
              @change="handleChange"
            />
          </div>
        </template>
      </CommonContent>
    </template>
  </CommonLayout>
</template>

<script setup>
import { inject, ref, watch } from 'vue';
import CommonLayout from '@/pages/digital/digital-setting/components/common/CommonLayout.vue';
import CommonContent from '@/pages/digital/digital-setting/components/common/CommonContent.vue';

const { barWidth, setBarWidth } = inject('barWidth');
const localValue = ref(barWidth.value);
let isUpdating = false;

watch(() => barWidth.value, (val) => {
  if (!isUpdating) localValue.value = val;
}, { immediate: true });

watch(localValue, (val) => {
  if (!isUpdating) {
    isUpdating = true;
    setBarWidth(val);
    setTimeout(() => { isUpdating = false; }, 0);
  }
});

const handleChange = (val) => setBarWidth(val);
</script>

<style lang="scss" scoped>
.config-item {
  margin-bottom: 12px;
  .label {
    margin-bottom: 8px;
    color: #e0e0e0;
  }
}
</style>
```

#### 5. locale/index.js（国际化配置）

```javascript
import { createI18n } from 'vue-i18n';
import cn from './lang/zh-cn.json';
import en from './lang/en.json';
import languageMgt from '@/utils/langMgt';

const i18n = createI18n({
  locale: languageMgt.getLanguage(),
  legacy: false,
  globalInjection: true,
  messages: { cn, en },
});

export default i18n;
```

#### 6. locale/lang/zh-cn.json（中文）

```json
{
  "dataConfiguration": "数据配置",
  "styleConfiguration": "样式配置",
  "layout": "排版",
  "dataSpecification": "数据说明",
  "displayContent": "展示内容"
}
```

#### 7. locale/lang/en.json（英文）

```json
{
  "dataConfiguration": "Data Configuration",
  "styleConfiguration": "Style Configuration",
  "layout": "Layout",
  "dataSpecification": "Data Specification",
  "displayContent": "Display Content"
}
```

#### 8. 本地测试

```bash
cd front/the project's visualization component library
npm run serve
# 访问 http://localhost:3000 查看组件
```

#### 9. 打包上传

```bash
npm run build:lib
# 选择 BarChartComponent 进行打包
# 将 lib/BarChartComponent.zip 上传到可视化平台
```

---

### 组件调试技巧

1. **查看组件列表**：访问组件管理页面，确认组件已注册
2. **控制台日志**：在组件中添加 `console.log` 查看数据流
3. **Props 检查**：在开发者工具中查看组件的 props 配置
4. **ECharts 调试**：在浏览器控制台输入 `$0.__vue__.chart` 查看图表实例

---

