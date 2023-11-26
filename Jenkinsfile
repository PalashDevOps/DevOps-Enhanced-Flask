pipeline {
    agent any
    
    environment {
        AWS_ACCESS_KEY_ID     = credentials('your-aws-access-key-id')
        AWS_SECRET_ACCESS_KEY = credentials('your-aws-secret-access-key')
    }

    stages {
        stage('Build') {
            steps {
                script {
                    docker.build('my-devops-app')
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    docker.image('my-devops-app').withRun('-p 5000:5000') {
                        sh 'python -m unittest discover tests'
                    }
                }
            }
        }
        stage('Push to Registry') {
            steps {
                script {
                    docker.withRegistry('https://registry.example.com', 'credentials-id') {
                        docker.image('my-devops-app').push('latest')
                    }
                }
            }
        }
        stage('Terraform Apply') {
            steps {
                script {
                    // Set up Terraform
                    sh 'wget https://releases.hashicorp.com/terraform/0.15.5/terraform_0.15.5_linux_amd64.zip'
                    sh 'unzip terraform_0.15.5_linux_amd64.zip'
                    sh 'mv terraform /usr/local/bin/'

                    // Apply Terraform configuration
                    sh 'terraform init terraform/'
                    sh 'terraform apply -auto-approve terraform/'
                }
            }
        }
        stage('Deploy to Kubernetes') {
            steps {
                script {
                    // Add Kubernetes deployment steps here using Helm
                    sh 'helm upgrade --install my-devops-app ./helm-chart'
                }
            }
        }
    }
}
