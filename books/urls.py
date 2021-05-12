from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="books-index"),
    path('<int:id>',views.get_book_by_id, name="books-details"),
    path('create_book', views.create_book, name="create_book"),
    path('delete_book/<int:id>', views.delete_book, name="delete_book"),
    path('update_book/<int:id>', views.update_book, name="update_book")
]