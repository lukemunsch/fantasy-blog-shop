# Generated by Django 3.2 on 2023-07-05 19:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0007_alter_news_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='author',
            field=models.ForeignKey(default='Anonymous', on_delete=django.db.models.deletion.CASCADE, related_name='articles', to=settings.AUTH_USER_MODEL),
        ),
    ]
