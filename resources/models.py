from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
CATEGORY = ((0, 'Mineral'), (1, 'Food'), (2, 'Material'), (3, 'Fabric'))
PUBLISH = ((0, 'Hidden'), (1, 'Displayed'))
class Products(models.Model):
    """set up model for our resources"""
    name = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        unique=True
    )
    description = models.TextField(max_length=200, null=False, blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.PositiveIntegerField(choices=CATEGORY, default=0)
    approved_item = models.PositiveIntegerField(choices=PUBLISH, default=0)
    slug = models.SlugField(max_length=254, unique=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f'{self.category}-{self.name}')
        return super().save(*args, **kwargs)
