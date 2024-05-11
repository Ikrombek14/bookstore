from django.urls import path
from .views import ListView, BookDetailView, CreateBookView, UpdateBookView, DeleteBookView


urlpatterns = [

    path('', ListView.as_view(), name='index'),
    path('book/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('add_book/', CreateBookView.as_view(), name='add_book'),
    path('update_book/<int:pk>/', UpdateBookView.as_view(), name='update_book'),
    path('delete_book/<int:pk>/', DeleteBookView.as_view(), name='delete_book'),

]