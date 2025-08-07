from django.urls import path 
from . import views
from .views import ItemListCreateView, ItemDetailView

app_name = 'hicourt'

urlpatterns = [
    # A simple home page view
    path('', views.home, name='home'),
    
    # A view to display search results or similar data
    path('result/', views.result, name='result'),
    
    # API endpoint for listing all items or creating a new one
    path('posts/', ItemListCreateView.as_view(), name='item-list-create'),
    
    # API endpoint for retrieving, updating, or deleting a specific item by its primary key
    path('posts/<int:pk>/', ItemDetailView.as_view(), name='item-detail'),
]