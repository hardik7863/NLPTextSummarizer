# End-to-End Text Summarizer Project

## Workflows

1. Update `config.yaml`
2. Update `params.yaml`
3. Update entity
4. Update the configuration manager in `src/config`
5. Update the components
6. Update the pipeline
7. Update `main.py`
8. Update `app.py`

---

# How to Run?

### Steps:

1. Clone the repository:
    ```bash
    https://github.com/hardik7863/NLPTextSummarizer.git
    ```

2. Create a conda environment after opening the repository:
    ```bash
    conda create -n summary python=3.8 -y
    conda activate summary
    ```

3. Install the requirements:
    ```bash
    pip install -r requirements.txt
    ```

4. Finally, run the following command:
    ```bash
    python app.py
    ```

5. Open up your local host and port to access the application.

---

## Author:
**Hardik**  
Data Scientist Enthusiast

Email: hardikbatwal@gmail.com  

---

# AWS-CICD Deployment with GitHub Actions

## Steps:

### 1. Login to AWS Console.

### 2. Create an IAM User for Deployment
- **Access Required**:
  1. EC2 access: Virtual machine.
  2. ECR: Elastic Container Registry to save your Docker image in AWS.

- **Deployment Description**:
  1. Build a Docker image of the source code.
  2. Push your Docker image to ECR.
  3. Launch your EC2 instance.
  4. Pull your image from ECR in EC2.
  5. Launch your Docker image in EC2.

- **Policies Required**:
  1. `AmazonEC2ContainerRegistryFullAccess`
  2. `AmazonEC2FullAccess`

### 3. Create an ECR Repository
- Save the URI: `566373416292.dkr.ecr.us-east-1.amazonaws.com/text-s`

### 4. Create an EC2 Machine (Ubuntu)

### 5. Open EC2 and Install Docker in the EC2 Machine:
```bash
# Optional
sudo apt-get update -y
sudo apt-get upgrade

# Required
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker ubuntu
newgrp docker
```
# 6. Configure EC2 as self-hosted runner:
    setting>actions>runner>new self hosted runner> choose os> then run command one by one


# 7. Setup github secrets:

    AWS_ACCESS_KEY_ID=

    AWS_SECRET_ACCESS_KEY=

    AWS_REGION = us-east-1

    AWS_ECR_LOGIN_URI = demo>>  566373416292.dkr.ecr.ap-south-1.amazonaws.com

    ECR_REPOSITORY_NAME = simple-app