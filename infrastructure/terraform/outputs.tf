output "backend_ecr_repository_url" {
  description = "URL of the backend container image repository"
  value       = aws_ecr_repository.backend.repository_url
}

output "frontend_ecr_repository_url" {
  description = "URL of the frontend container image repository"
  value       = aws_ecr_repository.frontend.repository_url
}
