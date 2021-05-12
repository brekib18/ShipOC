from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="urls-index"),
    path('profile',views.profile, name='profile')
]