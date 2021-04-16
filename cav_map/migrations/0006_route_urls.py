# Generated by Django 3.1.6 on 2021-04-16 19:51

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cav_map', '0005_remove_route_urls'),
    ]

    operations = [
        migrations.AddField(
            model_name='route',
            name='urls',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=500), default=[], size=None),
            preserve_default=False,
        ),
    ]
