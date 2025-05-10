from django.urls import path
from books import views 

urlpatterns = [
    path('Books/', views.books_list, name='books list'),
]