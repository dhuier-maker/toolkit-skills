# 选择器配置面板 (Select)

完整参考：`references/config-panel-templates.md` 和 `references/component-templates.md` 第十节

## 功能

提供下拉选择控件，支持预定义选项列表。适用于图表方向、饼图类型、主题选择等枚举值配置。

## 模板代码

```vue
<template>
  <CommonLayout title="选项配置">
    <template v-slot:content>
      <CommonContent>
        <template v-slot:content-detail>
          <el-select v-model="localValue" style="width: 100%">
            <el-option
              v-for="item in options"
              :key="item.value"
              :label="item.label"
              :value="item.value"
            />
          </el-select>
        </template>
      </CommonContent>
    </template>
  </CommonLayout>
</template>

<script setup>
import { inject, ref, watch } from 'vue';
import CommonLayout from '@/pages/digital/digital-setting/components/common/CommonLayout.vue';
import CommonContent from '@/pages/digital/digital-setting/components/common/CommonContent.vue';

const props = defineProps({
  title: { type: String, default: '选项配置' },
  options: { type: Array, default: () => [] },
  injectKey: { type: String, required: true },
});

const { [props.injectKey]: value, [`set${props.injectKey.charAt(0).toUpperCase() + props.injectKey.slice(1)}`]: setValue } = inject(props.injectKey);
const localValue = ref(value.value);

watch(() => value.value, (val) => { localValue.value = val; }, { immediate: true });
watch(localValue, (val) => { setValue(val); });
</script>
```

## 使用方式

在 Props 定义中引用：

```javascript
chartOrientation: {
  type: String,
  default: 'vertical',
  desc: '图表方向',
  name: '图表方向',
  groupKey: 'style',
  groupName: '样式配置',
  sort: 2,
  configurationTemplate: () => import('./components/ChartOrientation.vue'),
},
```

创建 `components/ChartOrientation.vue` 时传入 options：

```javascript
const options = [
  { label: '垂直', value: 'vertical' },
  { label: '水平', value: 'horizontal' },
];
```

## 配套：开关配置 (SwitchOption)

对于布尔型配置，可以使用 el-switch：

```vue
<template>
  <CommonLayout :title="title">
    <template v-slot:content>
      <CommonContent>
        <template v-slot:content-detail>
          <el-switch v-model="localValue" />
        </template>
      </CommonContent>
    </template>
  </CommonLayout>
</template>
```

## 完整参考

完整选择器代码请参考 `references/config-panel-templates.md`。