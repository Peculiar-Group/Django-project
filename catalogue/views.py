from django.shortcuts import render
from .models import Product
from django.http import HttpResponse

def products_list(request):
    products = Product.objects.all()
    return render(request, 'products_list.html', {'products': products})



def product_details(request, product_id):
    product = Product.objects.get(id=product_id)
    # images = product.images.all()
    return render(request,'product_details.html', {'product':product})