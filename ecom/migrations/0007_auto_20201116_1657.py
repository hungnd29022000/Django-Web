# Generated by Django 3.1.2 on 2020-11-16 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0006_auto_20201116_1646'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='cpu',
            field=models.TextField(default='', verbose_name='CPU'),
        ),
        migrations.AddField(
            model_name='product',
            name='display',
            field=models.TextField(default='', verbose_name='Display'),
        ),
        migrations.AddField(
            model_name='product',
            name='weight',
            field=models.TextField(default='', verbose_name='Weight'),
        ),
    ]
