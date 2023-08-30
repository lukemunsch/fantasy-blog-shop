from django import template


register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    """work out the total price of a specific line item"""
    return price * quantity
