# Generated by Django 3.1.2 on 2020-11-16 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0005_delete_sale_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='ram',
            field=models.IntegerField(default=4, verbose_name='RAM'),
        ),
        migrations.AddField(
            model_name='product',
            name='ssd',
            field=models.IntegerField(default=0, verbose_name='SSD'),
        ),
    ]