# Generated by Django 3.2.1 on 2021-05-07 11:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cereal', '0002_rename_candy_cerealimage_cereal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cereal',
            name='on_sale',
        ),
    ]
