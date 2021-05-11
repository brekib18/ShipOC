"""Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('',include('frontpage.urls')),
    path('admin/', admin.site.urls),
    path('morgunkorn/', include('cereal.urls')),
    path('fylgihlutir/', include('accessories.urls')),
    path('fot/', include('clothes.urls')),
    path('bakur/', include('books.urls')),
    path('upplysingar/', include('info.urls')),
    path('hafasamband/', include('contact.urls')),
    path('spjall/',include('chat.urls')),
    path('uppahalds/',include('favorites.urls')),
    path('karfa/',include('cart.urls')),
    path('innskraning/',include('login.urls'))
]
