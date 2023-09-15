from django.db import models

# Create your models here.
class Order(models.Model):
    """Set up your order model"""
    order_number = models.CharField(max_length=32, null=False, editable=False)
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

    def __str__(self):
        return self.full_name
