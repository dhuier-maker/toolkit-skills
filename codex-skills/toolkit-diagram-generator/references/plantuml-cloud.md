# Cloud Architecture Diagram Reference

**Engine**: PlantUML | **Code Fence**: ```plantuml | **Shared Rules**: [plantuml-basics.md](plantuml-basics.md)

## Quick Start

Choose cloud provider → Declare stencil icons → Group into VPC/region zones → Connect with arrow syntax → Wrap in ```plantuml fence.

## Cloud Stencil Families

| Family | Prefix | Typical Icons |
|--------|--------|---------------|
| AWS | `mxgraph.aws4.*` | `lambda_function`, `ec2`, `rds_instance`, `s3`, `api_gateway`, `cloudfront`, `dynamodb` |
| Azure | `mxgraph.azure.*` | `virtual_machine`, `azure_load_balancer`, `sql_database`, `azure_active_directory`, `storage` |
| GCP | `mxgraph.gcp2.*` | `compute_engine_2`, `cloud`, `process`, `repository`, `cloud_monitoring` |
| Alibaba | `mxgraph.alibaba_cloud.*` | `ecs_elastic_compute_service`, `slb_server_load_balancer_01`, `polardb`, `oss_object_storage_service` |
| IBM | `mxgraph.ibm_cloud.*` | `ibm-cloud--kubernetes-service`, `load-balancer--application`, `database--postgresql` |
| Kubernetes | `mxgraph.kubernetes.*` | `pod`, `svc`, `deploy`, `ing`, `sts`, `pvc`, `cm`, `secret` |
| OpenStack | `mxgraph.openstack.*` | `nova_server`, `neutron_router`, `cinder_volume`, `swift_container` |

## Cloud Architecture Types

| Type | Purpose | Key Stencils |
|------|---------|--------------|
| AWS Basic | Standard web app on AWS | `mxgraph.aws4.*` |
| AWS Serverless | Event-driven serverless | `mxgraph.aws4.*` |
| Azure Hybrid | Hybrid network on Azure | `mxgraph.azure.*` |
| GCP Data | Log processing on GCP | `mxgraph.gcp2.*` |
| Kubernetes | Microservices on K8s | `mxgraph.kubernetes.*` |

## Quick Example

```plantuml
@startuml
left to right direction
mxgraph.aws4.users "Users" as users
mxgraph.aws4.cloudfront "CloudFront" as cf
mxgraph.aws4.application_load_balancer "ALB" as alb

rectangle "VPC" {
  mxgraph.aws4.ec2 "EC2" as ec2
  mxgraph.aws4.rds_instance "RDS" as rds
}

users --> cf
cf --> alb
alb --> ec2
ec2 --> rds
@enduml
```

## Examples

See [examples/cloud/](../examples/cloud/) for complete toolkit-diagram-generator examples.
