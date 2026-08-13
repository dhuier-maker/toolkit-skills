# 自动化测试预览与打包流程

## 自动测试预览流程

组件开发完成后，执行以下步骤：

### 步骤 1：添加组件到测试页面

修改 `src/pages/extendComponentTest/index.vue` 文件：

```javascript
// 在 import 区域添加新组件（注释其他组件）
// import TestComponent from '@/packages/OldComponent/src/index.vue';
import TestComponent from '@/packages/NewComponent/src/index.vue';
```

### 步骤 2：启动本地开发服务器

```bash
npm run serve
```

### 步骤 3：打开浏览器预览

访问 http://localhost:3000 查看组件效果

### 步骤 4：用户反馈循环

| 用户反馈 | 动作 |
|----------|------|
| "满意" / "可以" / "没问题" | 进入打包询问阶段 |
| "不满意" / "需要修改" | 根据用户意见修改组件，重新预览 |
| 具体修改意见 | 根据意见调整组件代码，刷新页面预览 |

### 打包询问与执行

用户满意后询问是否打包：
- **是**：自动执行打包命令
- **否**：返回打包命令供用户手动执行

### 自动打包（用户选择"是"）

```powershell
$env:BUILD_COMPONENTS="ComponentName"; npm run build:lib
```

打包完成后提示：
```
✅ 打包完成！
输出位置：lib/ComponentName/
├── index.js      # 组件代码
├── style.css     # 样式文件
└── ComponentName.zip # 压缩包
```

### 返回命令（用户选择"否"）

```
打包命令已准备好，你可以随时执行：

# PowerShell
$env:BUILD_COMPONENTS="ComponentName"; npm run build:lib

# 或使用预定义脚本
npm run build:lib:biheader
npm run build:lib:all

# 或交互式选择
npm run build:lib
```

### 完整自动化流程图

```
组件开发完成
    ↓
修改测试页面 import
    ↓
启动 npm run serve
    ↓
打开 http://localhost:3000
    ↓
用户预览组件效果
    ↓
┌─────────────────────────────┐
│ 用户是否满意？              │
├─────────────────────────────┤
│ 不满意 → 修改组件 → 重新预览 │
│ 满意   → 询问是否打包        │
└─────────────────────────────┘
    ↓
┌─────────────────────────────┐
│ 是否需要打包？              │
├─────────────────────────────┤
│ 是 → 自动执行打包命令        │
│ 否 → 返回打包命令给用户      │
└─────────────────────────────┘
    ↓
流程结束
```

---

## 打包流程

### 打包命令

| 命令 | 说明 |
|------|------|
| `npm run build:lib` | 交互式选择组件（多选模式） |
| `npm run build:lib:all` | 打包所有组件 |
| `npm run build:lib:biheader` | 打包 BiHeader 组件 |
| `npm run build:lib:business` | 打包 BusinessDataOverview 组件 |
| `npm run build:lib:parking` | 打包 ParkingMonitor + ParkingList |
| `npm run build:lib:ticket` | 打包 TicketSearch 组件 |
| `npm run build:lib:chart` | 打包 BusinessCategoryChart + GuideRankList |

### 自定义批量打包（PowerShell）

```powershell
$env:BUILD_COMPONENTS="BiHeader,BusinessDataOverview,ParkingMonitor"; npm run build:lib
```

### 自定义批量打包（CMD）

```cmd
set BUILD_COMPONENTS=BiHeader,BusinessDataOverview,ParkingMonitor && npm run build:lib
```

### 输出位置

打包结果输出到 `lib/` 目录：
```
lib/
├── ComponentName/
│   ├── index.js      # 组件代码
│   └── style.css     # 样式文件
└── ComponentName.zip # 压缩包
```

### 外部依赖配置

外部依赖在 `src/config/externals/default.json` 中配置，打包时会被排除：
```json
{
  "vue": "vue",
  "echarts": "echarts",
  "element-plus": "element-plus",
  "dayjs": "dayjs"
}
```

---

## 开发完成后自动格式化

```bash
# 格式化组件文件
npx prettier --write "src/packages/ComponentName/src/index.vue"
npx eslint --fix "src/packages/ComponentName/src/index.vue"

# 确保文件末尾有换行符
node -e "const fs=require('fs'); let c=fs.readFileSync('src/packages/ComponentName/src/index.vue','utf8'); if(!c.endsWith('\n')){c+='\n'; fs.writeFileSync('src/packages/ComponentName/src/index.vue',c);}"
```
