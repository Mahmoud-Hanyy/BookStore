from django.urls import path
from . import views

urlspatterns = [
  path('', views.book_list, name='book_list')
]
