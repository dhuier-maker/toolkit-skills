# Vega / Vega-Lite Data Chart Reference

**Engine**: Vega-Lite (declarative) or Vega (programmatic) | **Code Fence**: ```vega-lite or ```vega

## Quick Start

Structure data as array of objects → Choose mark type → Map encodings (x, y, color, size) to fields → Set data types → Wrap in ```vega-lite or ```vega fence.

**Use Vega-Lite for 90% of charts; Vega only for radar, word cloud, force-directed.**

## Critical Syntax Rules

### Rule 1: Always Include Schema
```json
"$schema": "https://vega.github.io/schema/vega-lite/v5.json"
```

### Rule 2: Valid JSON Only
```
❌ {field: "x",}     → Trailing comma, unquoted key
✅ {"field": "x"}    → Proper JSON
```

### Rule 3: Field Names Must Match Data (Case-Sensitive)
```
❌ "field": "Category"  when data has "category"
✅ "field": "category"  → Case-sensitive match
```

### Rule 4: Type Must Be Valid
```
✅ quantitative | nominal | ordinal | temporal
❌ numeric | string | date
```

## Common Pitfalls

| Issue | Solution |
|-------|----------|
| Chart not rendering | Check JSON validity, verify `$schema` |
| Data not showing | Field names must match exactly |
| Wrong chart type | Match mark to data structure |
| Colors not visible | Check color scale contrast |
| Dual-axis issues | Add `resolve: {scale: {y: "independent"}}` |

## Mark Types (Vega-Lite)

| Mark | Chart Type | Best For |
|------|-----------|----------|
| `bar` | Bar chart | Categorical comparison |
| `line` | Line chart | Trends over time |
| `point` / `circle` | Scatter plot | Correlation |
| `area` | Area chart | Cumulative trends |
| `arc` | Pie/donut chart | Part-to-whole |
| `rect` | Heatmap | Matrix values |
| `tick` | Strip plot | Distribution |

## Output Format

````markdown
```vega-lite
{
  "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
  "data": { "values": [...] },
  "mark": "bar",
  "encoding": {
    "x": {"field": "category", "type": "nominal"},
    "y": {"field": "value", "type": "quantitative"}
  }
}
```
````

## Advanced Examples

See [references/examples.md](../vega/references/examples.md) for stacked bar, grouped bar, multi-series line, area, heatmap, radar (Vega), word cloud (Vega), and interactive chart examples.
