from django.urls import path
from . import views

urlpatterns = [
    # path for listing all books
    path('', views.book_list, name='book_list'),
    path('new/', views.book_create, name='book_create'),
]