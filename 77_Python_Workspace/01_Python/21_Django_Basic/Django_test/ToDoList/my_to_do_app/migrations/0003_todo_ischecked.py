# Generated by Django 3.1 on 2020-08-26 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_to_do_app', '0002_todo_isdone'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='isChecked',
            field=models.BooleanField(default=False),
        ),
    ]
