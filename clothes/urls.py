from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name = "clothes-index"),
    path('<int:id>', views.get_clothes_by_id, name="clothes-details")
]

