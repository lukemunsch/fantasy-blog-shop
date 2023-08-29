from django.shortcuts import (
    render,
    redirect,
    reverse,
    get_object_or_404
)

from django.contrib import messages

from resources.models import Product

# Create your views here.


def view_basket(request):
    """Set up a view to display our shopping basket"""
    return render(request, 'basket/basket.html')

# Set up our shopping basket functionality


def add_to_basket(request, product_id):
    """Add a quantity for a specific product to shopping basket"""
    quantity = int(request.POST.get('quantity'))

    redirect_url = request.POST.get('redirect_url')

    basket = request.session.get('basket', {})

    if product_id in list(basket.keys()):
        basket[product_id] += quantity
    else:
        basket[product_id] = quantity

    request.session['basket'] = basket

    return redirect(redirect_url)


def update_basket(request, product_id):
    """set up our view for updating basket products"""
    product = get_object_or_404(Product, id=product_id)
    quantity = int(request.POST.get('quantity'))
    basket = request.session.get('basket', {})

    if quantity > 0:
        basket[product_id] = quantity
        messages.success(
            request,
            f'we have updated {product.name} ' 
            f'quantity to {basket[product_id]}'
        )
    else:
        basket.pop(product_id)
        messages.error(
            request,
            f'We have removed {product.name} '
            f'from your basket'
        )

    request.session['basket'] = basket

    return redirect(reverse('view_basket'))
