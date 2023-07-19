from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models.functions import Lower

from .models import Product, Category

# Create your views here.
def resources(request):
    """set up shop for our resources"""
    categories = Category.objects.all()
    products = Product.objects.filter(approved_item=1)

    sort = None
    direction = None
    cat = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(
                    lower_name=Lower('name')
                )
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            cat = request.GET['category']
            products = products.filter(category__name=cat)
            cat = Category.objects.filter(name=cat)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'categories': categories,
        'cat': cat,
        'current_sorting': current_sorting,
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

    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(
                    lower_name=Lower('name')
                )
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'from_homepage': True,
        'current_sorting': current_sorting,
    }
    return render(request, 'resources/resources.html', context)
