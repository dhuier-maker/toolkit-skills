# 进度条模板 (Progress Bar)

完整参考：`references/component-templates.md` 第三节

## 功能介绍

方块式进度条排名组件，每个排名项包含排名图标、名称、横向方块进度条和数值。支持动画播放，适用于需要突出排名对比的数据展示。

## Props 定义

### 数据配置

```javascript
dynamicData: {
  type: Array,
  default: () => [
    { label: '项目A', value: 9970, rowNum: 1, percent: '90%' },
    { label: '项目B', value: 8656, rowNum: 2, percent: '77%' },
    { label: '项目C', value: 8519, rowNum: 3, percent: '75%' },
  ],
  desc: i18n.global.t('dataSpecification'),
  name: i18n.global.t('displayContent'),
  groupKey: 'data',
  groupName: i18n.global.t('dataConfiguration'),
  useDynamic: true,
  sort: 1,
},
```

### 样式配置

| 属性名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| cubeColor | String | '#01AFFF' | 方块颜色 |
| cubeCount | Number | 25 | 方块总数 |
| cubeSize | Number | 6 | 方块尺寸 |
| marginBottom | Number | 14 | 项间距 |
| openAnimate | Boolean | true | 开启动画 |
| animateDuration | Number | 5000 | 动画时长ms |

## 核心逻辑

```javascript
// 计算当前项覆盖的方块数
const getCubeStyle = (index, data) => {
  const percent = parseFloat(data.percent) / 100;
  const nowCubeCount = Math.floor(props.cubeCount * percent);
  let background = 'RGBA(255,255,255,.0)';
  if (index <= nowCubeCount) {
    background = props.cubeColor;
  }
  return {
    width: props.cubeSize * 2 + 'px',
    transform: 'skew(45deg)',
    background,
  };
};
```

## 完整代码

完整进度条代码请参考 `references/component-templates.md` 第三节中的 index.vue。
