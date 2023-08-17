from django.shortcuts import render, redirect

# Create your views here.
def view_basket(request):
    """Set up a view to display our shaopping basket"""
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
    print(request.session['basket'])
    return redirect(redirect_url)
