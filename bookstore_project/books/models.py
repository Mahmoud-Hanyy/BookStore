# books/models.py

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator, MaxLengthValidator
from django.contrib.auth.models import User # Import Django's built-in User model

class Category(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True,
        validators=[
            MinLengthValidator(2, 'Category name must be at least 2 characters long.')
        ]
    )

    class Meta:
        verbose_name_plural = "Categories" # Correct plural name for admin
        ordering = ['name'] # Order categories alphabetically

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(
        max_length=50,
        validators=[
            MinLengthValidator(10, 'Book title must be at least 10 characters long.'),
            MaxLengthValidator(50, 'Book title cannot exceed 50 characters.')
        ]
    )
    author = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    rate = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        default=0.00,
        validators=[MinValueValidator(0.00), MaxValueValidator(5.00)]
    )
    views = models.IntegerField(default=0)

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='books_created')
    categories = models.ManyToManyField(Category, blank=True, related_name='books')

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

class ISBN(models.Model):
    """
    Represents an ISBN for a book.
    Each ISBN is unique and associated with one book via a OneToOneField.
    """
    # CRITICAL CHANGE: Removed primary_key=True from here.
    # Django will now automatically create an 'id' primary key for ISBN,
    # and the 'book' field will explicitly create a 'book_id' foreign key column.
    book = models.OneToOneField(
        Book,
        on_delete=models.CASCADE,
        related_name='isbn_details' # Still using this related_name for accessing ISBN from Book
    )
    author_title = models.CharField(max_length=100, help_text="Title used for author in ISBN database")
    book_title = models.CharField(max_length=200, help_text="Title of the book as per ISBN record")
    isbn_number = models.CharField(max_length=13, unique=True, help_text="Unique 13-digit ISBN")

    def __str__(self):
        # Ensure we check if book exists before accessing its title (e.g., if ISBN is orphaned)
        return f"ISBN: {self.isbn_number} for {self.book.title if self.book else 'N/A'}"

