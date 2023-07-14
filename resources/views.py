from django.shortcuts import render

from .models import Products

# Create your views here.
def resources(request):
    """set up shop for our resources"""
    products = Products.objects.all()

    context = {
        'products': products,
    }
    return render(request, 'resources/resources.html', context)
