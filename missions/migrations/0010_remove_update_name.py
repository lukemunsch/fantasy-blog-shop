# Generated by Django 3.2 on 2023-06-20 10:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('missions', '0009_alter_update_mission'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='update',
            name='name',
        ),
    ]
