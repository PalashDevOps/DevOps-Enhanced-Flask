provider "aws" {
  region = "your-aws-region"
}

resource "aws_s3_bucket" "my_bucket" {
  bucket = "your-s3-bucket-name"
  
}

resource "aws_db_instance" "my_db_instance" {
  identifier           = "my-db-instance"
  allocated_storage    = 20
  storage_type         = "gp2"
  engine               = "mysql"
  engine_version       = "5.7"
  instance_class       = "db.t2.micro"
  username             = "your-db-user"
  password             = "your-db-password"
  parameter_group_name = "default.mysql5.7"
}

output "rds_endpoint" {
  value = aws_db_instance.my_db_instance.endpoint
}
