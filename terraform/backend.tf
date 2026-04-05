terraform {
  backend "s3" {
    bucket = "hasansyed-terraform-state"
    key = "hasansyed-dev/terraform.tfstate"
    region = "us-east-2"
    encrypt = true
    dynamodb_table = "terraform-locks"
  }
}