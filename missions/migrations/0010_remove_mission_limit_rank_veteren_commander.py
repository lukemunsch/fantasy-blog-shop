# Generated by Django 3.2 on 2023-06-01 21:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('missions', '0009_mission_limit_rank_veteren_commander'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='mission',
            name='limit_rank_Veteren_Commander',
        ),
    ]
