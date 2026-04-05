variable "aws_region" {
  description = "AWS region"
  type        = string
  default     = "us-east-2"
}

variable "domain_name" {
  description = "Custom domain name"
  type        = string
  default     = "hasansyed.dev"
}

variable "acm_certificate_arn" {
  description = "ARN of ACM certificate for CloudFront (must be in us-east-1)"
  type        = string
  default = "arn:aws:acm:us-east-1:123456789012:certificate/xxxx-xxxx"
}

variable "lambda_function_name" {
  description = "Name of Lambda function"
  type        = string
  default     = "VisitorCounter"
}

variable "dynamodb_table_name" {
  description = "DynamoDB table name"
  type        = string
  default     = "VisitorCounter2.0"
}