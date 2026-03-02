from django.contrib import admin

from .models import Book, BookCategory


@admin.register(BookCategory)
class BookCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'published_year', 'is_active')
    list_filter = ('category', 'is_active')
    search_fields = ('title', 'author', 'description')