from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import BookForm

# Create your views here.

def book_list(request):
  books = Book.objects.all()
  context = {
    'books': books
  }
  return render(request, 'books/book_list.html', context)


def book_create(request):
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
    book = get_object_or_404(Book, pk=pk)
    context = {
        'book': book
    }
    return render(request, 'books/book_detail.html', context)