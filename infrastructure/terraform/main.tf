locals {
  name_prefix = "${var.project_name}-${var.environment}"

  common_tags = {
    Project     = var.project_name
    Environment = var.environment
    ManagedBy   = "terraform"
  }
}

# Placeholder for core infrastructure resources (VPC, database, container
# platform, etc). Flesh out per environment as the platform's cloud
# footprint is defined.

resource "aws_ecr_repository" "backend" {
  name = "${local.name_prefix}-backend"
  tags = local.common_tags
}

resource "aws_ecr_repository" "frontend" {
  name = "${local.name_prefix}-frontend"
  tags = local.common_tags
}
