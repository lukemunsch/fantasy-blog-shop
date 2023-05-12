from django.db import models
from django.template.defaultfilters import slugify
from django.utils.crypto import get_random_string


def unique_member_id():
    random_id = int(get_random_string(10, allowed_chars='0123456789'))
    return random_id

RANK = ((1, "Rookie"), (2, "Soldier"), (3, "Veteran"), (4, "Commander"),)
STATUSES = ((1, "Active"), (2, "Leave"), (3, "Medical Leave"), (4, "Retired"), (5, "Deceased"))
# Create your models here.
class Personnel(models.Model):
    """Set up model for our team members"""
    name = models.CharField(max_length=100, null=False, blank=False, unique=True)
    age = models.PositiveIntegerField(default=0)
    originated_from = models.CharField(max_length=100, null=False, blank=False)
    rank = models.PositiveIntegerField(choices=RANK, default=1)
    speciality = models.TextField(default="", max_length=1000)
    current_status = models.PositiveIntegerField(choices=STATUSES, default=1)
    joined = models.DateField(auto_now=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    profile_image = models.ImageField(null=True, blank=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        """set up hoe the personnel is ordered"""
        ordering = ['rank', 'name']
        verbose_name_plural = "Personnel"

    def __str__(self):
        """set up how we display choices"""
        return self.name

    def save(self, *args, **kwargs):
        """setting up the method for generating slug"""
        if not self.slug:
            self.slug = slugify(f'{self.name}-{self.originated_from}-{self.age}')
        return super().save(*args, **kwargs)
