# Generated by Django 3.2 on 2023-05-14 18:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personnel', '0005_remove_personnel_member_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='personnel',
            options={'ordering': ['-rank', 'name'], 'verbose_name_plural': 'Personnel'},
        ),
    ]
