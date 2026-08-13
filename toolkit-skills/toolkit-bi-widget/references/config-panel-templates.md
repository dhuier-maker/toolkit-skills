## 四、配置面板组件规范

### 4.1 基本结构

配置面板组件用于在可视化平台中提供可视化的属性配置界面。

```vue
<template>
  <CommonLayout title="配置项名称">
    <template v-slot:content>
      <CommonContent>
        <template v-slot:content-detail>
          <!-- 配置内容区域 -->
          <div class="config-item">
            <div class="label">配置项标签</div>
            <el-input-number
              v-model="localValue"
              :min="minValue"
              :max="maxValue"
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

// 通过 inject 获取配置值和更新函数
// 命名规范：{ propName, setPropName }
const { propName, setPropName } = inject('propName');

const localValue = ref(propName.value);
let isUpdating = false;

// 监听外部值变化
watch(() => propName.value, (val) => {
  if (!isUpdating) {
    localValue.value = val;
  }
}, { immediate: true });

// 监听本地值变化并同步
watch(localValue, (val) => {
  if (!isUpdating) {
    isUpdating = true;
    setPropName(val);
    setTimeout(() => { isUpdating = false; }, 0);
  }
});

const handleChange = (val) => {
  setPropName(val);
};
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

### 4.2 常用配置面板组件模板

#### 数值配置
```vue
<template>
  <CommonLayout title="数值配置">
    <template v-slot:content>
      <CommonContent>
        <template v-slot:content-detail>
          <div class="mbs-4">
            <div style="margin-bottom: 8px">数值范围</div>
            <el-input-number
              v-model="localValue"
              :min="min"
              :max="max"
              :step="step"
              style="width: 100%"
            />
          </div>
        </template>
      </CommonContent>
    </template>
  </CommonLayout>
</template>
```

#### 颜色配置
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
```

#### 渐变颜色配置
```vue
<template>
  <CommonLayout title="渐变颜色">
    <template v-slot:content>
      <CommonContent>
        <template v-slot:content-detail>
          <div class="gradient-config">
            <div class="mbs-4">
              <div style="margin-bottom: 8px">渐变方向</div>
              <el-row :gutter="8">
                <el-col :span="12">
                  <el-input-number v-model="gradient.x" :controls="false" :min="0" :max="1" :step="0.1" style="width: 100%">
                    <template #prefix>X1:</template>
                  </el-input-number>
                </el-col>
                <el-col :span="12">
                  <el-input-number v-model="gradient.y" :controls="false" :min="0" :max="1" :step="0.1" style="width: 100%">
                    <template #prefix>Y1:</template>
                  </el-input-number>
                </el-col>
              </el-row>
            </div>
            <div class="mbs-4">
              <div style="margin-bottom: 8px">渐变色节点</div>
              <div v-for="(stop, index) in gradient.colorStops" :key="index" class="gradient-stop">
                <el-row :gutter="8" align="middle">
                  <el-col :span="8">
                    <el-input-number v-model="stop.offset" :controls="false" :min="0" :max="1" :step="0.1" style="width: 100%" />
                  </el-col>
                  <el-col :span="12">
                    <el-color-picker v-model="stop.color" show-alpha />
                  </el-col>
                  <el-col :span="4">
                    <el-button v-if="gradient.colorStops.length > 2" type="danger" size="small" text @click="removeStop(index)">删</el-button>
                  </el-col>
                </el-row>
              </div>
              <el-button size="small" @click="addStop" style="margin-top: 8px">添加渐变点</el-button>
            </div>
          </div>
        </template>
      </CommonContent>
    </template>
  </CommonLayout>
</template>
```

#### 选择器配置
```vue
<template>
  <CommonLayout title="选项配置">
    <template v-slot:content>
      <CommonContent>
        <template v-slot:content-detail>
          <el-select v-model="localValue" style="width: 100%">
            <el-option v-for="item in options" :key="item.value" :label="item.label" :value="item.value" />
          </el-select>
        </template>
      </CommonContent>
    </template>
  </CommonLayout>
</template>

<script setup>
const options = [
  { label: '选项一', value: 'option1' },
  { label: '选项二', value: 'option2' },
];
</script>
```

