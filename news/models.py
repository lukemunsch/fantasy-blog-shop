from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

from personnel.models import Personnel

# Create your models here.
# ---------- set up choices for integer fields ---
TYPES = ((1, 'General'), (2, 'Systems'), (3, 'Discoveries'))
PUBLISH = ((0, 'Hidden'), (1, 'Displayed'))
class News(models.Model):
    """Setting up my model to update news"""
    title = models.CharField(max_length=150, null=False, blank=False)
    news_type = models.IntegerField(choices=TYPES, default=1)
    news_img = models.ImageField(null=True, blank=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        default='Anonymous',
        related_name='articles'
    )
    approved_post = models.IntegerField(choices=PUBLISH, default=0)
    publish_date = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)
    news_content = models.TextField(
        max_length=4000,
        null=False,
        blank=False,
        default=''
    )
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        """set up our ordering for this model"""
        ordering = ['-publish_date']
        verbose_name_plural = "News"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        """setting up the method for generating slug"""
        if not self.slug:
            self.slug = slugify(f'{self.news_type}-{self.title}')
        return super().save(*args, **kwargs)
