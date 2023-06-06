from django.urls import path
from . import views

url_patterns = [
    path('products/', views.products_page),
    path('products/<int:my_id>/', views.dynamic_lookup_view),
    path('add-product/', views.products_create_page)
]