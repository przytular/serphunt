# Generated by Django 2.2.3 on 2019-07-18 14:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spoof', '0005_auto_20190718_1316'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='proxy',
            unique_together={('host', 'port')},
        ),
    ]
