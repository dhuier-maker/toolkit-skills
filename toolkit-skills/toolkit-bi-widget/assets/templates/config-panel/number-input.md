# 数值输入配置面板 (NumberInput)

完整参考：`references/config-panel-templates.md` 和 `references/component-templates.md` 第十节

## 功能

提供数值输入控件，支持 min/max 范围限制、step 步进。适用于宽度、大小、间距等数值配置。

## 模板代码

```vue
<template>
  <CommonLayout title="数值配置">
    <template v-slot:content>
      <CommonContent>
        <template v-slot:content-detail>
          <div class="config-item">
            <div class="label">数值范围</div>
            <el-input-number
              v-model="localValue"
              :min="min"
              :max="max"
              :step="step"
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

const props = defineProps({
  title: { type: String, default: '数值配置' },
  min: { type: Number, default: 0 },
  max: { type: Number, default: 100 },
  step: { type: Number, default: 1 },
  injectKey: { type: String, required: true },
});

// 动态 inject
const injectKey = props.injectKey;
const setKey = 'set' + injectKey.charAt(0).toUpperCase() + injectKey.slice(1);
const { [injectKey]: value } = inject(injectKey);
const { [setKey]: setValue } = inject(injectKey);

// 适配不同的 inject 模式
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

## 使用方式

在 Props 定义中引用：

```javascript
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
```

然后创建 `components/BarWidth.vue` 使用此模板。

## 完整参考

完整数值配置代码请参考 `references/config-panel-templates.md`。