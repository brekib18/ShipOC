# Generated by Django 3.2.1 on 2021-05-10 14:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accessories', '0002_auto_20210510_1359'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accessoriesimage',
            old_name='accessory',
            new_name='accessories',
        ),
    ]
