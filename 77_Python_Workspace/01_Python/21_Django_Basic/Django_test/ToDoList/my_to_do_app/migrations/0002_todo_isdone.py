# Generated by Django 3.1 on 2020-08-17 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_to_do_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='isDone',
            field=models.BooleanField(default=False),
        ),
    ]
