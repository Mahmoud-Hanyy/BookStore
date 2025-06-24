"""
URL configuration for bookstore_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from books import views as book_views # Import views from your books app for custom signup

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', include('books.urls')),
    
    # Authentication URLs provided by Django (login, logout, password reset, etc.)
    path('accounts/', include('django.contrib.auth.urls')),
    
    # Custom URL for user registration (signup)
    path('accounts/signup/', book_views.signup, name='signup'),
]
