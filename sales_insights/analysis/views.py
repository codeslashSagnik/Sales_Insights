
from django.shortcuts import render
from .utils import predict_revenue, find_optimal_price

def revenue_prediction_view(request):
    if request.method == 'POST':
        price_per_unit = float(request.POST['price_per_unit'])
        units_sold = int(request.POST['units_sold'])
        month = int(request.POST['month'])
        
        predicted_revenue = predict_revenue(price_per_unit, units_sold, month, weekday)
        

        price_range = range(1, 100) 
        best_price, max_revenue = find_optimal_price(price_range, units_sold, month, weekday)
        
        return render(request, 'result.html', {
            'predicted_revenue': predicted_revenue,
            'best_price': best_price,
            'max_revenue': max_revenue,
        })
    
    return render(request, 'form.html')

