# 渐变色选择器配置面板 (GradientPicker)

完整参考：`references/config-panel-templates.md`

## 功能

提供渐变色配置控件，支持渐变方向（x/y/x2/y2）和多个渐变色节点配置。适用于柱状图渐变、背景渐变等复杂颜色配置。

## 模板代码

```vue
<template>
  <CommonLayout title="渐变颜色">
    <template v-slot:content>
      <CommonContent>
        <template v-slot:content-detail>
          <div class="gradient-config">
            <!-- 渐变方向 -->
            <div class="config-item">
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

            <!-- 渐变色节点 -->
            <div class="config-item">
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

<script setup>
import { inject, ref, watch } from 'vue';
import CommonLayout from '@/pages/digital/digital-setting/components/common/CommonLayout.vue';
import CommonContent from '@/pages/digital/digital-setting/components/common/CommonContent.vue';

// inject 和双向绑定逻辑
const addStop = () => {
  gradient.value.colorStops.push({ offset: 0, color: '#ffffff' });
};

const removeStop = (index) => {
  gradient.value.colorStops.splice(index, 1);
};
</script>
```

## 使用方式

适用于需要配置线性渐变的属性（如柱状图柱体颜色、背景色）。

完整渐变色选择器代码请参考 `references/config-panel-templates.md`。