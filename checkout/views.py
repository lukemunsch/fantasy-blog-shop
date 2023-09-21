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
        'stripe_public_key': 'pk_test_51KfrxTCFZ5MUgwOyPW7N4O2Hi881agVemSpuiBBg5chjcX3ghQSxGCq7CpXjoy0cr96cCylYXHyC800UpA94FKTG00kE2WsDgt',
        'client_secret': 'test client secret',
    }
    return render(request, 'checkout/checkout.html', context)
