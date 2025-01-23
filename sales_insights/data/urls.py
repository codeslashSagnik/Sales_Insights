from django.urls import path
from . import views

urlpatterns = [
    path('add_article/', views.add_article, name='add_article'),
    path('dashboard/', views.dashboard, name='dashboard'),
    #path('edit_article/<int:pk>/', views.edit_article, name='edit_article'),
    path('delete_article/<int:pk>/', views.delete_article, name='delete_article'),
]
