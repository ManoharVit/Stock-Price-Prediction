import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV, TimeSeriesSplit
from sklearn.linear_model import Ridge
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

# Load and preprocess data
data = pd.read_csv('Data_pipeline_airflow_dags_data_scaled_data_train.csv', index_col='date')
df = data.copy()

def split_time_series_data(df, target_column, test_size=0.1, val_size=0.1):
    df = df.sort_index()
    X = df.drop(columns=[target_column])
    y = df[target_column]
    X_train_val, X_test, y_train_val, y_test = train_test_split(X, y, test_size=test_size, shuffle=False)
    X_train, X_val, y_train, y_val = train_test_split(X_train_val, y_train_val, test_size=val_size/(1-test_size), shuffle=False)
    return X_train, X_val, X_test, y_train, y_val, y_test

X_train, X_val, X_test, y_train, y_val, y_test = split_time_series_data(df, 'close')

# Ridge Regression
def train_ridge(X_train, y_train, X_val, y_val):
    tscv = TimeSeriesSplit(n_splits=5)
    model = Ridge()
    param_grid = {'alpha': [0.05, 0.1, 0.2, 1.0]}
    grid_search = GridSearchCV(model, param_grid, cv=tscv, scoring='neg_mean_squared_error')
    grid_search.fit(X_train, y_train)
    best_model = grid_search.best_estimator_
    y_pred_val = best_model.predict(X_val)
    val_rmse = np.sqrt(mean_squared_error(y_val, y_pred_val))
    print(f"Best Parameters for Ridge: {grid_search.best_params_}")
    print(f"Validation RMSE for Ridge: {val_rmse}")
    return best_model, val_rmse

ridge_model, ridge_val_rmse = train_ridge(X_train, y_train, X_val, y_val)

# SVR
def train_svr(X_train, y_train, X_val, y_val):
    param_grid = {
        'C': [1, 10, 100],
        'gamma': ['scale', 'auto'],
        'kernel': ['rbf', 'linear'],
        'epsilon': [0.1, 0.2, 0.5]
    }
    model = SVR()
    grid_search = GridSearchCV(model, param_grid, cv=3, scoring='neg_mean_squared_error', verbose=1)
    grid_search.fit(X_train, y_train)
    best_model = grid_search.best_estimator_
    y_pred_val = best_model.predict(X_val)
    val_rmse = np.sqrt(mean_squared_error(y_val, y_pred_val))
    print(f"Best Parameters for SVR: {grid_search.best_params_}")
    print(f"Validation RMSE for SVR: {val_rmse}")
    return best_model, val_rmse

svr_model, svr_val_rmse = train_svr(X_train, y_train, X_val, y_val)

# Function to select the best model based on RMSE
def select_best_model(models_metrics):
    best_model_name = None
    best_model_metrics = None
    best_rmse = float('inf')
    for model_name, metrics in models_metrics.items():
        model_rmse = metrics.get('RMSE')
        if model_rmse < best_rmse:
            best_rmse = model_rmse
            best_model_name = model_name
            best_model_metrics = metrics
    return best_model_name, best_model_metrics

# Collect metrics
models_metrics = {
    'SVM': {'RMSE': svr_val_rmse, 'MAE': svr_val_rmse},
    'Ridge Regression': {'RMSE': ridge_val_rmse, 'MAE': ridge_val_rmse},
}

# Select the best model based on RMSE
best_model_name, best_model_metrics = select_best_model(models_metrics)
print(f"The best model is {best_model_name} with metrics: {best_model_metrics}")


