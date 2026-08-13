# 配置面板组件模板

配置面板组件用于在可视化平台中提供可视化的属性配置界面，每个配置面板组件对应一个 Props 属性。

## 支持的模板

| 模板文件 | 说明 |
|----------|------|
| `number-input.md` | 数值输入配置面板 |
| `color-picker.md` | 颜色选择器配置面板 |
| `gradient-picker.md` | 渐变色选择器配置面板 |
| `select.md` | 下拉选择器配置面板 |

## 通用结构

所有配置面板组件使用相同的布局组件和 inject 机制：

```vue
<template>
  <CommonLayout title="配置项名称">
    <template v-slot:content>
      <CommonContent>
        <template v-slot:content-detail>
          <!-- 配置内容 -->
        </template>
      </CommonContent>
    </template>
  </CommonLayout>
</template>
```

## 依赖组件

```javascript
import CommonLayout from '@/pages/digital/digital-setting/components/common/CommonLayout.vue';
import CommonContent from '@/pages/digital/digital-setting/components/common/CommonContent.vue';
```

## 数据绑定模式

```javascript
const { propName, setPropName } = inject('propName');
const localValue = ref(propName.value);

watch(() => propName.value, (val) => { localValue.value = val; }, { immediate: true });
watch(localValue, (val) => { setPropName(val); });
```

## Props 关联

在组件的 Props 定义中通过 `configurationTemplate` 引用：

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

## 完整参考

配置面板完整规范请参考 `references/config-panel-templates.md`。