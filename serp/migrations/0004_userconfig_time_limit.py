# Generated by Django 2.2.3 on 2019-07-15 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serp', '0003_auto_20190713_1156'),
    ]

    operations = [
        migrations.AddField(
            model_name='userconfig',
            name='time_limit',
            field=models.IntegerField(default=300),
        ),
    ]
