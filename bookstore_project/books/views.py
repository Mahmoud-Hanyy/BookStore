from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import BookForm

def book_list(request):
    """
    Retrieves all Book objects from the database and
    renders them in a template.
    """
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, 'books/book_list.html', context)

def book_create(request):
    """
    Handles creating a new book.
    If it's a GET request, it displays an empty form.
    If it's a POST request, it processes the form submission.
    """
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()

    context = {
        'form': form,
        'form_title': 'Add New Book'
    }
    return render(request, 'books/book_form.html', context)

def book_detail(request, pk):
    """
    Retrieves a single Book object by its primary key (pk) and
    renders its details in a template.
    Returns a 404 error if the book is not found.
    """
    book = get_object_or_404(Book, pk=pk)
    context = {
        'book': book
    }
    return render(request, 'books/book_detail.html', context)

def book_update(request, pk):
    """
    Handles updating an existing book.
    If it's a GET request, it displays the form pre-filled with book data.
    If it's a POST request, it processes the updated form submission.
    """
    book = get_object_or_404(Book, pk=pk)

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_detail', pk=book.pk)
    else:
        form = BookForm(instance=book)

    context = {
        'form': form,
        'form_title': f'Edit Book: {book.title}'
    }
    return render(request, 'books/book_form.html', context)

def book_delete(request, pk):
    """
    Handles deleting a specific book.
    Only processes POST requests for deletion (to prevent accidental deletion via GET).
    """
    book = get_object_or_404(Book, pk=pk)

    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    # If a GET request comes to this, we just redirect back to detail page.
    # For production, a dedicated confirmation page is often better.
    return redirect('book_detail', pk=pk)