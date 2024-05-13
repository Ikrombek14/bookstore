from django.urls import path
from .views import *


urlpatterns = [
    path('', home_page, name='home_page'),
    path('register/', SignUpView.as_view(), name='signup'),
    path('login/', login_page, name='login_page'),
    path('logout/', log_out, name='log_out'),


    path('book/<int:pk>/', book_detail, name='book_detail'),
    path('add_book/', CreateBookView.as_view(), name='add_book'),
    path('update_book/<int:pk>/', UpdateBookView.as_view(), name='update_book'),
    path('delete_book/<int:pk>/', delete_book, name='delete_book'),

]