from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="cereal-index"),
    path('<int:id>',views.get_cereal_by_id,name="cereal-details")
]