# Generated by Django 3.2.1 on 2021-05-12 17:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_cart_cartimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='category_id',
        ),
    ]
