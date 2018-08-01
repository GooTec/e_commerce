# Generated by Django 2.0.7 on 2018-08-01 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='maing_img',
            new_name='main_img',
        ),
        migrations.AddField(
            model_name='product',
            name='name',
            field=models.CharField(default='거문고', max_length=20),
        ),
        migrations.AddField(
            model_name='profile',
            name='address',
            field=models.CharField(default=None, max_length=40),
        ),
        migrations.AddField(
            model_name='profile',
            name='address_detail',
            field=models.CharField(default=None, max_length=40),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Gu', '거문고'), ('Hae', '해금'), ('Ah', '아쟁'), ('Ga', '가야금'), ('Dae', '대금'), ('etc', '소품')], default='Gu', max_length=10),
        ),
    ]