from django.shortcuts import render

from .models import Product, Category

# Create your views here.
def resources(request):
    """set up shop for our resources"""
    categories = Category.objects.all()
    products = Product.objects.all()

    context = {
        'products': products,
        'categories': categories,
    }
    return render(request, 'resources/resources.html', context)
