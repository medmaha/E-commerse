from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404
from store.models import Category, Product

def categories(request):
    return {
        'categories': Category.objects.all()
    }


def all_products(request):
    products = Product.objects.all()
    return render(request, 'store/home.html', {
        'products_all': products,
    })


def category_list(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)

    return render(request, 'store/products/category_list.html',{
        'products': products,
        'category': category,
    })


def product_detail(request, pruduct_slug):
    product = get_object_or_404(Product, slug=pruduct_slug)

    return render(request, 'store/products/product_detail.html',{
        'product': product
    })
