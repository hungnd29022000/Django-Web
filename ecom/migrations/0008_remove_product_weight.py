# Generated by Django 3.1.2 on 2020-11-16 09:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0007_auto_20201116_1657'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='weight',
        ),
    ]