output "cloudfront_domain" {
  value = aws_cloudfront_distribution.portfolio.domain_name
}

output "api_gateway_url" {
  value = "${aws_api_gateway_deployment.prod.invoke_url}/prod"
}

output "lambda_function_arn" {
  value = aws_lambda_function.visitor_counter.arn
}

output "dynamodb_table_name" {
  value = aws_dynamodb_table.visitor_counter.name
}