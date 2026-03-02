from django.shortcuts import get_object_or_404, render

from .models import Book


def book_list(request):
    items = Book.objects.filter(is_active=True).select_related('category')
    return render(request, 'library/book_list.html', {'books': items})


def book_detail(request, pk):
    item = get_object_or_404(Book.objects.select_related('category'), pk=pk, is_active=True)
    return render(request, 'library/book_detail.html', {'book': item})