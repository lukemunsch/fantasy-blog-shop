from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField

from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    """set up our customer profile to 
    attach orders and store user preferences"""
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    default_phone_number = models.CharField(
        max_length=20, null=True, blank=True
    )
    default_town_or_city = models.CharField(
        max_length=50,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """handle the creation or update of a user profile"""
    if created:
        UserProfile.objects.create(user=instance)
        # Exising user: just save the profile
    instance.userprofile.save()
