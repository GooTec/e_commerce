# Generated by Django 2.0.7 on 2018-08-01 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20180801_1351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='fullname',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.CharField(max_length=10),
        ),
    ]
