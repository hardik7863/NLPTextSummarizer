# Text Summarizer Using Huggingface

### Workflows 

1. Config.yaml
2. Params.yaml
3. Config entity
4. Configuration Manager
5. Update the components- Data Ingestion, Data Transformation, Model Trainer
6. Create our Pipeline-- Training Pipeline, Prediction Pipeline
7. Front end-- API's, Training API's, Batch Prediction API's

## Overview
This project aims to develop a text summarization tool using Huggingface's transformer models. The tool generates concise summaries from large text documents, making it easier to extract key information quickly.

## Tech Stack
- Python
- Huggingface Transformers
- TensorFlow/PyTorch
- FastAPI (for API development)
- Docker
- Google Colab (for model training)
- GitHub Actions (CI/CD)

## Features
- **Data Ingestion**: Collect and preprocess text data for training.
- **Data Transformation**: Transform raw text data into a suitable format for model training.
- **Model Training**: Train transformer models for text summarization using Huggingface's pre-trained models.
- **Prediction Pipeline**: Generate summaries for new text inputs.
- **RESTful APIs**: Expose model training and prediction functionalities via FastAPI.
- **CI/CD**: Automate testing and deployment using GitHub Actions.
- **Docker**: Containerize the application for scalable and reproducible environments.

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/21-NLPTextSummarizer.git
    cd 21-NLPTextSummarizer
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
### Training the Model
To train the model, run the following command:
```bash
python main.py