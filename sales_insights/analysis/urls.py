from django.urls import path
from . import views

urlpatterns = [
    path('', views.result_view, name='revenue_prediction'),

    path('result/', views.result_view, name='result'),
]