from django.shortcuts import get_object_or_404, render

from .models import Category, Product
from quoteapi.views import *
import requests

def product_all(request):
        response = requests.request("GET", url, headers=headers).json()
        formatted_quote_content = response['content']
        formatted_quote_originator = response['originator']['name']
        formatted_quote = f'"{formatted_quote_content}" - by {formatted_quote_originator}'
        products = Product.products.all()
        return render(request, 'store/home.html',{'response':formatted_quote,'products': products})


def category_list(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'store/products/category.html', {'category': category, 'products': products})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'store/products/single.html', {'product': product})