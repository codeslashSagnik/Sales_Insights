import pickle
import numpy as np
from sklearn.preprocessing import MinMaxScaler

def load_model():
    with open('E:/cv projects/Sales Insights/sales_insights/analysis/models/random_forest_model.pkl', 'rb') as file:

        model = pickle.load(file)
    return model


def predict_revenue(price_per_unit, units_sold, month):
    model = load_model()
    input_data = np.array([[price_per_unit, units_sold, month]])
    predicted_revenue = model.predict(input_data)[0]
    return predicted_revenue


def find_optimal_price(price_range, units_sold, month):
    model = load_model()
    best_price = None
    max_revenue = float('-inf')
    with open('E:/cv projects/Sales Insights/sales_insights/analysis/models/scaler.pkl', 'rb') as scaler_file:
        scaler = pickle.load(scaler_file)

    for price in price_range:
        input_data = np.array([[price, units_sold, month]])
        input_data_scaled  = scaler.transform(input_data)
        revenue = model.predict(input_data_scaled )[0]
        if revenue > max_revenue:
            max_revenue = revenue
            best_price = price
    
    return best_price, max_revenue
