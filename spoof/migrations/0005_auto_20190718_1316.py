# Generated by Django 2.2.3 on 2019-07-18 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spoof', '0004_auto_20190718_1229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proxy',
            name='password',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='proxy',
            name='proxy_user',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
