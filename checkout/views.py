from django.shortcuts import render, redirect, reverse, get_object_or_404

from django.contrib import messages
from django.conf import settings

from basket.contexts import basket_contents
import stripe
from .forms import OrderForm
from resources.models import Product
from .models import Order, OrderLineItem



# Create your views here.
def checkout(request):
    """set up our checkout view"""
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        basket = request.session.get('basket', {})
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'postcode': request.POST['postcode'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
            'town_or_city': request.POST['town_or_city'],
            'country': request.POST['country'],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save()
            for product_id, quantity in basket.items():
                try:
                    product = Product.objects.get(id=product_id)
                    order_line_item = OrderLineItem(
                        order=order,
                        product=product,
                        quantity=quantity,
                    )
                    order_line_item.save()

                except Product.DoesNotExist:
                    messages.error(
                        request, (
                            "One of the products in your basket "
                            "wasn't found in our database - "
                            "Please call us for assistance!"
                        )
                    )
                    order.delete()
                    return redirect(reverse('view_basket'))
                
            request.session['save-info'] = 'save-info' in request.POST
            return redirect(reverse(
                'checkout_success',
                args=[order.order_number]
            ))
        else:
            messages.error(
                request, (
                'There was a problem with your form - '
                'Please double-check your information.'
            ))

    else:
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


def checkout_success(request, order_number):
    """create a view for when our checkout is successful"""
    save_info = request.session.get('save-info')
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(
        request,
        (f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}')
    )
    if 'basket' in request.session:
        del request.session['basket']

    context = {
        'order': order,
    }

    return render(request, 'checkout/checkout_success.html', context)
