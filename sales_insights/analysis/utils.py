import numpy as np
import pickle

def load_model_and_scalers():
  
    with open('E:/cv projects/Sales Insights/sales_insights/analysis/models/random_forest_model.pkl', 'rb') as model_file:
        model = pickle.load(model_file)
    
    with open('E:/cv projects/Sales Insights/sales_insights/analysis/models/scaler_X.pkl', 'rb') as scaler_X_file:
        scaler_X = pickle.load(scaler_X_file)
    
    with open('E:/cv projects/Sales Insights/sales_insights/analysis/models/scaler_Y.pkl', 'rb') as scaler_Y_file:
        scaler_Y = pickle.load(scaler_Y_file)
    
    return model, scaler_X, scaler_Y

def calculate_revenue(price, model, scaler_X, scaler_Y, month=5):

    sample_input = np.array([[price, month]])  
    sample_input_scaled = scaler_X.transform(sample_input)  
    
    
    predicted_units_sold = model.predict(sample_input_scaled)
    
    
    predicted_units_sold = scaler_Y.inverse_transform(predicted_units_sold.reshape(-1, 1))[0][0]
    
    return price * predicted_units_sold

def find_optimal_price(price_range, model, scaler_X, scaler_Y, month=5):

    optimal_price = None
    max_revenue = 0
    
    for price in price_range:
        revenue = calculate_revenue(price, model, scaler_X, scaler_Y, month)
        if revenue > max_revenue:
            max_revenue = revenue
            optimal_price = price
    
    return optimal_price, max_revenue
