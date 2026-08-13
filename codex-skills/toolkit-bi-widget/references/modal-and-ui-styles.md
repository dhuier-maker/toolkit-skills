# 弹窗样式模板

```scss
// 详情弹窗样式
.detail-panel {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: min(400px, 90vw);
  max-height: 70vh;
  background: linear-gradient(135deg, rgba(13, 25, 41, 0.98) 0%, rgba(10, 14, 26, 0.98) 100%);
  border: 1px solid rgba(0, 212, 255, 0.18);
  border-radius: 8px;
  z-index: 10000;
  display: flex;
  flex-direction: column;
  overflow: hidden;
}

.detail-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 14px 16px;
  background: rgba(0, 212, 255, 0.08);
  border-bottom: 1px solid rgba(0, 212, 255, 0.12);
}

.detail-content {
  flex: 1;
  overflow-y: auto;
  padding: 16px;

  // 自定义滚动条
  &::-webkit-scrollbar {
    width: 4px;
  }
  &::-webkit-scrollbar-track {
    background: rgba(0, 20, 40, 0.4);
    border-radius: 2px;
  }
  &::-webkit-scrollbar-thumb {
    background: rgba(0, 212, 255, 0.3);
    border-radius: 2px;
  }
}
```
