# Generated by Django 3.2.1 on 2021-05-14 17:36

import buy.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cereal', '0003_alter_cereal_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='BillingInfos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=256)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('zip_code', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('active', models.BooleanField(default=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentInfos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('card_number', models.DecimalField(decimal_places=0, max_digits=16, validators=[buy.models.credidcardcheck])),
                ('exp_month', models.DecimalField(decimal_places=0, max_digits=2, validators=[buy.models.exp_monthcheck])),
                ('exp_year', models.DecimalField(decimal_places=0, max_digits=2, validators=[buy.models.exp_yearcheck])),
                ('cvv', models.DecimalField(decimal_places=0, max_digits=3, validators=[buy.models.cvv_check])),
                ('active', models.BooleanField(default=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=0, max_digits=2)),
                ('step', models.CharField(default='billing', max_length=255)),
                ('billing_info', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='buy.billinginfos')),
                ('ordered_products', models.ManyToManyField(to='cereal.Cereal')),
                ('payment_info', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='buy.paymentinfos')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
