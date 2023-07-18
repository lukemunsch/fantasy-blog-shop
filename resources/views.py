from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Product, Category

# Create your views here.
def resources(request):
    """set up shop for our resources"""
    categories = Category.objects.all()
    products = Product.objects.filter(approved_item=1)

    context = {
        'products': products,
        'categories': categories,
    }
    return render(request, 'resources/resources.html', context)

@login_required
def pending_resources(request):
    """set up page for pending resources"""
    if not request.user.is_superuser:
        messages.error(
            request,
            'You are not authorised to access this Resource!'
        )
        return redirect(reverse('home'))
    
    products = Product.objects.filter(approved_item=0)

    context = {
        'products': products,
        'from_homepage': True,
    }
    return render(request, 'resources/resources.html', context)
