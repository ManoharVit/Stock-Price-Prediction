# Stock-Price-Prediction

## Description
The primary goal of this project is to improve stock price forecasting and prediction by creating an effective Machine Learning Operations (MLOps) pipeline. Utilising sophisticated financial modelling methods like the GARCH and Kalman filters, the pipeline seeks to maximise model performance and increase the precision of stock volatility forecasts. In order to provide scalability and flexibility to new data and market trends, the project builds an automated pipeline that facilitates continuous integration and delivery of machine learning models. The system is able to react dynamically to shifting market conditions because of the smooth integration of fresh data made possible by this scalable MLOps architecture. In the end, this helps academics, data scientists, and financial analysts who want to use MLOps to make better investment decisions by producing forecasts that are more accurate.

```bash
    .
    |-- .DS_Store
    |-- LICENSE
    |-- requirements.txt
    |-- README.md
    |-- current_tree.txt
    |-- pipeline/
        |-- .DS_Store
        |-- config/
        |-- airlfow/
            |-- .DS_Store
            |-- dags/
                |-- docker.yaml
    |-- test/
    |-- docs/
    |-- mlruns/
    |-- gcpdeploy/
        |-- gcp.py
    |-- .git/
        |-- .DS_Store
        |-- config
        |-- HEAD
        |-- description
        |-- index
        |-- packed-refs
        |-- COMMIT_EDITMSG
        |-- FETCH_HEAD
        |-- info/
            |-- exclude
        |-- refs/
            |-- heads/
                |-- main
            |-- tags/
            |-- remotes/
                |-- origin/
                    |-- Oviya
                    |-- Gopichand
                    |-- Omkar
                    |-- Manohar
                    |-- HEAD
                    |-- Vy
                    |-- Samarth
                    |-- main
        |-- branches/
    |-- data/
        |-- FamaFrench_Data_5_Fact.csv
    |-- assets/
        |-- Initial plan.jpg
    |-- notebooks/
        |-- dataprep.ipynb
        |-- prediction.py
    |-- src/
        |-- dataapi.py
```

## Table of Contents
1. [Installation](#installation)
2. [Usage](#usage)
3. [Technologies](#technologies)
4. [License](#license)
5. [Contact](#contact)

## Installation

### Prerequisites
List the software and dependencies required for the project to run
- Python 3.12
- Flask 2.0
- yfinance
- Pandas

### Steps to Install/Use

1. Clone this repository:
    ```bash
    git clone https://github.com/ManoharVit/Stock-Price-Prediction.git
    cd Stock-Price-Prediction
    ```

2. Set up a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up the database:
    - Configure your database connection settings in `config.py` or `.env` file.
    - Run migrations (if applicable):
        ```bash
        flask db upgrade
        ```

5. Start the application:
    ```bash
    flask run
    ```

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

