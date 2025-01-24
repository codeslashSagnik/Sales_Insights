import pickle
import numpy as np


def load_model():
    with open('random_forest_model.pkl', 'rb') as file:
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
    
    for price in price_range:
        input_data = np.array([[price, units_sold, month]])
        revenue = model.predict(input_data)[0]
        if revenue > max_revenue:
            max_revenue = revenue
            best_price = price
    
    return best_price, max_revenue
