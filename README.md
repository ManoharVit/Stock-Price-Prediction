# Stock Price Prediction

The project integrates advanced machine learning techniques with MLOps practices to create a scalable, automated, and efficient pipeline for financial market forecasting. The approach focuses on stock market analysis, combining data from various sources including FRED (Federal Reserve Economic Data), Fama-French factors. The project utilizes modern tools and platforms such as Google Cloud Platform (GCP), Vertex AI, GitHub Actions, and Airflow, emphasizing automation, monitoring, and model lifecycle management. 

Here's an overview of the projectc how we build a predictive model for stock price forecasting while implementing a complete MLOps workflow for data collection, model training, deployment, and monitoring to ensure scalability, reproducibility, and maintainability.

### README files

To read all files:

   > Refer to [Assignments Submissions](https://github.com/IE7374-MachineLearningOperations/StockPricePrediction/tree/1e36981df331c0ecb44a13194e940dbe7ba8aa5b/Assignments_Submissions/) 

To read current phase:
   > Refer to [Model Deployment](https://github.com/IE7374-MachineLearningOperations/StockPricePrediction/tree/c50d70f57592fa1ca139141ce09fe82099e7ea1b/Assignments_Submissions/Model%20Deployment)

## Table of Contents
- [Directory Structure](#directory-structure)
- [Data Sources](#data-sources)
- [Setup and Usage](#setup-and-usage)
- [Environment Setup](#environment-setup)
- [Running the Pipeline](#running-the-pipeline)
- [Test Functions](#test-functions)
- [Reproducibility and Data Versioning](#reproducibility-and-data-versioning)
- [Airflow Implementation](#airflow-implementation)
- [Pipeline Components](#pipeline-components)
- [CI/CD Prerequisites](#prerequisites)
- [Model Serving and Deployment](#model-serving-and-deployment)
- [Monitoring and Maintenance](#monitoring-and-maintenance)
- [Notifications](#notifications)
- [UI Dashboard for Stock Price Prediction](#ui-dashboard-for-stock-price-predictor)
---

### Directory Structure

```
.
├── artifacts                      
│   ├── drift_detection_log.txt
│   └── schema.pbtxt
├── assets                         # airflow*, gcp*, and github* images
│   ├── airflow_dags.png
│   ├── Model serving.png
│   ├── wandb_main_dashboard.png
│   └── VM_instance.png
├── Assignments_Submissions        # Reports and documentation
│   ├── DataPipeline Phase         # Includes README and pipeline documentation
│   ├── Model Deployment           # Deployment phase documentation
│   ├── Model Development Pipeline Phase
│   ├── Scoping Phase              # Scoping reports and user needs
├── data                           # Raw and preprocessed datasets
│   ├── raw                        # Unprocessed datasets
│   ├── preprocessed               # Cleaned datasets
├── GCP                            # Google Cloud-related files and scripts
│   ├── application credentials, deployment configs
│   ├── gcpdeploy                  # Scripts for training and serving models
│   └── wandb                      # Weights & Biases logs and metadata
├── pipeline                       # Pipeline scripts and configurations
│   ├── airflow                    # DAGs, logs, and DAG-related scripts
│   ├── dags/data                  # Data source files for pipeline tasks
│   ├── artifacts                  # Artifacts generated from DAGs
│   ├── tests                      # Unit test scripts for pipeline tasks
│   └── wandb                      # Workflow and run logs
├── src                            # Core source code (Py script, Notebook, Model scripts)
│   ├── Data
│   ├── best_model.py
│   └── Datadrift_detection_updated.ipynb
├── requirements.txt               # Python dependencies
├── dockerfile                
├── LICENSE                        
└── README.md                      # Main documentation

```
---

### Setup and Usage

To set up and run the pipeline:

   > Refer to [Environment Setup](https://github.com/IE7374-MachineLearningOperations/StockPricePrediction/tree/main?tab=readme-ov-file#environment-setup) 

   > Refer to [Running Pipeline](https://github.com/IE7374-MachineLearningOperations/StockPricePrediction/tree/main?tab=readme-ov-file#running-the-pipeline)


## Environment Setup

To set up and run this project, ensure the following are installed:

- **Python** (3.8 or later)
- **Docker** (for running Apache Airflow)
- **DVC** (for data version control)
- **Google Cloud SDK** (we are deploying on GCP)

### Installation Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/IE7374-MachineLearningOperations/StockPricePrediction.git
   cd Stock-Price-Prediction
   ```

2. **Install Python Dependencies**
   Install all required packages listed in `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

3. **Initialize DVC**
   Set up DVC to manage large data files by pulling the tracked data:
   ```bash
   dvc pull
   ```
---

## Running the Pipeline

To execute the data pipeline, follow these steps:

1. **Start Airflow Services**
   Run Docker Compose to start services of the Airflow web server, scheduler:
   ```bash
   cd pipeline/airflow/
   docker-compose up
   ```

2. **Access Airflow UI**
   Open `http://localhost:8080` in your browser. Log into the Airflow UI and enable the DAG

3. **Trigger the DAG**
   Trigger the DAG manually to start processing. The pipeline will:
   - Ingest raw data and preprocess it.
   - Perform correlation analysis to identify redundant features.
   - Execute PCA to reduce dimensionality.
   - Generate visualizations, such as time series plots and correlation matrices.

4. **Check Outputs**
   Once completed, check the output files and images in the `artifcats/` folder.

or 

```sh
# Step 1: Activate virtual environment: 
cd airflow_env/ # (go to Airflow environment and open in terminal)
source bin/activate

# Step 2: Install Airflow (not required if done before)
pip install apache-airflow

# Step 3: Initialize Airflow database (not required if done before)
airflow db init

# Step 4: Start Airflow web server and airflow scheduler
airflow webserver -p 8080 & airflow scheduler

# Step 5: Access Airflow UI in your default browser
# http://localhost:8080

# Step 6: Deactivate virtual environment (after work completion)
deactivate
```

---
## Test Functions
   Run all tests in the `tests` directory
   ```bash
   pytest pipeline/airflow/tests/
   ```
---
## Reproducibility and Data Versioning

We used **DVC (Data Version Control)** for files management.

### DVC Setup
1. **Initialize DVC** (not required if already initialize):
   ```bash
   dvc init
   ```

2. **Pull Data Files**
   Pull the DVC-tracked data files to ensure all required datasets are available:
   ```bash
   dvc pull
   ```

3. **Data Versioning**
   Data files are generated with `.dvc` files in the repository

4. **Tracking New Data**
   If new files are added, to track them. Example:
   ```bash
   dvc add <file-path>
   dvc push
   ```
5. **Our Project Bucket**

![GCP Bucket](https://github.com/IE7374-MachineLearningOperations/StockPricePrediction/blob/v1.0/assets/gcpbucket.png)

---

### Data Sources

1. **ADS Index**: Tracks economic trends and business cycles.
2. **Fama-French Factors**: Provides historical data for financial research.
3. **FRED Variables**: Includes various economic indicators, such as AMERIBOR, NIKKEI 225, and VIX.
4. **YFinance**: Pulls historical stock data ('GOOGL') for financial time-series analysis.

---

### Airflow Implementation

The Airflow DAG (`Group10_DataPipeline_MLOps`) was successfully implemented and tested, with all tasks executing as expected. The following details summarize the pipeline's performance and execution.

#### DAG Run Summary
- **Total Runs**: 10
- **Last Run**: 2024-11-16 02:34:59 UTC
- **Run Status**: Success
- **Run Duration**: 00:03:37

![DAG Run Summary](https://github.com/IE7374-MachineLearningOperations/StockPricePrediction/blob/v1.0/assets/airflow_graph.png)

#### Task Overview
The DAG consists of 19 tasks, each representing a step in the data processing, feature engineering, and model development pipeline. Key tasks include:
1. `download_data_task` - Downloads initial datasets from multiple financial data sources.
2. `convert_data_task` - Converts data types to ensure compatibility and efficiency.
3. `keep_latest_data_task` - Filters datasets to keep only the most recent data.
4. `remove_weekend_data_task` - Removes data points from weekends to ensure consistency in the time-series analysis.
5. `handle_missing_values_task` - Handles missing data using imputation techniques or removal where necessary.
6. `plot_time_series_task` - Visualizes the time series trends for better exploratory analysis.
7. `removing_correlated_variables_task` - Eliminates highly correlated variables to prevent redundancy.
8. `add_lagged_features_task` - Generates lagged features to capture temporal dependencies in the dataset.
9. `add_feature_interactions_task` - Creates new interaction features between existing variables for improved predictive power.
10. `add_technical_indicators_task` - Calculates financial technical indicators, such as moving averages and RSI.
11. `scaler_task` - Scales the dataset features to a consistent range to enhance model training stability.
12. `visualize_pca_components_task` - Performs PCA for dimensionality reduction and visualizes the key components.
13. `upload_blob_task` - Uploads processed data or model artifacts to cloud storage for later access.
14. `linear_regression_model_task` - Trains a linear regression model on the processed data.
15. `lstm_model_task` - Trains an LSTM model for time-series predictions.
16. `xgboost_model_task` - Trains an XGBoost model for predictive analysis.
17. `sensitivity_analysis_task` - Analyzes model sensitivity to understand feature importance and impact on predictions.
18. `detect_bias_task` - Detects any biases in the model by evaluating it across different data slices.
19. `send_email_task` - Sends notifications regarding the DAG's completion status to the stakeholders.

All tasks completed successfully with minimal execution time per task, indicating efficient pipeline performance.

#### Execution Graph and Gantt Chart
The **Execution Graph** confirms that tasks were executed sequentially and completed successfully (marked in green), showing no deferred, failed, or skipped tasks. The **Gantt Chart** illustrates the time taken by each task and confirms that the pipeline completed within the expected duration.

#### Execution Graph
![Execution Graph](https://github.com/IE7374-MachineLearningOperations/StockPricePrediction/blob/v1.0/assets/airflow_pipeline.png)

#### Gantt Chart
![Gantt Chart](https://github.com/IE7374-MachineLearningOperations/StockPricePrediction/blob/v1.0/assets/airflow_gantt.png)

#### Task Logs
Detailed logs for each task provide insights into the processing steps, including correlation matrix updates, data handling operations, and confirmation of successful execution steps. 

![Task Logs](https://github.com/IE7374-MachineLearningOperations/StockPricePrediction/blob/v1.0/assets/airflow_logging.jpeg)

#### Email Notifications 
**Anomaly Detection and Automated Alert**
Automated email notifications were configured to inform the team of task success or failure. As shown in the sample emails, each run completed with a success message confirming the full execution of the DAG tasks.

![Email Notifications](https://github.com/IE7374-MachineLearningOperations/StockPricePrediction/blob/v1.0/assets/email_notification.jpeg)

#### Testing Summary
The pipeline scripts were validated with 46 unit tests using `pytest`. All tests passed with zero errors. These tests cover critical modules such as:
- `test_handle_missing.py`
- `test_feature_interactions.py`
- `test_plot_yfinance_time_series.py`

![Test Summary](https://github.com/IE7374-MachineLearningOperations/StockPricePrediction/blob/v1.0/assets/test_functions.jpeg)

These tests ensure the stability and accuracy of data transformations, visualizations, and feature engineering processes.

---

### Pipeline Components

1. **Data Extraction**:
   - `download_data.py`: Downloads datasets from various financial sources and loads them into the `data` directory.

2. **Data Preprocessing**:
   - `convert_column_dtype.py`: Converts data types for efficient processing.
   - `remove_weekend_data.py`: Filters out weekend data to maintain consistency in time-series analyses.
   - `handle_missing.py`: Handles missing data by imputation or removal.

3. **Feature Engineering**:
   - `correlation.py`: Generates a correlation matrix to identify highly correlated features.
   - `pca.py`: Performs Principal Component Analysis to reduce dimensionality and capture key components.
   - `lagged_features.py`: Creates lagged versions of features for time-series analysis.
   - `technical_indicators.py`: Calculates common technical indicators used in financial analyses.

4. **Data Scaling**:
   - `scaler.py`: Scales features to a standard range for better model performance.

5. **Analysis and Visualization**:
   - `plot_yfinance_time_series.py`: Plots time-series data.
   - `feature_interactions.py`: Generates interaction terms between features.

6. **Hyperparameter Tuning**:
   - Hyperparameter tuning was performed using grid search, random search, and Bayesian optimization. The best models were selected and saved as checkpoints in the `artifacts` directory. Visualizations for hyperparameter sensitivity, such as `Linear Regression - Hyperparameter Sensitivity: model__alpha.png` and `model__l1_ratio.png`, are also included in the `artifacts` directory.

7. **Model Sensitivity Analysis**:
   - Sensitivity analysis was conducted to understand how changes in inputs impact model performance. Techniques like **SHAP** (SHapley Additive exPlanations) were used for feature importance analysis. Feature importance graphs, such as `Feature Importance for ElasticNet on Test Set.png`, were saved to provide insights into key features driving model predictions.

---

## Model Serving and Deployment

## Prerequisites
Steps for Replication

#### 1. **Environment Setup**
    - Access to a Google Cloud Platform (GCP) account with billing enabled.
    - Vertex AI and Cloud Build services activated within your GCP project.
    - The `gcloud` CLI tool installed and configured with the appropriate permissions.
    - A GitHub repository with access to GitHub Actions for automation.
    - Required IAM roles for deploying models to Vertex AI and managing Cloud Build resources.

![GCP Billing Dashboard](https://github.com/IE7374-MachineLearningOperations/StockPricePrediction/blob/257dc9560a2e3741e7e383bd63d00340c193c9c0/assets/GCP%20billing%20dashbgoard.png)

#### 2. **Running Deployment Automation**
   - Push changes to the main branch of the GitHub repository.
   - GitHub Actions automatically triggers the CI/CD pipeline to initiate deployment using Cloud Build.
   - The pipeline executes pre-defined steps, ensuring the model is correctly deployed to Vertex AI.
   - Confirm that all dependencies are installed locally or in the CI/CD pipeline environment.

#### 3. **Verifying Deployment**
   - Access the Vertex AI console to verify the deployment.
   - Test the deployed model endpoint to confirm successful deployment and validate model predictions.
   - Review monitoring dashboards to ensure no issues with prediction outputs or feature drift.

![Drift Detection Logging](https://github.com/IE7374-MachineLearningOperations/StockPricePrediction/blob/v2.1/assets/Drift%20Detection%20logging.png)

> Please refer to [Data drift Notebook](https://github.com/IE7374-MachineLearningOperations/StockPricePrediction/blob/c79c65ec5044c5935e2e3052730dac3a9778c51a/src/Datadrift_detection_updated.ipynb)

- **The drift detection** process identifies significant shifts in data patterns by analyzing key statistical metrics across features such as Volume, RSI, MACD, MA20, and SP500_VIXCLS_ratio. Metrics like mean, variance, and percentile differences reveal substantial deviations, indicating changes in data distribution. For example, Volume shows a mean difference of `1.083e+16` and variance difference of `0.591`, while RSI highlights deviations in its 50th percentile and variance. MACD and MA20 exhibit notable shifts in percentiles, suggesting changes in trend-related features, and SP500_VIXCLS_ratio reveals variability in market volatility. These findings emphasize the need to monitor data sources, adjust preprocessing pipelines, and potentially retrain models to maintain prediction accuracy and ensure model reliability in dynamic environments.

---

## Model Serving and Deployment

Workflows and setups for managing machine learning pipelines on Vertex AI in Google Cloud are as follows:

1. **Jupyter Notebooks in Vertex AI Workbench**:
   - The setup includes instances like `group10-test-vy` and `mlops-group10`, both configured for NumPy/SciPy and scikit-learn environments. These notebooks are GPU-enabled, optimizing their utility for intensive ML operations.

2. **Training Pipelines**:
   - Multiple training pipelines are orchestrated on Vertex AI, such as `mlops-group10` and `group10-model-train`. These are primarily custom training pipelines aimed at tasks like hyperparameter tuning, training, and validation, leveraging the scalability of Google Cloud's infrastructure.

3. **Metadata Management**:
   - Metadata tracking is managed through Vertex AI Metadata Store, with records such as `vertex_dataset`. This ensures reproducibility and streamlined monitoring of all artifacts produced during ML workflows.

4. **Model Registry**:
   - Deployed models like `mlops-group10-deploy` and `group10-model` are maintained in the model registry. The registry supports versioning and deployment tracking for consistency and monitoring.

5. **Endpoints for Online Prediction**:
   - Various endpoints, such as `mlops-group10-deploy` and `testt`, are active and ready for predictions. The setup is optimized for real-time online predictions, and monitoring can be enabled for anomaly detection or drift detection.

### Steps for Deployment of Trained Models
1. **Model Registration**: Once a model is trained, register it in Vertex AI's Model Registry. Specify the model name, version, and any relevant metadata.

![Vertex AI Jupyter Notebooks](https://github.com/IE7374-MachineLearningOperations/StockPricePrediction/blob/v3.1/assets/Vertex%20AI%20jupyter%20notebooks.png)

![Model Serving](https://github.com/IE7374-MachineLearningOperations/StockPricePrediction/blob/v2.1/assets/Model%20serving.png)

![Vertex AI Model Registry](https://github.com/IE7374-MachineLearningOperations/StockPricePrediction/blob/v3.1/assets/Vertex%20AI%20model%20registry.png)

2. **Create an Endpoint**: 
   - In Vertex AI, create an endpoint. This endpoint will act as the interface for serving predictions.
   - Navigate to Vertex AI > Online prediction > Endpoints > Create.
   - Assign a name and select the appropriate region.

![Vertex AI Endpoints](https://github.com/IE7374-MachineLearningOperations/StockPricePrediction/blob/v2.1/assets/Vertex%20Ai%20endpoints.png)

3. **Deploy the Model to an Endpoint**:
   - Select the registered model and choose "Deploy to Endpoint".
   - Configure the deployment settings such as machine type, traffic splitting among model versions, and whether to enable logging or monitoring.
   - Confirm deployment which will make the model ready to serve predictions.

![Vertex AI Model Development Training](https://github.com/IE7374-MachineLearningOperations/StockPricePrediction/blob/v3.1/assets/Vertex%20AI%20model%20development%20training.png)

### Model Versioning
- **Manage Versions**: In Vertex AI, each model can have multiple versions allowing easy rollback and version comparison.
- **Update Versions**: Upload new versions of the model to the Model Registry and adjust the endpoint configurations to direct traffic to the newer version.

### Deployment Automation
#### Continuous Integration and Deployment Pipeline
- **Automate Deployments**: Use GitHub Actions and Google Cloud Build to automate the deployment of new model versions from a repository.
- **CI/CD Pipeline Configuration**:
   - **GitHub Actions**: Configure workflows in `.github/workflows/` directory to automate testing, building, and deploying models.
   - **Cloud Build**: Create a `cloudbuild.yaml` file specifying steps to build, test, and deploy models based on changes in the repository.

![GitHub Actions CI/CD](https://github.com/IE7374-MachineLearningOperations/StockPricePrediction/blob/v2.1/assets/Github%20Actions%20CICD.png)

---

#### Automated Deployment Scripts
- **Script Functions**:
  - **Pull the Latest Model**: Scripts should fetch the latest model version from Vertex AI Model Registry or a specified repository.
  - **Deploy or Update Model**: Automate the deployment of the model to the configured Vertex AI endpoint.
  - **Monitor and Log**: Set up logging for deployment status to ensure visibility and troubleshooting capabilities.

---
### Workflows Overview

#### 1. **Airflow DAG Trigger Workflow**
   - **File:** `airflowtrigeer.yaml`
   - **Purpose:** Initializes Airflow, starts required services, triggers a DAG (`Group10_DataPipeline_MLOps`), and monitors its execution.
   - **Key Steps:**
     - Sets up Python and dependencies.
     - Initializes and starts Airflow services via Docker Compose.
     - Triggers the specified Airflow DAG and monitors its status until completion.
     - Stops services and removes containers after execution.
   - **Triggers:** On push to `main` 

![Airflow DAG Trigger Workflow](https://github.com/IE7374-MachineLearningOperations/StockPricePrediction/blob/v3.1/assets/Trigger%20airflow%20action.png)

#### 2. **Model Training Workflow**
   - **File:** `model.yml`
   - **Purpose:** Packages the trainer code, uploads it to GCS, and triggers a Vertex AI Custom Job for model training.
   - **Key Steps:**
     - Prepares a Python trainer package (`trainer/task.py`) and packages it.
     - Uploads the package to a GCS bucket.
     - Triggers a Vertex AI Custom Job with specified training arguments (e.g., dataset path, epochs, batch size).
     - Notifies upon completion.

![Model Training Workflow](https://github.com/IE7374-MachineLearningOperations/StockPricePrediction/blob/v3.1/assets/Train%20deploy%20github%20action.png)

#### 3. **Deploy and Monitor Workflow**
   - **File:** `deploy_monitor.yaml`
   - **Purpose:** Deploys the trained model to Vertex AI, creates an endpoint, and sets up monitoring for model performance and data drift.
   - **Key Steps:**
     - Deploys the model to Vertex AI.
     - Configures a new or existing endpoint for predictions.
     - Enables monitoring for performance and feature/data drift.
   - **Triggers:** On push to `main` 

![Deploy and Monitor Workflow](https://github.com/IE7374-MachineLearningOperations/StockPricePrediction/blob/v3.1/assets/Deploy%20and%20monitor%20action.png)

#### 4. **Train and Deploy Workflow**
   - **File:** `train_deploy.yaml`
   - **Purpose:** Trains the ML model and deploys it to Vertex AI for online predictions.
   - **Key Steps:**
     - Builds a Docker image of the training script and pushes it to GCP Artifact Registry.
     - Triggers model training.
     - Deploys the trained model to a new or existing endpoint.
   - **Triggers:** On push to `main`

![Train Workflow](https://github.com/IE7374-MachineLearningOperations/StockPricePrediction/blob/v3.1/assets/Train%20deploy%20github%20action.png)

#### 5. **Pytest Workflow**
   - **File:** Not explicitly listed (part of repository tests).
   - **Purpose:** Runs automated tests on codebase changes.
   - **Key Steps:**
     - Installs project dependencies.
     - Executes tests using `pytest` to ensure the codebase is robust and ready for deployment.
   - **Triggers:** On push to `main`

![Pytest Workflow](https://github.com/IE7374-MachineLearningOperations/StockPricePrediction/blob/v3.1/assets/Pytest%20action.png)

#### **6. `syncgcp.yaml`**
- **Purpose**: Synchronizes local artifacts and Airflow DAGs with a Google Cloud Storage bucket. Workflow to build Docker images, upload artifacts to GCP, and deploy to endpoints.
- **Steps**:
  - **Environment setup**: Installs the Google Cloud CLI and authenticates with a service account.
  - **File uploads**:
    - Uploads specific artifacts and files to predefined GCP bucket locations.
    - Synchronizes repository content with the bucket directory structure.
  - **Verification**: Lists uploaded files to confirm the sync.

![Upload and Dockerize Workflow](https://github.com/IE7374-MachineLearningOperations/StockPricePrediction/blob/v3.1/assets/syncgcp%20githubaction.png)

---

![GitHub Actions](https://github.com/IE7374-MachineLearningOperations/StockPricePrediction/blob/v2.1/assets/Github%20Workflows.png)


#### Summary
These YAML workflows automate various aspects of an ML lifecycle:
1. **`airflowtrigger.yaml`**: Airflow DAG management.
2. **`train_deploy.yaml`**: Trains the ML model and deploys it to Vertex AI for online predictions.
3. **`model.yml`**: Training pipeline and GCS uploads.
4. **`PyTest.yaml`**: Testing and reporting.
5. **`syncgcp.yaml`**: Artifact and DAG synchronization with GCP.
6. **`deploy_monitor.yaml`**: Deploys the trained model, monitoring for model performance and data drift.

- Each workflow is tailored for a specific task in CI/CD for ML operations, leveraging GitHub Actions and Google Cloud services.
---

## Monitoring and Maintenance

1. **Monitoring**:
   - Vertex AI provides dashboards to monitor model performance and data drift.
   - Alerts are configured to notify stakeholders when anomalies, such as feature attribution drift, are detected.

![Monitor Feature Detection](https://github.com/IE7374-MachineLearningOperations/StockPricePrediction/blob/v2.1/assets/Monitor%20feature%20detection.png)

![Monitor Drift Detection](https://github.com/IE7374-MachineLearningOperations/StockPricePrediction/blob/v2.1/assets/Monitor%20drift%20detection.png)

![Model Monitoring Anomalies](https://github.com/IE7374-MachineLearningOperations/StockPricePrediction/blob/v2.1/assets/Model%20monitoring%20Anomolies.png)

The provided images highlight the active setup and management of a Vertex AI model monitoring system. Files like `anomalies.json` and `anomalies.textproto` document identified issues in the input data. The structure also includes folders such as `baseline`, `logs`, and `metrics`, which organize monitoring data effectively for future analysis. A notification email confirming the creation of a model monitoring job for a specific Vertex AI endpoint. This email provides essential details, such as the endpoint name, monitoring job link, and the GCS bucket path where statistics and anomalies will be saved. 

2. **Maintenance**:
   - Pre-configured thresholds for model performance trigger retraining or redeployment of updated models.
   - Logs and alerts from Vertex AI and Cloud Build ensure the system remains reliable and scalable.

![Monitor Details](https://github.com/IE7374-MachineLearningOperations/StockPricePrediction/blob/v2.1/assets/Monitor%20details.png)

![Logging Dashboard](https://github.com/IE7374-MachineLearningOperations/StockPricePrediction/blob/v2.1/assets/Logging%20Dashboard.png)


---

## Notifications

### Vertex AI Failure Notification
This notification is sent when a Vertex AI Model Monitoring job partially fails. For example, if the model encounters a drift detection issue or missing explanation specifications, an email alert is sent.

![Vertex AI Failure Notification](https://github.com/IE7374-MachineLearningOperations/StockPricePrediction/blob/v3.1/assets/VertexAI%20failure%20notification.png)  

### Vertex AI Anomaly and Data Drift Notification
This email notification is triggered when data drift or anomalies are detected in the deployed model. It provides links to detailed logs and monitoring jobs for debugging.

![Vertex AI Anomaly and Data Drift Notification](https://github.com/IE7374-MachineLearningOperations/StockPricePrediction/blob/v3.1/assets/Vertex%20AI%20Anomoly%20and%20Datadrift%20notify.png)  


#### **Partial Failure Notification**
This email is sent when a model monitoring job partially fails, providing details about the type of failure and suggestions for resolving the issue.

![Partial Failure Notification](https://github.com/IE7374-MachineLearningOperations/StockPricePrediction/blob/v3.1/assets/VertexAI%20failure%20notification.png)  

#### **Anomaly and Data Drift Detection Notification**
This email is triggered when the Vertex AI monitoring job detects data drift or anomalies in the deployed model. It provides links for further investigation.

![Anomaly and Data Drift Detection Notification](https://github.com/IE7374-MachineLearningOperations/StockPricePrediction/blob/v3.1/assets/Vertex%20AI%20Anomoly%20and%20Datadrift%20notify.png)  

## UI Dashboard for Stock Price Predictor

The **Stock Price Predictor UI Dashboard** is a user-friendly interface designed to analyzing stock trends and making informed financial decisions. This dashboard, running locally at [http://127.0.0.1:5001](http://127.0.0.1:5001), provides a good experience for users to explore stock predictions and insights.

### Running the Dashboard

To launch the application:

1. Run the following command:
   ```bash
   python app/app.py
   ```

2. Access the dashboard at:
   [http://127.0.0.1:5001](http://127.0.0.1:5001)

This dashboard bridges the gap between raw stock data and actionable investment strategies, making financial decision-making easier and more efficient.

#### Key Features

1. **Homepage**: 
   - Provides an overview of the tool's capabilities and purpose.
   - Highlights the integration of machine learning with financial decision-making.

   ![Homepage](https://github.com/IE7374-MachineLearningOperations/StockPricePrediction/blob/63ef3b06820c954454afe53fd669159ebb54bf34/assets/UI_Dashboard_homepage.png)

2. **Prediction Page**:
   - Displays the **current stock price** and the **predicted price**.
   - Includes options to "Buy" or "Sell" based on the predicted price trend.
   - Offers a gamified experience to engage users in testing their predictions.

   ![Prediction Dashboard](https://github.com/IE7374-MachineLearningOperations/StockPricePrediction/blob/63ef3b06820c954454afe53fd669159ebb54bf34/assets/UI_Dashboard_predict.png)

3. **Visualization Dashboard**:
   - Features dynamic and interactive charts to compare actual vs. predicted stock prices.
   - Provides insights into stock trends.

   ![Visualization Dashboard](https://github.com/IE7374-MachineLearningOperations/StockPricePrediction/blob/63ef3b06820c954454afe53fd669159ebb54bf34/assets/UI_Dashboard_visuals.png)

---
## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/IE7374-MachineLearningOperations/StockPricePrediction/blob/2abdea96ee56b51357cd519a9f5e89126b9c87bb/LICENSE) file.

