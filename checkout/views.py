from django.shortcuts import render, redirect, reverse, get_object_or_404

from django.contrib import messages

from .forms import OrderForm

# Create your views here.
def checkout(request):
    basket = request.session.get('basket', {})
    if not basket:
        messages.error(
            request,
            "There's nothing in your basket currently!"
        )
    order_form = OrderForm()
    context = {
        'order_form': order_form,
    }
    return render(request, 'checkout/checkout.html', context)
