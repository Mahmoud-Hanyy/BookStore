from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, Category, ISBN
from .forms import BookForm, CustomUserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required # Import the decorator

def book_list(request):
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, 'books/book_list.html', context)

@login_required # This view now requires a user to be logged in
def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book_instance = form.save(commit=False)
            if request.user.is_authenticated and not book_instance.user:
                book_instance.user = request.user
            book_instance.save()
            form.save_m2m() # Save ManyToMany fields after the instance is saved
            return redirect('book_list')
    else:
        initial_data = {}
        if request.user.is_authenticated:
            # Pre-select the current user for the 'user' field in the form
            initial_data['user'] = request.user
        form = BookForm(initial=initial_data)

    context = {
        'form': form,
        'form_title': 'Add New Book'
    }
    return render(request, 'books/book_form.html', context)

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    context = {
        'book': book
    }
    return render(request, 'books/book_detail.html', context)

@login_required # This view now requires a user to be logged in
def book_update(request, pk):
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

@login_required # This view now requires a user to be logged in
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return redirect('book_detail', pk=pk)

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('book_list')
    else:
        form = CustomUserCreationForm()
    context = {'form': form}
    return render(request, 'registration/signup.html', context) 