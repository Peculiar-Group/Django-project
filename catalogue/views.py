from django.shortcuts import render
from .models import Product
from django.http import HttpResponse

def products_list(request):
    products = Product.objects.all()
    return render(request, 'products_list.html', {'products': products})

def check(request):
    return render(request,'check.html')