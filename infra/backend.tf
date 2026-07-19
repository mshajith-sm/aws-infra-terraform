terraform {
    backend "s3" {
        bucket = "terraform-backend-state-ms"
        key    = "ec2-demo/terraform.tfstate"
        region = "us-east-1"
    }
}