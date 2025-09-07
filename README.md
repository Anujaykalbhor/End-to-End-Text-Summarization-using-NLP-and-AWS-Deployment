# End-to-End-Text-Summarization-using-NLP-and-AWS-Deployment


# End-to-end Text Summarization with NLP and AWS CI/CD -->
This repository contains the code and instructions for an end-to-end Text Summarization project, from data processing to model deployment. The project is deployed on AWS using a CI/CD pipeline with GitHub Actions.

# Project Workflows
This section provides a high-level overview of the main steps in the project, from configuration to running the final application.

1. Update config.yaml with project settings.

2. Update params.yaml with model hyperparameters.

3. Define data and model schemas in the entity folder.

4. Implement the configuration manager in src/config.

5. Develop the core components for data ingestion, validation, and model training.

6. Build the training and prediction pipelines.

7. Update main.py for command-line execution.

8. Update app.py for API serving.

# How to Run Locally
Follow these steps to set up the project on your local machine and run the application.

## Steps:
1. Clone the repository to get a local copy of the code:

git clone [https://github.com/entbappy/End-to-end-Text-Summarization-using-NLP-and-AWS-Deployment.git](https://github.com/entbappy/End-to-end-Text-Summarization-using-NLP-and-AWS-Deployment.git)

cd End-to-end-Text-Summarization-using-NLP-and-AWS-Deployment

2. Create and activate a Python virtual environment to manage dependencies and avoid conflicts with other projects:

conda create -n summary python=3.8 -y
conda activate summary

3. Install the required libraries and frameworks listed in the requirements.txt file:

pip install -r requirements.txt

4. Run the application, which will start a local server to serve the text summarization API:

python app.py

5. Open your browser to the specified local host and port to view the application and interact with the API.

# AWS CI/CD Deployment with GitHub Actions
This section outlines the steps to deploy the application on AWS using a CI/CD pipeline. The pipeline will automatically build, tag, and push the Docker image to ECR on every code push to the main branch.

# 1. AWS IAM User Setup
Create an IAM user with programmatic access for your GitHub Actions. Attach the following policies to this user to grant the necessary permissions for the pipeline:

- AmazonEC2ContainerRegistryFullAccess: This policy allows the pipeline to push and pull Docker images from ECR.

- AmazonEC2FullAccess: This policy allows the pipeline to manage EC2 instances for deployment.

# 2. AWS ECR Repository
Create a private ECR repository to store your Docker image. This serves as a central registry for your application's container image.

- Save the Repository URI: 577436424323.dkr.ecr.us-east-1.amazonaws.com/text-s

# 3. GitHub Secrets Configuration
Store your AWS credentials and repository information as GitHub Secrets. This is a crucial security step that ensures your sensitive data is not exposed in the workflow file.

- AWS_ACCESS_KEY_ID: Your IAM user's access key ID.

- AWS_SECRET_ACCESS_KEY: Your IAM user's secret access key.

- AWS_REGION: The AWS region for your resources (e.g., us-east-1).

- ECR_REPOSITORY_NAME: The name of your ECR repository (e.g., text-summarization-repo).

# 4. GitHub Actions Workflow
Define a CI/CD workflow by creating a YAML file in the .github/workflows directory of your repository. This file will contain the steps for building, pushing, and deploying your Docker image automatically on every push.

# 5. AWS EC2 Setup
Launch an Ubuntu-based EC2 instance to serve as the deployment target. This instance will pull the Docker image and run the application as a container.

# Post-Launch Steps on the EC2 Machine:

- Install Docker:

sudo apt-get update -y
sudo apt-get upgrade -y
curl -fsSL [https://get.docker.com](https://get.docker.com) -o get-docker.sh
sudo sh get-docker.sh

- Add the ubuntu user to the docker group to allow running Docker commands without using sudo:

sudo usermod -aG docker ubuntu
newgrp docker

# 6. Automated Deployment
The CI/CD workflow will automatically handle the build and push to ECR. To complete the deployment, the workflow will connect to the EC2 instance, pull the latest image, and run it as a container to serve your application.