# DevOps-Enhanced-Flask
This repository contains an enhanced DevOps project showcasing a Flask web application with integrated AWS services, Terraform for infrastructure as code, and Jenkins for continuous integration and continuous deployment (CI/CD) pipelines.
# My Enhanced DevOps Project

This project is an enhanced version that demonstrates a Flask web application deployed using Docker, Jenkins, AWS, Terraform, and Kubernetes with Helm.

## Prerequisites

Before you begin, make sure you have the following tools installed on your machine:

- Docker
- Jenkins
- AWS CLI
- Terraform
- Helm

## How to Run Locally

1. Build the Docker image:

   ```bash
   docker build -t my-devops-app .
2. Run the Docker container:
   ```bash
   docker run -p 5000:5000 my-devops-app
3. Access the application at http://localhost:5000.

## CI/CD Pipeline

  - The Jenkinsfile in this project defines a comprehensive CI/CD pipeline with the following stages:

      - Build: Builds the Docker image.
      - Test: Executes unit tests within a temporary container.
      - Push to Registry: Pushes the Docker image to a container registry.
      - Terraform Apply: Applies the Terraform configuration to create AWS resources.
      - Deploy to Kubernetes: Deploys the application to a Kubernetes cluster using Helm.
      - 
      For more information on each stage, refer to the Jenkinsfile.

## AWS Resources

The terraform directory contains Terraform configuration to create the following AWS resources:

 - S3 Bucket
 - RDS Instance (MySQL)
  
To apply the Terraform configuration, run the following commands:

```bash
cd terraform
terraform init
terraform apply -auto-approve
```
## Helm Chart
The helm-chart directory contains Helm charts for deploying the application to Kubernetes. 

Customize the values.yaml file as needed.

To deploy the application using Helm:
```
helm upgrade --install my-devops-app ./helm-chart
