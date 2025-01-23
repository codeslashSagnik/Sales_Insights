from django import forms
from .models import SalesData

class SalesDataForm(forms.ModelForm):
    class Meta:
        model = SalesData
        fields = ['date', 'price_per_unit', 'units_sold']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}), 
        }
