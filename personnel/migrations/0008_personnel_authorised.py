# Generated by Django 3.2 on 2023-06-09 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personnel', '0007_alter_personnel_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='personnel',
            name='authorised',
            field=models.PositiveIntegerField(choices=[(0, 'Hidden'), (1, 'Shown')], default=0),
        ),
    ]
