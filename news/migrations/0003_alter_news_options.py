# Generated by Django 3.2 on 2023-05-22 21:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20230519_1307'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['-updated_on', '-publish_date'], 'verbose_name_plural': 'News'},
        ),
    ]
