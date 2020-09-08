from django.urls import path
from . import views
from .views import products_list, check

urlpatterns = [
    path('products/', products_list, name='products_list'),
    path('check/', check, name='check'),
]
