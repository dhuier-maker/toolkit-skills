# 交互元素模板 (UIElements)

> BI 大屏常用交互元素：搜索框（含 focus 发光）、下拉选择器、开关切换器、日期/时间选择器、面板右上角操作按钮组。

---

## 一、搜索框

### Props

| 属性 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| value | String | '' | 搜索关键词（v-model） |
| placeholder | String | '搜索…' | 占位文字 |
| size | String | 'default' | 尺寸：small/default/large |

### Vue 代码

```vue
<template>
  <div class="search-box" :class="[`search-box--${size}`]">
    <svg class="search-box__icon" viewBox="0 0 16 16" width="14" height="14">
      <circle cx="7" cy="7" r="5" fill="none" stroke="currentColor" stroke-width="1.5" />
      <line x1="11" y1="11" x2="14" y2="14" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" />
    </svg>
    <input
      class="search-box__input"
      :value="value"
      :placeholder="placeholder"
      @input="$emit('input', $event.target.value)"
      @keyup.enter="$emit('search', value)"
    />
    <span v-if="value" class="search-box__clear" @click="$emit('input', '')">&times;</span>
  </div>
</template>

<script>
export default {
  name: 'SearchBox',
  props: {
    value: { type: String, default: '' },
    placeholder: { type: String, default: '搜索…' },
    size: { type: String, default: 'default' },
  },
}
</script>
```

### CSS

```scss
.search-box {
  display: flex;
  align-items: center;
  gap: 6px;
  padding: 0 10px;
  background: rgba(var(--color-primary-rgb), 0.06);
  border: 1px solid rgba(var(--color-primary-rgb), 0.15);
  border-radius: 6px;
  transition: all var(--duration-fast) var(--ease-default);

  &--small { height: 28px; .search-box__input { font-size: 11px; } }
  &--default { height: 32px; .search-box__input { font-size: 12px; } }
  &--large { height: 36px; .search-box__input { font-size: 13px; } }

  &__icon { color: var(--color-text-muted); flex-shrink: 0; }

  &__input {
    flex: 1;
    background: transparent;
    border: none;
    outline: none;
    color: var(--color-text);
    font-family: inherit;

    &::placeholder { color: var(--color-text-muted); }
  }

  &__clear {
    color: var(--color-text-muted);
    cursor: pointer;
    font-size: 16px;
    line-height: 1;

    &:hover { color: var(--color-primary); }
  }

  /* focus 发光 */
  &:focus-within {
    border-color: var(--color-primary);
    box-shadow: 0 0 8px rgba(var(--color-primary-rgb), 0.2);
    background: rgba(var(--color-primary-rgb), 0.08);
  }
}
```

---

## 二、下拉选择器

```vue
<template>
  <div class="select-box" :class="{ 'is-open': isOpen }">
    <div class="select-box__trigger" @click="isOpen = !isOpen">
      <span class="select-box__value">{{ selectedLabel || placeholder }}</span>
      <svg class="select-box__arrow" viewBox="0 0 12 12" width="12" height="12">
        <path d="M2 4L6 8L10 4" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" />
      </svg>
    </div>
    <ul v-show="isOpen" class="select-box__dropdown">
      <li
        v-for="opt in options"
        :key="opt.value"
        class="select-box__option"
        :class="{ 'is-active': opt.value === value }"
        @click="select(opt.value)"
      >{{ opt.label }}</li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'SelectBox',
  props: {
    value: { type: [String, Number], default: '' },
    options: { type: Array, default: () => [] },
    placeholder: { type: String, default: '请选择' },
  },
  data() { return { isOpen: false } },
  computed: {
    selectedLabel() { return this.options.find(o => o.value === this.value)?.label || '' },
  },
  mounted() { document.addEventListener('click', this.onClickOutside) },
  beforeDestroy() { document.removeEventListener('click', this.onClickOutside) },
  methods: {
    select(val) { this.$emit('input', val); this.isOpen = false },
    onClickOutside(e) { if (!this.$el.contains(e.target)) this.isOpen = false },
  },
}
</script>
```

```scss
.select-box {
  position: relative;
  &__trigger {
    display: flex; align-items: center; justify-content: space-between;
    height: 32px; padding: 0 10px;
    background: rgba(var(--color-primary-rgb), 0.06);
    border: 1px solid rgba(var(--color-primary-rgb), 0.15);
    border-radius: 6px; cursor: pointer;
    transition: all var(--duration-fast) var(--ease-default);
  }
  &__value { color: var(--color-text); font-size: 12px; }
  &__arrow { color: var(--color-text-muted); transition: transform var(--duration-fast); }
  &.is-open &__arrow { transform: rotate(180deg); }
  &.is-open &__trigger { border-color: var(--color-primary); }

  &__dropdown {
    position: absolute; top: calc(100% + 4px); left: 0; right: 0;
    background: var(--bg-panel-solid); border: 1px solid rgba(var(--color-primary-rgb), 0.2);
    border-radius: 6px; z-index: var(--z-tooltip); padding: 4px 0;
    max-height: 200px; overflow-y: auto;
  }
  &__option {
    padding: 6px 10px; font-size: 12px; color: var(--color-text);
    cursor: pointer; transition: background var(--duration-fast);
    &:hover { background: rgba(var(--color-primary-rgb), 0.08); }
    &.is-active { color: var(--color-primary); }
  }
}
```

---

## 三、开关切换器

```vue
<template>
  <button
    class="switch-toggle"
    :class="{ 'is-active': value }"
    @click="$emit('input', !value)"
  >
    <span class="switch-toggle__knob" />
  </button>
</template>

<script>
export default {
  name: 'SwitchToggle',
  props: { value: { type: Boolean, default: false } },
}
</script>
```

```scss
.switch-toggle {
  position: relative;
  width: 36px; height: 20px;
  background: rgba(255, 255, 255, 0.1);
  border: 1px solid rgba(var(--color-primary-rgb), 0.2);
  border-radius: 10px; cursor: pointer;
  transition: all var(--duration-fast) var(--ease-default);

  &__knob {
    position: absolute; top: 2px; left: 2px;
    width: 14px; height: 14px; border-radius: 50%;
    background: var(--color-text-muted);
    transition: all var(--duration-fast) var(--ease-default);
  }

  &.is-active {
    background: rgba(var(--color-primary-rgb), 0.2);
    border-color: var(--color-primary);

    .switch-toggle__knob {
      left: 18px;
      background: var(--color-primary);
    }
  }
}
```

---

## 四、面板右上角操作按钮组

```vue
<template>
  <div class="panel-actions">
    <button v-for="action in actions" :key="action.key"
      class="panel-actions__btn"
      :title="action.label"
      @click="$emit('action', action.key)"
    >
      <span v-html="action.icon" />
    </button>
  </div>
</template>

<script>
export default {
  name: 'PanelActions',
  props: {
    actions: { type: Array, default: () => [
      { key: 'refresh', label: '刷新', icon: '↻' },
      { key: 'fullscreen', label: '全屏', icon: '⤢' },
      { key: 'close', label: '关闭', icon: '✕' },
    ] },
  },
}
</script>
```

```scss
.panel-actions {
  display: flex; gap: 4px;

  &__btn {
    width: 24px; height: 24px;
    display: flex; align-items: center; justify-content: center;
    background: transparent; border: none;
    color: var(--color-text-muted); font-size: 14px;
    border-radius: 4px; cursor: pointer;
    transition: all var(--duration-fast) var(--ease-default);

    &:hover {
      color: var(--color-primary);
      background: rgba(var(--color-primary-rgb), 0.1);
    }
  }
}
```

---

## 五、日期/时间选择器

使用 Element UI 的 `el-date-picker`，仅提供主题适配样式：

```scss
// Element UI DatePicker 主题覆盖
.el-date-editor {
  .el-input__inner {
    background: rgba(var(--color-primary-rgb), 0.06) !important;
    border-color: rgba(var(--color-primary-rgb), 0.15) !important;
    color: var(--color-text) !important;
    height: 32px;

    &::placeholder { color: var(--color-text-muted) !important; }
  }

  .el-input__prefix,
  .el-input__suffix { color: var(--color-text-muted) !important; }

  &.is-active .el-input__inner {
    border-color: var(--color-primary) !important;
    box-shadow: 0 0 8px rgba(var(--color-primary-rgb), 0.2) !important;
  }
}

// 下拉面板
.el-picker-panel {
  background: var(--bg-panel-solid) !important;
  border-color: rgba(var(--color-primary-rgb), 0.2) !important;
  color: var(--color-text) !important;
}
```
