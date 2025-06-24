from django import forms
from .models import Book, Category # Make sure Category is imported
from django.contrib.auth.forms import UserCreationForm # Import Django's UserCreationForm

class BookForm(forms.ModelForm):
    """
    A ModelForm for the Book model, including all the extended fields
    and the user/categories relationships.
    """
    class Meta:
        model = Book
        # Ensure all fields from your Book model are listed here,
        # excluding 'isbn' as it's typically managed via admin inline or signal.
        fields = ['title', 'author', 'price', 'description', 'rate', 'views', 'user', 'categories']

class CustomUserCreationForm(UserCreationForm):
    """
    A custom user creation form that extends Django's built-in UserCreationForm.
    This form will be used for user registration (signup).
    """
    class Meta(UserCreationForm.Meta):
        # Using the default User model from Django (django.contrib.auth.models.User)
        model = UserCreationForm.Meta.model
        # Using the default fields for user creation (username, password, password confirmation)
        fields = UserCreationForm.Meta.fields