"""import context requirements"""
from decimal import Decimal
from django.shortcuts import get_object_or_404
from django.conf import settings

from resources.models import Product

def basket_contents(request):
    """set up the context for our wallet"""
    basket_items = []
    total = 0
    product_count = 0

    if total < settings.PURCHASE_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERC/100)
        free_delivery_delta = settings.PURCHASE_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = total + delivery

    context = {
        'basket_items': basket_items,
        'total': total,
        'product_count': product_count,
        'PURCHASE_THRESHOLD': settings.PURCHASE_THRESHOLD,
        'delivery': delivery,
        'STANDARD_DELIVERY_PERC': settings.STANDARD_DELIVERY_PERC,
        'free_delivery_delta': free_delivery_delta,
        'grand_total': grand_total,
    }

    return context
