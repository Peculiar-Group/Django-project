from django.urls import path
from . import views
from .views import products_list, product_details

urlpatterns = [
    path('', products_list, name='products_list'),
    path('products/<int:product_id>/',product_details, name='product-details'),
]
