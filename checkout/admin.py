from django.contrib import admin

from checkout.models import Order, OrderLineItem

# Register your models here.
class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    """set up the admin for order model"""
    readonly_fields = ('order_number', 'date', 'delivery_cost',
                       'order_total', 'grand_total',)
    inlines = (OrderLineItemAdminInline,)
    fields = ('order_number', 'date', 'full_name', 'email', 'phone_number',
              'town_or_city', 'street_address1', 'street_address2', 'county',
              'delivery_cost', 'order_total', 'grand_total',)
    list_display = ('order_number', 'date', 'full_name',
                    'order_total', 'delivery_cost', 'grand_total',)

admin.site.register(Order, OrderAdmin)
