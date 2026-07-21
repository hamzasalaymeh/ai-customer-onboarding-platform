variable "aws_region" {
  description = "AWS region to deploy into"
  type        = string
  default     = "us-east-1"
}

variable "environment" {
  description = "Deployment environment name (dev, staging, prod)"
  type        = string
}

variable "project_name" {
  description = "Name used to prefix and tag provisioned resources"
  type        = string
  default     = "ai-customer-onboarding"
}

variable "backend_image" {
  description = "Container image for the backend service"
  type        = string
  default     = ""
}

variable "frontend_image" {
  description = "Container image for the frontend service"
  type        = string
  default     = ""
}
