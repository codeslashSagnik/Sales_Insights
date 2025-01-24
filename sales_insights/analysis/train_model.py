import os
import numpy as np
import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from sklearn.model_selection import GridSearchCV
import pickle


try:
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='user',
        database='sales_data'
    )
    print("Connection to MySQL server established successfully.")
except mysql.connector.Error as err:
    print(f"Error: {err}")
    connection = None

if connection:
    try:
        query = "SELECT * FROM data_salesdata;"
        df = pd.read_sql(query, connection)
        print("Data fetched successfully from the database.")
    except Exception as e:
        print(f"Error while fetching data: {e}")
        df = None
        
if df is not None:
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    df['total_revenue'] = df['price_per_unit'] * df['units_sold']
    print("Feature 'total_revenue' added.")


    output_file = "./csv_data/cleaned_sales_data.csv"
    try:
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        df.to_csv(output_file, index=False)
        print(f"Cleaned data saved to {output_file}.")
    except Exception as e:
        print(f"Error while saving data: {e}")

 
    if connection:
        connection.close()
        print("Connection to MySQL server closed.")

    
    selected_df = df[['id', 'price_per_unit', 'units_sold', 'total_revenue']]

   
    df = pd.read_csv('./csv_data/cleaned_sales_data.csv')

    numerical_features = ['price_per_unit', 'units_sold', 'total_revenue']
    scaler = MinMaxScaler()
    df[numerical_features] = scaler.fit_transform(df[numerical_features])

    
    models = {
        'Linear Regression': LinearRegression(),
        'Ridge Regression': Ridge(),
        'Lasso Regression': Lasso(),
        'Random Forest': RandomForestRegressor(),
        'Support Vector Regression': SVR()
    }

    params = {
        'Ridge Regression': {'alpha': [0.1, 1, 10, 100]},
        'Lasso Regression': {'alpha': [0.1, 1, 10, 100]},
        'Random Forest': {'n_estimators': [100, 200], 'max_depth': [None, 10, 20]},
        'Support Vector Regression': {'C': [0.1, 1, 10], 'kernel': ['linear', 'rbf']}
    }

    X = df[['price_per_unit', 'total_revenue']]
    y = df['units_sold']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


    def tune_models(X_train, y_train):
        results = []
        for model_name, model in models.items():
            if model_name in params:
                grid_search = GridSearchCV(model, params[model_name], scoring='neg_mean_squared_error', cv=5)
                grid_search.fit(X_train, y_train)
                best_params = grid_search.best_params_
            else:
                model.fit(X_train, y_train)
                best_params = {}

            results.append({
                'Model': model_name,
                'Best Parameters': best_params
            })
        return pd.DataFrame(results)


    tuned_res = tune_models(X_train, y_train)
    print(tuned_res)

    models_dir = "./models/"
    os.makedirs(models_dir, exist_ok=True)

    model_performance = []

    for model_name, model in models.items():
        best_params = tuned_res[tuned_res['Model'] == model_name]['Best Parameters'].values[0]
        model.set_params(**best_params)

        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

        mse = mean_squared_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)

        model_performance.append({
            'Model': model_name,
            'MSE': mse,
            'R2 Score': r2
        })

        model_filename = os.path.join(models_dir, f"{model_name.replace(' ', '_').lower()}_model1.pkl")
        with open(model_filename, "wb") as file:
            pickle.dump(model, file)

 
    performance_df = pd.DataFrame(model_performance)
    print(performance_df)

