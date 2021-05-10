from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clothes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(blank=True, max_length=255)),
                ('price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='ClothesCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ClothesImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(max_length=9999)),
                ('clothes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clothes.clothes')),
            ],
        ),
        migrations.AddField(
            model_name='clothes',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clothes.clothescategory'),
        ),
    ]