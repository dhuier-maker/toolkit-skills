# JSON Canvas Reference

**Engine**: JSON Canvas | **Code Fence**: ```canvas

## Quick Start

Define nodes with `id`, `type`, `x`, `y`, `width`, `height` → Plan layout on 100px grid → Connect edges with `fromNode`/`toNode` → Apply colors (1-6) → Wrap in ```canvas fence.

Origin (0,0) at top-left, X right, Y down. Obsidian Canvas compatible.

## Structure Format

```canvas
{
  "nodes": [
    {"id": "n1", "type": "text", "text": "Node 1", "x": 0, "y": 0, "width": 120, "height": 50}
  ],
  "edges": []
}
```

## Node Types

| Type | Required Fields | Purpose |
|------|----------------|---------|
| `text` | `text` | Display custom text content |
| `file` | `file` | Reference external files |
| `link` | `url` | External URL references |
| `group` | `label` | Visual container for grouping |

## Required Node Attributes

All nodes require: `id`, `type`, `x`, `y`, `width`, `height`

## Color Presets

| Value | Color |
|-------|-------|
| `"1"` | Red |
| `"2"` | Orange |
| `"3"` | Yellow |
| `"4"` | Green |
| `"5"` | Cyan |
| `"6"` | Purple |

## Edge Connections

```json
{
  "id": "e1",
  "fromNode": "n1",
  "fromSide": "right",
  "toNode": "n2",
  "toSide": "left",
  "toEnd": "arrow"
}
```

## Coordinate System

- Origin (0,0) at top-left
- X increases to the right
- Y increases downward

## Common Pitfalls

| Issue | Solution |
|-------|----------|
| Nodes overlapping | Increase spacing (100+ px) |
| Edges not visible | Verify `fromNode`/`toNode` match node IDs |
| Invalid JSON | Check quotes and commas |
| IDs invalid | Use only a-z, A-Z, 0-9, -, _ |

## Advanced Syntax

See [references/syntax.md](../canvas/references/syntax.md) for detailed syntax and edge options.
