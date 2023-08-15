"""import context requirements"""
from decimal import Decimal
from django.conf import settings


def basket_contents(request):
    """set up a context file for basket"""
    basket_items = []
    total = 0
    product_count = 0
    delivery = 0

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
        'free_delivery_delta': free_delivery_delta,
        'purchase_threshold': settings.PURCHASE_THRESHOLD,
        'grand_total': grand_total,
        'standard_delivery_perc': settings.STANDARD_DELIVERY_PERC,
    }
    return context
