from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path('profile',views.profile, name='profile'),

    path('nyskraning', views.register, name="register"),
    path('innskra', LoginView.as_view(template_name='user/login.html'), name='login'),
    path('utskra', LogoutView.as_view(next_page='login'), name='logout')

]