# Generated by Django 3.1.7 on 2021-04-11 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cav_map', '0005_remove_class_schedule'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classschedule',
            name='date_posted',
        ),
        migrations.RemoveField(
            model_name='student',
            name='email',
        ),
        migrations.AddField(
            model_name='classschedule',
            name='numClasses',
            field=models.IntegerField(default=0),
        ),
    ]