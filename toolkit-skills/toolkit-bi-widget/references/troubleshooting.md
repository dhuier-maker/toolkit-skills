## 十三、常见问题与解决方案

### 12.1 文件末尾换行符问题

**问题**：Prettier/ESLint 报错 `Insert ⏎`

**原因**：文件末尾缺少换行符

**解决方案**：
```bash
# 使用 Node.js 添加换行符
node -e "const fs=require('fs'); let c=fs.readFileSync('file.vue','utf8'); if(!c.endsWith('\n')){c+='\n'; fs.writeFileSync('file.vue',c);}"
```

**IDE 配置**：
- VS Code: 设置 `"files.insertFinalNewline": true`
- WebStorm: 编辑器 → 常规 → 保存时 → 确保文件末尾有换行符

---

### 12.2 中文字符编码问题

**问题**：中文显示乱码或编译失败

**原因**：使用 shell 命令修改文件破坏了 UTF-8 编码

**解决方案**：
- **严禁**使用 `echo`、`printf`、`sed` 等 shell 命令修改含中文的文件
- 使用 Write 工具或 Node.js `fs` 模块处理
- 检查编码：`node -e "console.log(require('fs').readFileSync('file.vue').toString().charCodeAt(0))"`

---

### 12.3 Prettier 格式化问题

**问题**：数组/对象格式化报错

**解决方案**：
```bash
# 自动格式化
npx prettier --write "src/packages/ComponentName/src/index.vue"
npx eslint --fix "src/packages/ComponentName/src/index.vue"
```

---

### 12.4 弹窗组件设计问题

**问题**：弹窗应该跟随组件，而非独立拆分

**解决方案**：弹窗集成在组件内部
```vue
<script setup>
const showDetail = ref(false);
const selectedItem = ref(null);

const handleItemClick = (item) => {
  selectedItem.value = item;
  showDetail.value = true;
  emit('item-click', item); // 同时通知父组件
};

const closeDetail = () => {
  showDetail.value = false;
  selectedItem.value = null;
};
</script>

<template>
  <!-- 主内容 -->
  <div @click="handleItemClick">...</div>

  <!-- 详情弹窗（集成在组件内） -->
  <div v-if="showDetail" class="detail-panel" @click.stop>
    <div class="detail-header">
      <span>{{ selectedItem?.name }}</span>
      <span @click="closeDetail">×</span>
    </div>
    <div class="detail-content">...</div>
  </div>
</template>
```

---

### 12.5 示例数据缺失问题

**问题**：组件默认数据为空数组，无法预览效果

**解决方案**：提供 realistic 示例数据
```javascript
dynamicData: {
  type: Array,
  default: () => [
    { id: 1, name: '示例数据1', value: 100 },
    { id: 2, name: '示例数据2', value: 200 },
  ],
  // ...
}
```

---

