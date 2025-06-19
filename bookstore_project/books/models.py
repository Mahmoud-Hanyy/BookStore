from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Book(models.Model):
    """
    Represents a book in the bookstore with extended details.
    Each book now has a title, description, rate, and views count.
    """
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(blank=True, null=True) 
    rate = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        default=0.00,
        validators=[MinValueValidator(0.00), MaxValueValidator(5.00)] # Ensures rate is between 0 and 5
    )
    views = models.IntegerField(default=0)
    def __str__(self):
        """
        Returns a string representation of the book,
        useful for the Django admin site and debugging.
        """
        return self.title

    class Meta:
        ordering = ['title']
