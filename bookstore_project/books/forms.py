from django import forms
from .models import Book, Category # Ensure Category is imported
from django.contrib.auth.models import User # Ensure User is imported if you'll use it in forms

class BookForm(forms.ModelForm):
    # If you want to customize how User or Categories are displayed in the form,
    # you can add custom fields here. For now, ModelForm handles them.
    class Meta:
        model = Book
        # Ensure all fields are listed, excluding 'isbn' as it's now an inline/signal managed object
        fields = ['title', 'author', 'price', 'description', 'rate', 'views', 'user', 'categories']