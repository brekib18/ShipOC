from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name = "clothes-index"),
    path('<int:id>', views.get_clothes_by_id, name="clothes-details"),
    path('create_clothes', views.create_clothes, name="create_clothes"),
    path('delete_clothes/<int:id>', views.delete_clothes, name="delete_clothes"),
    path('update_clothes/<int:id>', views.update_clothes, name="update_clothes")
]

