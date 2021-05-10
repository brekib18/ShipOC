from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accessories', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AccsessoryCategory',
            new_name='AccessoriesCategory',
        ),
        migrations.RenameModel(
            old_name='AccerssoryImage',
            new_name='AccessoriesImage',
        ),
        migrations.RenameField(
            model_name='accessoriesimage',
            old_name='accsessory',
            new_name='accessory',
        ),
    ]