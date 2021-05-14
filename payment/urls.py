from django.urls import path
from . import views

urlpatterns = [
    path('billings/', views.billing_info, name="payment-billing_addresss"),
    path('payment_infos/', views.payment_info, name='payment-payment_infos'),
    path('overviews/', views.order_overview, name='payment-overviews'),
    path('confirmations/', views.confirmation, name='payment-confirmations')
]