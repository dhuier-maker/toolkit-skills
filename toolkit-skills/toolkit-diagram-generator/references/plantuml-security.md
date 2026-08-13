# Security Architecture Diagram Reference

**Engine**: PlantUML | **Code Fence**: ```plantuml | **Shared Rules**: [plantuml-basics.md](plantuml-basics.md)

## Quick Start

Define trust boundaries → Place identity/encryption/firewall icons → Connect with access flows → Group into security zones → Wrap in ```plantuml fence.

## Identity & Access Stencils

| Category | Stencils | Purpose |
|----------|----------|---------|
| IAM | `identity_and_access_management`, `identity_access_management_iam_roles_anywhere` | Identity policies & roles |
| SSO/Directory | `cognito`, `ad_connector`, `directory_service`, `cloud_directory` | User authentication & federation |
| STS | `sts`, `sts_alternate` | Temporary security credentials |
| Organizations | `organizations`, `organizations_account`, `organizations_organizational_unit` | Multi-account governance |

## Encryption & Secrets Stencils

| Category | Stencils | Purpose |
|----------|----------|---------|
| KMS | `key_management_service`, `key_management_service_external_key_store` | Key management & encryption |
| Secrets | `secrets_manager` | Secrets rotation & storage |
| Certificates | `certificate_manager`, `private_certificate_authority` | TLS certificate lifecycle |
| HSM | `cloudhsm` | Hardware security module |
| Encryption | `encrypted_data` | Encrypted data at rest |

## Network Security Stencils

| Category | Stencils | Purpose |
|----------|----------|---------|
| Firewall | `network_firewall`, `network_firewall_endpoints`, `firewall_manager` | Network traffic filtering |
| WAF | `generic_firewall` | Web application firewall |
| Shield | `shield`, `shield_shield_advanced`, `shield2` | DDoS protection |
| Security Group | `security_group`, `group_security_group` | Instance-level firewall |

## Threat Detection & Compliance Stencils

| Category | Stencils | Purpose |
|----------|----------|---------|
| Detection | `guardduty`, `detective`, `inspector` | Threat detection & investigation |
| Data Protection | `macie` | Sensitive data discovery |
| Compliance | `security_hub`, `security_hub_finding`, `audit_manager`, `config` | Compliance posture & audit |
| Logging | `cloudtrail`, `cloudtrail_cloudtrail_lake`, `security_lake` | Audit trail & log aggregation |

## Examples

See [examples/security/](../examples/security/) for complete toolkit-diagram-generator examples.
