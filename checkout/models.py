from django.db import models

import uuid

from django.db.models import Sum
from django.conf import settings

from resources.models import Product
from user_profiles.models import UserProfile

# Create your models here.
class Order(models.Model):
    """Set up your order model"""
    order_number = models.CharField(max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name="orders")
    full_name = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(max_length=250, blank=False, null=False)
    phone_number = models.CharField(max_length=15, null=False, blank=False)
    country = models.CharField(max_length=20, null=False, blank=False)
    postcode = models.CharField(max_length=20, null=False, blank=False)
    town_or_city = models.CharField(max_length=20, null=False, blank=False)
    street_address1 = models.CharField(max_length=20, null=False, blank=False)
    street_address2 = models.CharField(max_length=20, null=False, blank=False)
    county = models.CharField(max_length=20, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    order_total = models.DecimalField(max_digits=15, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=15, decimal_places=2, null=False, default=0)
    original_basket = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(max_length=254, null=False, blank=False, default='')

    def __str__(self):
        return self.order_number

    def _generate_order_number(self):
        """generates a random unique orer number"""
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        update grand total of order each time item is added
        accounting for delivery costs
        """
        self.order_total = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total__sum'] or 0
        if self.order_total < settings.PURCHASE_THRESHOLD:
            self.delivery_cost = self.order_total * settings.STANDARD_DELIVERY_PERC/100
        else:
            self.delivery_cost = 0
        self.grand_total = self.order_total + self.delivery_cost
        self.save()


    def save(self, *args, **kwargs):
        """override save method to set order number if not set already"""
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)


class OrderLineItem(models.Model):
    """Set up our line items for orders"""
    order = models.ForeignKey(
        Order,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name='lineitems'
    )
    product = models.ForeignKey(
        Product,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
    )
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        null=False,
        blank=False,
        editable=False
    )

    def __str__(self):
        return f'{self.product.name} on order {self.order.order_number}'
