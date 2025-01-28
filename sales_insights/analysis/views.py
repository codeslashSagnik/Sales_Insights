from django.shortcuts import render
from .utils import load_model_and_scalers, find_optimal_price
import numpy as np
from .utils import calculate_revenue

def result_view(request):
    if request.method == 'POST':
        price_min = float(request.POST['price_min'])
        price_max = float(request.POST['price_max'])
        month = int(request.POST['month'])
        

        model, scaler_X, scaler_Y = load_model_and_scalers()

        price_range = np.arange(price_min, price_max + 0.1, 0.1)
        
   
        optimal_price, max_revenue = find_optimal_price(price_range, model, scaler_X, scaler_Y, month)
        
      
        optimal_units_sold = calculate_revenue(optimal_price, model, scaler_X, scaler_Y, month) / optimal_price
        optimal_units_sold = int(optimal_units_sold)

        
       
        return render(request, 'result.html', {
            'optimal_price': optimal_price,
            'max_revenue': max_revenue,
            'optimal_units_sold': optimal_units_sold
        })
    
    return render(request, 'form.html')
