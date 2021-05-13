from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="accessories-index"),
    path('<int:id>',views.get_accessories_by_id,name="accessories-details"),
    path('create_accessories', views.create_accessories, name="create_accessories"),
    path('delete_accessories/<int:id>', views.delete_accessories, name="delete_accessories"),
    path('update_accessories/<int:id>', views.update_accessories, name="update_accessories")
]