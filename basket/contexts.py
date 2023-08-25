"""import context requirements"""
from decimal import Decimal
from django.shortcuts import get_object_or_404
from django.conf import settings

from resources.models import Product

def basket_contents(request):
    """set up the context for our wallet"""
    basket_products = []
    total = 0
    product_count = 0
    basket = request.session.get('basket', {})

    for product_id, quantity in basket.items():
        product = get_object_or_404(Product, pk=product_id)
        total += quantity * product.price
        product_count += quantity
        basket_products.append({
            'product_id': product_id,
            'quantity': quantity,
            'product': product,
        })

    if total < settings.PURCHASE_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERC/100)
        free_delivery_delta = settings.PURCHASE_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = total + delivery

    context = {
        'basket_products': basket_products,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'PURCHASE_THRESHOLD': settings.PURCHASE_THRESHOLD,
        'STANDARD_DELIVERY_PERC': settings.STANDARD_DELIVERY_PERC,
        'grand_total': grand_total,
    }

    return context
