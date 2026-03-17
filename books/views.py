from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import BookForm
from .models import Book

@login_required
def book_list(request):
    books = Book.objects.filter(user=request.user)
    context = {
        'books': books,
        'title': 'Список книг'
    }
    return render(request, 'books/book_list.html', context)


@login_required
def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.user = request.user
            book.save()
            return redirect('book_list')
    else:
        form = BookForm()
    context = {
        'form': form
    }
    return render(request, 'books/book_form.html', context)


@login_required
def book_toggle(request, pk):
    book = get_object_or_404(Book, pk=pk, user=request.user)
    book.status = not book.status
    book.save()
    return redirect('book_list')

@login_required
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk, user=request.user)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return redirect('book_list')