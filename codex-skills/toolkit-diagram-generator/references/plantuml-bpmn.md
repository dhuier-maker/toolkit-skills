# BPMN Business Process Diagram Reference

**Engine**: PlantUML | **Code Fence**: ```plantuml | **Shared Rules**: [plantuml-basics.md](plantuml-basics.md)

## Quick Start

Choose toolkit-diagram-generator type → Declare stencil icons for events/gateways/tasks → Group into pools/lanes → Connect with arrow syntax → Wrap in ```plantuml fence.

## BPMN Stencil Family (`mxgraph.bpmn.*`)

**Events** — Circle shapes for process triggers and outcomes:

| Icon | Meaning |
|------|---------|
| `mxgraph.bpmn.event.start` | Start Event |
| `mxgraph.bpmn.event.end` | End Event |
| `mxgraph.bpmn.event.terminateEnd` | Terminate End |
| `mxgraph.bpmn.event.timerStart` | Timer Start |
| `mxgraph.bpmn.event.timerCatching` | Timer Intermediate |
| `mxgraph.bpmn.event.messageStart` | Message Start |
| `mxgraph.bpmn.event.messageCatching` | Message Catching |
| `mxgraph.bpmn.event.messageEnd` | Message End |
| `mxgraph.bpmn.event.errorEnd` | Error End |
| `mxgraph.bpmn.event.errorBound` | Error Boundary |
| `mxgraph.bpmn.event.signalStart` | Signal Start |
| `mxgraph.bpmn.event.signalEnd` | Signal End |

**Gateways** — Diamond shapes for branching/merging:

| Icon | Meaning |
|------|---------|
| `mxgraph.bpmn.gateway2.exclusive` | Exclusive Gateway (XOR) |
| `mxgraph.bpmn.gateway2.parallel` | Parallel Gateway (AND) |
| `mxgraph.bpmn.gateway2.inclusive` | Inclusive Gateway (OR) |
| `mxgraph.bpmn.gateway2.complex` | Complex Gateway |

**Tasks** — Use `rectangle` for tasks, stencil markers for typed tasks:

| Icon | Meaning |
|------|---------|
| `mxgraph.bpmn.user_task` | User Task |
| `mxgraph.bpmn.service_task` | Service Task |
| `mxgraph.bpmn.script_task` | Script Task |
| `mxgraph.bpmn.manual_task` | Manual Task |
| `mxgraph.bpmn.business_rule_task` | Business Rule Task |

**Data** — Document-like shapes:

| Icon | Meaning |
|------|---------|
| `mxgraph.bpmn.data2.dataObject` | Data Object |
| `mxgraph.bpmn.data2.dataInput` | Data Input |
| `mxgraph.bpmn.data2.dataOutput` | Data Output |

## EIP Stencil Family (`mxgraph.eip.*`)

Enterprise Integration Pattern icons for message-based architectures. See [stencils/eip.md](../stencils/eip.md) for full list.

## Lean Mapping Stencil Family (`mxgraph.lean_mapping.*`)

Value Stream Mapping symbols. See [stencils/lean_mapping.md](../stencils/lean_mapping.md) for full list.

## Connection Types

- Sequence flows use `-->` (solid arrow)
- Message flows use `..>` (dashed arrow)

## Examples

See [examples/bpmn/](../examples/bpmn/) for complete toolkit-diagram-generator examples.
