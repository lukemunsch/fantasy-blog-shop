from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.

PUBLISH = ((0, 'Hidden'), (1, 'Displayed'))

class Category(models.Model):
    """set up our model for th categories of our"""
    name = models.CharField(max_length=50, null=False, blank=False)
    friendly_name = models.CharField(max_length=50, null=False, blank=False)

    class Meta:
        """set up extra model settings"""
        verbose_name_plural = 'Categories'

    def __str__(self) -> str:
        return self.name

    def get_friendly_name(self):
        """function for returning the 
        friendly name instead of original name"""
        return self.friendly_name

class Product(models.Model):
    """set up model for our resources"""
    name = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        unique=True
    )
    description = models.TextField(max_length=200, null=False, blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    approved_item = models.PositiveIntegerField(choices=PUBLISH, default=0)
    slug = models.SlugField(max_length=254, unique=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        """overriding the save function to create our slug"""
        if not self.slug:
            self.slug = slugify(f'{self.category}-{self.name}')
        return super().save(*args, **kwargs)
