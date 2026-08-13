# Network Topology Diagram Reference

**Engine**: PlantUML | **Code Fence**: ```plantuml | **Shared Rules**: [plantuml-basics.md](plantuml-basics.md)

## Quick Start

Choose topology type → Declare stencil icons for network devices → Connect with arrow syntax → Group into zones → Wrap in ```plantuml fence.

## Network Stencil Families

| Family | Prefix | Typical Icons |
|--------|--------|---------------|
| Networks | `mxgraph.networks.*` | `switch`, `router`, `firewall`, `server`, `pc`, `laptop`, `wireless_hub`, `cloud` |
| Cisco | `mxgraph.cisco.*` | `routers.router`, `switches.layer_3_switch`, `security.firewall`, `servers.fileserver` |
| Cisco 19 | `mxgraph.cisco19.*` | `nexus_9300`, `nexus_5k`, `fabric_interconnect`, `ucs_5108_blade_chassis` |
| Cisco SAFE | `mxgraph.cisco_safe.security_icons.*` | `ngfw`, `waf`, `ids`, `siem`, `nac`, `vpn`, `ddos`, `malware_sandbox` |
| Citrix | `mxgraph.citrix2.*` | `netscaler_gateway`, `storefront`, `delivery_controller`, `vda` |

## Connection Types

| Syntax | Meaning | Use Case |
|--------|---------|----------|
| `A -- B` | Solid line, no arrow | Physical Ethernet / LAN link |
| `A --> B` | Solid line with arrow | Directed traffic flow |
| `A .. B` | Dashed line, no arrow | VPN tunnel / wireless link |
| `A ..> B` | Dashed line with arrow | Directed VPN / logical flow |
| `A -- B : "label"` | Labeled connection | Link description |

## Quick Example

```plantuml
@startuml
mxgraph.networks.cloud "Internet" as inet
mxgraph.networks.firewall "Firewall" as fw
mxgraph.networks.router "Router" as rtr
mxgraph.networks.switch "Switch" as sw

rectangle "Office LAN" {
  mxgraph.networks.pc "PC 1" as pc1
  mxgraph.networks.pc "PC 2" as pc2
  mxgraph.networks.server "Server" as srv
}

inet -- fw
fw -- rtr
rtr -- sw
sw -- pc1
sw -- pc2
sw -- srv
@enduml
```

## Examples

See [examples/network/](../examples/network/) for complete toolkit-diagram-generator examples.
