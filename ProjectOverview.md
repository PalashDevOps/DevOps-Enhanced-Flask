# Project Overview

## Flask Web Application

The project involves a Flask web application, a simple example showcasing a "Hello DevOps World!" message.

## Key Components

### Docker

- The application is containerized using Docker, allowing for consistency and portability across different environments.

### Jenkins CI/CD Pipeline

- Jenkins is configured with a comprehensive CI/CD pipeline.
- The pipeline includes stages for building the Docker image, running tests, pushing the image to a registry, applying Terraform to create AWS resources, and deploying to Kubernetes using Helm.

### AWS Resources (Terraform)

- The `terraform` directory contains Terraform configurations for creating AWS resources:
  - S3 Bucket: Object storage for static assets.
  - RDS Instance (MySQL): Managed relational database for the application.

### Helm for Kubernetes Deployment

- The `helm-chart` directory includes Helm charts for deploying the Flask application to a Kubernetes cluster.
- Helm allows for easy configuration and management of Kubernetes deployments.

## Demo Steps

### Run Locally

1. Build and run the Docker container locally to see the "Hello DevOps World!" message at [http://localhost:5000](http://localhost:5000).

### CI/CD Pipeline

1. Push changes to the Git repository.
2. Jenkins automatically triggers the CI/CD pipeline.
3. The pipeline includes stages for building, testing, pushing to a registry, applying Terraform, and deploying to Kubernetes.

### AWS Resources

1. Terraform applies the configuration, creating AWS resources (S3 Bucket, RDS Instance) to support the application.

### Kubernetes Deployment

1. Helm deploys the application to a Kubernetes cluster, providing scalability and manageability.

### Access the Deployed Application

1. Verify the deployed application in the Kubernetes cluster.
2. Changes made locally should be reflected in the deployed version.

## Expected Outcomes

### Local Run

- You should see the "Hello DevOps World!" message when accessing [http://localhost:5000](http://localhost:5000).

### CI/CD Pipeline

- Jenkins should successfully execute each stage in the pipeline, ensuring code quality, containerization, and successful deployment.

### AWS Resources

- AWS resources (S3 Bucket, RDS Instance) should be created as defined in the Terraform configuration.

### Kubernetes Deployment

- The Flask application should be successfully deployed to the Kubernetes cluster using Helm.

## Purpose

The project is designed to showcase best practices in DevOps, demonstrating how to containerize applications, set up CI/CD pipelines, provision cloud infrastructure with Terraform, and deploy applications to Kubernetes using Helm. It provides a practical example of a Flask application with enhanced DevOps practices.
