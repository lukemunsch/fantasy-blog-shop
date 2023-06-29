
from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField

from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    """set up custom profile to attach to user
    orders and store user purchase history"""
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    default_phone_number = models.CharField(
        max_length=20,
        null=True,
        blank=True
    )
    default_town_or_city = models.CharField(
        max_length=50,
        null=True,
        blank=True
    )
    default_country = CountryField(
        blank_label='Country',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.user.username
