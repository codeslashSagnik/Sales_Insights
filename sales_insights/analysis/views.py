
from django.shortcuts import render
from .utils import predict_revenue, find_optimal_price
def result_view(request):
    if request.method == 'POST':
        
        price_min = float(request.POST['price_min'])
        price_max = float(request.POST['price_max'])
        units_sold = int(request.POST['units_sold'])
        month = int(request.POST['month'])
        
        expected_revenue = price_min * units_sold
        
        price_per_unit = (price_min + price_max) / 2
        
        
        predicted_revenue = predict_revenue(price_per_unit, units_sold, month)
        
        
        price_range = range(int(price_min), int(price_max) + 1)  
        
        
        best_price, max_revenue = find_optimal_price(price_range, units_sold, month)
        
        optimal_units= int(predicted_revenue / best_price)
        
        
        return render(request, 'result.html', {
            'predicted_revenue': predicted_revenue,
            'expected_revenue': expected_revenue,
            'best_price': best_price,
            'max_revenue': max_revenue,
            'optimal_units': optimal_units
        })
    
    return render(request, 'form.html')




