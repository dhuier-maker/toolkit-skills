# UML Diagram Reference

**Engine**: PlantUML | **Code Fence**: ```plantuml | **Shared Rules**: [plantuml-basics.md](plantuml-basics.md)

## Diagram Types

| Type | Purpose | Key Syntax |
|------|---------|------------|
| Class | Class structure and relationships | `class`, `interface`, `<\|--` |
| Sequence | Message interactions over time | `participant`, `->`, `-->` |
| Activity | Workflow and process flow | `start`, `:action;`, `if/else` |
| Swimlane Activity | Multi-role activity with swimlanes | `\|Lane\|`, `:action;` |
| State Machine | Object lifecycle states | `state`, `[*] -->` |
| Component | System component organization | `component`, `[name]`, `interface` |
| Use Case | User-system interactions | `actor`, `usecase`, `(name)` |
| Deployment | Physical deployment architecture | `node`, `artifact`, `database` |
| Object | Runtime object snapshot | `object "name" as id` |
| Package | Module organization | `package "name"` |
| Communication | Object collaboration | Numbered messages with sequence syntax |
| Composite Structure | Internal class structure | `component` with nested `port` |
| Interaction Overview | Activity + sequence combination | `group`, `ref over` |
| Profile | UML extension mechanisms | `<<stereotype>>` labels |

## Key Syntax

- Use standard PlantUML keywords: `class`, `interface`, `abstract`, `enum`, `actor`, `participant`, `component`, `node`, `database`, `package`
- Relationships: `-->`, `<|--` (inheritance), `*--` (composition), `o--` (aggregation), `..>` (dependency), `..|>` (implementation)
- Use `skinparam` for global styling and colors
- Use `#color` on individual elements for specific colors
- Notes: `note left of`, `note right of`, `note over`, or standalone `note "text" as N`

## Mxgraph Stencil Icons

draw-uml supports 9500+ mxgraph stencil icons via `mxgraph.*` syntax. Default colors are applied automatically.

**Full stencil reference**: See [stencils/README.md](../stencils/README.md)

### Examples

```plantuml
@startuml
mxgraph.aws4.lambda "Lambda\nFunction" as fn
mxgraph.aws4.api_gateway "API GW" as gw
mxgraph.aws4.dynamodb "DynamoDB" as db

gw --> fn
fn --> db
@enduml
```

```plantuml
@startuml
mxgraph.kubernetes.ing "Ingress" as ing
mxgraph.kubernetes.svc "Service" as svc
mxgraph.kubernetes.pod "Pod" as pod
mxgraph.kubernetes.deploy "Deployment" as deploy

ing --> svc
@enduml
```

## Examples

See [examples/uml/](../examples/uml/) for complete toolkit-diagram-generator examples:
- [class-diagram.md](../examples/uml/class-diagram.md)
- [sequence-diagram.md](../examples/uml/sequence-diagram.md)
- [activity-diagram.md](../examples/uml/activity-diagram.md)
- [state-machine-diagram.md](../examples/uml/state-machine-diagram.md)
- [component-diagram.md](../examples/uml/component-diagram.md)
- [use-case-diagram.md](../examples/uml/use-case-diagram.md)
- [deployment-diagram.md](../examples/uml/deployment-diagram.md)
