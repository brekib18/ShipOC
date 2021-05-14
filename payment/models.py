from django.db import models
from django.contrib.auth.models import User
from cereal.models import Cereal
from django.core.exceptions import ValidationError


class BillingInfo(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    active = models.BooleanField(default=True)

def cardcheck(value):
    if len(str(value)) != 16:
        raise ValidationError('Invalid - try again')

def exp_mcheck(value):
    if value > 12:
        raise ValidationError('Invalid month')

def exp_ycheck(value):
    if len(str(value)) != 2 or int(value) < 21:
        raise ValidationError('Invalid year')

def cvc_check(value):
    if len(str(value)) != 3:
        raise ValidationError('Invalid length')

class PaymentInfo(models.Model):
    cardholder = models.CharField(max_length=255)
    card_number = models.DecimalField(max_digits=16, decimal_places=0, validators=[cardcheck])
    exp_month = models.DecimalField(max_digits=2, decimal_places=0, validators=[exp_mcheck])
    exp_year = models.DecimalField(max_digits=2, decimal_places=0, validators=[exp_ycheck])
    cvc = models.DecimalField(max_digits=3, decimal_places=0,  validators=[cvc_check])
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    active = models.BooleanField(default=True)


class Order(models.Model):
    ordered_products = models.ManyToManyField(Cereal)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    quantity = models.DecimalField(max_digits=2, decimal_places=0)
    billing_info = models.ForeignKey(BillingInfo, null=True, on_delete=models.DO_NOTHING)
    payment_info = models.ForeignKey(PaymentInfo, null=True, on_delete=models.DO_NOTHING)
    step = models.CharField(max_length=255, default="billing")

    def __str__(self):
        return self.user
