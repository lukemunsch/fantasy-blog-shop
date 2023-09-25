from django.shortcuts import render, redirect, reverse, get_object_or_404

from django.contrib import messages
from django.conf import settings

from basket.contexts import basket_contents

import stripe

from .forms import OrderForm

# Create your views here.
def checkout(request):
    """set up our checkout view"""
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    basket = request.session.get('basket', {})

    if not basket:
        messages.error(
            request,
            "There's nothing in your basket currently!"
        )
    order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(
            request,
            'Your public key is missing; Did you forget to '
            'set it in your environment?'
        )

    current_basket = basket_contents(request)
    total = current_basket['grand_total']
    stripe_total = round(total * 100)

    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }
    return render(request, 'checkout/checkout.html', context)
