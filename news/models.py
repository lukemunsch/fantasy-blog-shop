from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

from personnel.models import Personnel

# Create your models here.
# ---------- set up choices for integer fields ---
TYPES = ((1, 'General'), (2, 'Systems'), (3, 'Discoveries'))
GRADES = (
    (1, 'Extreme'),
    (2, 'Dangerous'),
    (3, 'Serious'),
    (4, 'Moderate'),
    (5, 'Basic'),
    (6, 'Training')
)
class News(models.Model):
    """Setting up my model to update news"""
    title = models.CharField(max_length=150, null=False, blank=False)
    news_type = models.IntegerField(choices=TYPES, default=1)
    news_img = models.ImageField(null=True, blank=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=False,
        blank=False
    )
    publish_date = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)
    news_content = models.TextField(
        max_length=2000,
        null=False,
        blank=False,
        default='Add content here'
    )
    slug = models.SlugField(max_length=254, unique=True)

    class Meta:
        """set up our ordering for this model"""
        ordering = ['updated_on', 'publish_date']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        """set up our slug creation"""
        if not self.slug:
            self.slug = slugify(f'{self.news_type}-{self.publish_date}')
        return super().save(*args, **kwargs)
