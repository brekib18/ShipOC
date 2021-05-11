from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="books-index"),
    path('<int:id>',views.get_book_by_id,name="books-details")
]