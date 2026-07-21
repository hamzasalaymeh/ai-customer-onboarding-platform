# Infrastructure

Terraform definitions for provisioning the platform's cloud environments.

## Layout

```
terraform/
├── providers.tf              Provider configuration
├── main.tf                   Core resources (compute, database, networking)
├── variables.tf               Input variables
├── outputs.tf                  Exposed outputs
└── environments/
    ├── dev.tfvars
    └── prod.tfvars
```

## Usage

```bash
cd terraform
terraform init
terraform plan -var-file=environments/dev.tfvars
terraform apply -var-file=environments/dev.tfvars
```
