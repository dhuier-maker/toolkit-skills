# 颜色选择器配置面板 (ColorPicker)

完整参考：`references/config-panel-templates.md` 和 `references/component-templates.md` 第十节

## 功能

提供颜色选择控件，支持透明度（Alpha）选择。适用于文字颜色、背景色、边框颜色等颜色配置。

## 模板代码

```vue
<template>
  <CommonLayout title="颜色配置">
    <template v-slot:content>
      <CommonContent>
        <template v-slot:content-detail>
          <el-color-picker v-model="localValue" show-alpha />
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
  injectKey: { type: String, required: true },
});

const { [props.injectKey]: colorValue, [`set${props.injectKey.charAt(0).toUpperCase() + props.injectKey.slice(1)}`]: setColorValue } = inject(props.injectKey);
const localValue = ref(colorValue.value);

watch(() => colorValue.value, (val) => { localValue.value = val; }, { immediate: true });
watch(localValue, (val) => { setColorValue(val); });
</script>
```

## 使用方式

在 Props 定义中引用：

```javascript
fontColor: {
  type: String,
  default: '#ffffff',
  desc: '字体颜色',
  name: '字体颜色',
  groupKey: 'style',
  groupName: '样式配置',
  sort: 3,
  configurationTemplate: () => import('./components/FontColor.vue'),
},
```

## 完整参考

完整颜色选择器代码请参考 `references/config-panel-templates.md`。