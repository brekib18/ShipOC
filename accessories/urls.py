from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="accessories-index"),
    path('<int:id>',views.get_accessories_by_id,name="accessories-details")
]