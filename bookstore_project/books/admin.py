# books/admin.py

from django.contrib import admin
from .models import Book, Category, ISBN # Import all your models

# Register Category model simply
admin.site.register(Category)

# Inline for ISBN to be displayed within the Book admin form
class ISBNInline(admin.StackedInline):
    """
    Defines an inline form for the ISBN model to be used within the Book admin.
    StackedInline displays fields vertically.
    """
    model = ISBN
    # Explicitly specify the field linking ISBN back to Book.
    # This is crucial when the OneToOneField is not also the primary_key.
    fk_name = 'book'
    can_delete = False
    verbose_name_plural = 'ISBN Details'

# Customize the Book model's admin interface
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """
    Customizes how the Book model is displayed and manipulated in the Django admin.
    """
    list_display = ('title', 'author', 'price', 'rate', 'views', 'user', 'display_categories', 'display_isbn_number')
    list_filter = ('author', 'rate', 'categories', 'user')
    search_fields = ('title', 'author', 'description', 'isbn_details__isbn_number') # Access via related_name

    fieldsets = (
        (None, {
            'fields': ('title', 'author', 'price', 'description')
        }),
        ('Ratings & Usage', {
            'fields': ('rate', 'views'),
            'classes': ('collapse',)
        }),
        ('Relationships', {
            'fields': ('user', 'categories'),
        }),
    )

    inlines = [ISBNInline]

    def save_model(self, request, obj, form, change):
        if not obj.pk: # Only set user for newly created objects
            if obj.user is None: # Only if user hasn't been explicitly set
                obj.user = request.user
        super().save_model(request, obj, form, change)

    def display_categories(self, obj):
        return ", ".join([category.name for category in obj.categories.all()])
    display_categories.short_description = 'Categories'

    def display_isbn_number(self, obj):
        # Access the ISBN details via the related_name 'isbn_details'
        # Also, check if the isbn_details object exists before accessing its number
        return obj.isbn_details.isbn_number if hasattr(obj, 'isbn_details') else 'N/A'
    display_isbn_number.short_description = 'ISBN'

