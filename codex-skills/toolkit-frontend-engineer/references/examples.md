## 代码示例

### 示例：Vue 3 列表组件

```vue
<!-- src/views/village/VillageList.vue -->
<template>
  <div class="village-list">
    <!-- 搜索栏 -->
    <div class="search-bar">
      <el-input
        v-model="searchKeyword"
        placeholder="搜索村庄名称"
        clearable
        @clear="handleSearch"
        @keyup.enter="handleSearch"
      >
        <template #prefix>
          <el-icon><Search /></el-icon>
        </template>
      </el-input>
      <el-button type="primary" @click="handleSearch">搜索</el-button>
      <el-button @click="handleReset">重置</el-button>
    </div>

    <!-- 数据表格 -->
    <el-table
      v-loading="loading"
      :data="tableData"
      stripe
      border
      @selection-change="handleSelectionChange"
    >
      <el-table-column type="selection" width="55" />
      <el-table-column prop="id" label="ID" width="80" />
      <el-table-column prop="name" label="村庄名称" min-width="150" />
      <el-table-column prop="address" label="地址" min-width="200" />
      <el-table-column prop="population" label="人口" width="100" align="center" />
      <el-table-column prop="status" label="状态" width="100" align="center">
        <template #default="{ row }">
          <el-tag :type="row.status === 1 ? 'success' : 'info'">
            {{ row.status === 1 ? '正常' : '禁用' }}
          </el-tag>
        </template>
      </el-table-column>
      <el-table-column label="操作" width="180" fixed="right">
        <template #default="{ row }">
          <el-button link type="primary" @click="handleView(row)">查看</el-button>
          <el-button link type="primary" @click="handleEdit(row)">编辑</el-button>
          <el-button link type="danger" @click="handleDelete(row)">删除</el-button>
        </template>
      </el-table-column>
    </el-table>

    <!-- 分页 -->
    <div class="pagination">
      <el-pagination
        v-model:current-page="pagination.page"
        v-model:page-size="pagination.pageSize"
        :total="pagination.total"
        :page-sizes="[10, 20, 50, 100]"
        layout="total, sizes, prev, pager, next, jumper"
        @size-change="handleSizeChange"
        @current-change="handlePageChange"
      />
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, reactive, onMounted } from 'vue'
import { ElMessage, ElMessageBox } from 'element-plus'
import type { Village } from '@/types/village'
import { getVillageList, deleteVillage } from '@/api/village'

// Props 定义
interface Props {
  title?: string
}

withDefaults(defineProps<Props>(), {
  title: '村庄列表'
})

// Emits 定义
const emit = defineEmits<{
  (e: 'view', row: Village): void
  (e: 'edit', row: Village): void
}>()

// 状态
const loading = ref(false)
const searchKeyword = ref('')
const tableData = ref<Village[]>([])
const selectedRows = ref<Village[]>([])

// 分页
const pagination = reactive({
  page: 1,
  pageSize: 10,
  total: 0
})

// 加载数据
const fetchData = async () => {
  loading.value = true
  try {
    const res = await getVillageList({
      keyword: searchKeyword.value,
      page: pagination.page,
      pageSize: pagination.pageSize
    })
    tableData.value = res.data.list
    pagination.total = res.data.total
  } catch (error) {
    ElMessage.error('加载数据失败')
  } finally {
    loading.value = false
  }
}

// 搜索
const handleSearch = () => {
  pagination.page = 1
  fetchData()
}

// 重置
const handleReset = () => {
  searchKeyword.value = ''
  handleSearch()
}

// 分页变化
const handleSizeChange = () => {
  pagination.page = 1
  fetchData()
}

const handlePageChange = () => {
  fetchData()
}

// 选择变化
const handleSelectionChange = (rows: Village[]) => {
  selectedRows.value = rows
}

// 查看
const handleView = (row: Village) => {
  emit('view', row)
}

// 编辑
const handleEdit = (row: Village) => {
  emit('edit', row)
}

// 删除
const handleDelete = async (row: Village) => {
  try {
    await ElMessageBox.confirm('确定删除该村庄吗？', '提示', {
      type: 'warning'
    })
    await deleteVillage(row.id)
    ElMessage.success('删除成功')
    fetchData()
  } catch (error) {
    if (error !== 'cancel') {
      ElMessage.error('删除失败')
    }
  }
}

// 初始化
onMounted(() => {
  fetchData()
})
</script>

<style scoped lang="scss">
.village-list {
  padding: 16px;
}

.search-bar {
  display: flex;
  gap: 12px;
  margin-bottom: 16px;

  .el-input {
    width: 300px;
  }
}

.pagination {
  display: flex;
  justify-content: flex-end;
  margin-top: 16px;
}
</style>
```

### 示例：TypeScript 类型定义

```typescript
// src/types/village.ts

export interface Village {
  id: number
  name: string
  address: string
  population: number
  status: 0 | 1
  createTime: string
  updateTime: string
}

export interface VillageQuery {
  keyword?: string
  page: number
  pageSize: number
}

export interface VillageListResponse {
  list: Village[]
  total: number
}

export interface VillageForm {
  id?: number
  name: string
  address: string
  population: number
  status: 0 | 1
}
```

### 示例：API 接口定义

```typescript
// src/api/village.ts

import request from '@/utils/request'
import type { Village, VillageQuery, VillageListResponse, VillageForm } from '@/types/village'

export const getVillageList = (params: VillageQuery) => {
  return request.get<VillageListResponse>('/village/list', { params })
}

export const getVillageDetail = (id: number) => {
  return request.get<Village>('/village/detail', { params: { id } })
}

export const addVillage = (data: VillageForm) => {
  return request.post('/village/add', data)
}

export const updateVillage = (data: VillageForm) => {
  return request.put('/village/update', data)
}

export const deleteVillage = (id: number) => {
  return request.delete('/village/delete', { params: { id } })
}
```

### 示例：React 18 计数器组件

```tsx
// src/components/Counter.tsx

import { useState, useCallback } from 'react'

interface CounterProps {
  initialCount?: number
  step?: number
  onChange?: (count: number) => void
}

export const Counter: React.FC<CounterProps> = ({
  initialCount = 0,
  step = 1,
  onChange
}) => {
  const [count, setCount] = useState(initialCount)

  const increment = useCallback(() => {
    setCount(prev => {
      const newCount = prev + step
      onChange?.(newCount)
      return newCount
    })
  }, [step, onChange])

  const decrement = useCallback(() => {
    setCount(prev => {
      const newCount = prev - step
      onChange?.(newCount)
      return newCount
    })
  }, [step, onChange])

  const reset = useCallback(() => {
    setCount(initialCount)
    onChange?.(initialCount)
  }, [initialCount, onChange])

  return (
    <div className="counter">
      <span className="counter-value">{count}</span>
      <div className="counter-buttons">
        <button onClick={decrement}>-</button>
        <button onClick={reset}>Reset</button>
        <button onClick={increment}>+</button>
      </div>
    </div>
  )
}
```

