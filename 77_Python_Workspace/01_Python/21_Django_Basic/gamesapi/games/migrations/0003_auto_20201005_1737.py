# Generated by Django 3.1.2 on 2020-10-05 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_auto_20201005_1733'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='name',
        ),
        migrations.AddField(
            model_name='game',
            name='Sname',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
    ]
