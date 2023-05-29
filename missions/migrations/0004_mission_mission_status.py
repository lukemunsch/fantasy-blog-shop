# Generated by Django 3.2 on 2023-05-29 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('missions', '0003_alter_mission_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='mission',
            name='mission_status',
            field=models.IntegerField(choices=[(1, 'Active'), (2, 'Completed'), (3, 'On Hold'), (4, 'Cancelled')], default=1),
        ),
    ]