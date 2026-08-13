# PlantUML Shared Rules

Applies to: uml, cloud, network, security, archimate, bpmn, data-analytics, iot, mindmap

## Critical Rules

- Every toolkit-diagram-generator starts with `@startuml` and ends with `@enduml`
  (mindmap uses `@startmindmap`/`@endmindmap`)
- Always use ```plantuml or ```puml code fence. NEVER use ```text — it will NOT render as a toolkit-diagram-generator
- Use `left to right direction` for flow/architecture diagrams (data flows left→right)
- Default colors are applied automatically — no need to specify `fillColor` or `strokeColor` unless overriding
- Use `rectangle "Name" { ... }` or `package "Name" { ... }` for grouping elements
- Use `cloud "Name" { ... }` for cloud/Internet boundary shapes

## Mxgraph Stencil Syntax

```
mxgraph.<namespace>.<icon> "Label" as <alias>
mxgraph.<namespace>.<icon> "Label" as <alias> #color
mxgraph.<namespace>.<icon> <alias>
```

- `mxgraph.<namespace>.<icon>` — the stencil shape key (e.g. `mxgraph.aws4.lambda`)
- `"Label"` — display text (quoted if contains spaces, unquoted for single word)
- `as <alias>` — identifier for use in relationships
- `#color` — optional override color (e.g. `#FF6600`, `#LightBlue`)

## Connection Types

| Syntax | Meaning | Use Case |
|--------|---------|----------|
| `A --> B` | Solid arrow | Sync flow / data flow / API call |
| `A ..> B` | Dashed arrow | Async / event / audit / streaming |
| `A -- B` | Solid line, no arrow | Physical / bidirectional link |
| `A --> B : "label"` | Labeled connection | Describe the flow or protocol |

## Stencil Reference

Full stencil reference with 9500+ icons: See [stencils/README.md](../stencils/README.md)

Common stencil families:

| Family | Prefix | Typical Use |
|--------|--------|-------------|
| AWS | `mxgraph.aws4.*` | Lambda, EC2, RDS, S3, API Gateway, CloudFront, DynamoDB |
| Azure | `mxgraph.azure.*` | Virtual Machine, Load Balancer, SQL Database, AD, Storage |
| GCP | `mxgraph.gcp2.*` | Compute Engine, Cloud SQL, BigQuery, Cloud Run |
| Alibaba | `mxgraph.alibaba_cloud.*` | ECS, SLB, PolarDB, OSS |
| Kubernetes | `mxgraph.kubernetes.*` | Pod, Service, Deployment, Ingress, PVC, ConfigMap |
| Cisco | `mxgraph.cisco.*` | Router, Switch, Firewall, Server |
| Networks | `mxgraph.networks.*` | Switch, Router, Firewall, Server, PC, Laptop |
| BPMN | `mxgraph.bpmn.*` | Start/End Event, Gateway, User/Service Task |
| EIP | `mxgraph.eip.*` | Enterprise Integration Patterns |
| Lean | `mxgraph.lean_mapping.*` | Value Stream Mapping symbols |
