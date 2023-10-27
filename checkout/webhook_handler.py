from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

from .models import Order, OrderLineItem
from user_profiles.models import UserProfile
from resources.models import Product

import json
import time

import stripe

class StripeWH_Handler:
    """handle stripe webhooks"""
    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, order):
        """send the user a confirmation email about their order"""
        customer_email = order.email
        subject = render_to_string(
            'checkout/confirmation_emails/confirmation_email_subject.txt',
            {'order': order}
        )
        body = render_to_string(
            'checkout/confirmation_emails/confirmation_email_body.txt',
            {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL}
        )

        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [customer_email]
        )

    def handle_event(self, event):
        """handle generic/unknown/unexpect webhooks events"""
        return HttpResponse(
            content=f'Unhandled Webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """handle successful payment intent webhooks from stripe"""
        print("hello")
        intent = event.data.object
        print(intent)
        pid = intent.id
        print(pid)
        basket = intent.metadata.basket
        print(basket)
        save_info = intent.metadata.save_info

        # Get the Charge object
        stripe_charge = stripe.Charge.retrieve(
            intent.latest_charge
        )
        print(stripe_charge)
        billing_details = stripe_charge.billing_details
        print(billing_details)
        shipping_details = intent.shipping
        print(shipping_details)
        grand_total = round(stripe_charge.amount / 100, 2)
        print(grand_total)

        # clean data in the shopping details
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        # Update profile information if save_info was checked
        profile = None
        username = intent.metadata.username
        print(username)
        if username != 'AnonymousUser':
            profile = UserProfile.objects.get(user__username=username)
            if save_info:
                profile.default_phone_number = shipping_details.phone
                profile.default_country = shipping_details.address.country
                profile.default_postcode = shipping_details.address.postcode
                profile.default_town_or_city = shipping_details.address.city
                profile.default_street_address1 = shipping_details.address.line1
                profile.default_street_address2 = shipping_details.address.line2
                profile.default_county = shipping_details.address.state
                profile.save()
                print("saved!")

        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    full_name__iexact=shipping_details.name,
                    email__iexact=billing_details.email,
                    phone_number__iexact=shipping_details.phone,
                    country__iexact=shipping_details.address.country,
                    postcode__iexact=shipping_details.address.postcode,
                    town_or_city__iexact=shipping_details.address.city,
                    street_address1__iexact=shipping_details.address.line1,
                    street_address2__iexact=shipping_details.address.line2,
                    county__iexact=shipping_details.address.state,
                    grand_total=grand_total,
                    original_basket=basket,
                    stripe_pid=pid,
                )
                order_exists = True
                print("exists!")
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if order_exists:
            self._send_confirmation_email(order)
            print("boom!")
            return HttpResponse(
                content=(f'Webhook received: {event["type"]} | \
                        SUCCESS: Verified orer already in database'),
                status=200
            )
        else:
            order = None
            print("none!")
            try:
                order = Order.objects.create(
                    full_name=shipping_details.name,
                    user_profile=profile,
                    email=billing_details.email,
                    phone_number=shipping_details.phone,
                    country=shipping_details.address.country,
                    postcode=shipping_details.address.postal_code,
                    town_or_city=shipping_details.address.city,
                    street_address1=shipping_details.address.line1,
                    street_address2=shipping_details.address.line2,
                    county=shipping_details.address.state,
                    original_basket=basket,
                    stripe_pid=pid,
                )
                for product_id, quantity in json.loads(basket).items():
                    product = Product.objects.get(id=product_id)
                    order_line_item = OrderLineItem(
                        order=order,
                        product=product,
                        quantity=quantity,
                    )
                    order_line_item.save()
                print(order)
            except Exception as e:
                if order:
                    order.delete()
                print("deleted!")
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)

        self._send_confirmation_email(order)
        print("confirmed!")
        return HttpResponse(
            content=(f'Webhook received: {event["type"]} | SUCCESS: '
                     'Created order in webhook'),
            status=200)

    def handle_payment_intent_failed(self, event):
        """handle failed payment intent webhooks from stripe"""
        return HttpResponse(
            content=f'failed Webhook received: {event["type"]}',
            status=200)
