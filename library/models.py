from django.db import models


class BookCategory(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ['name']
        verbose_name = "Kitob kategoriyasi"
        verbose_name_plural = "Kitob kategoriyalari"

    def __str__(self):
        return self.name


class Book(models.Model):
    category = models.ForeignKey(BookCategory, on_delete=models.CASCADE, related_name='books')
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    published_year = models.PositiveIntegerField(blank=True, null=True)
    cover_image = models.ImageField(upload_to='book_covers/', blank=True, null=True)
    pdf_file = models.FileField(upload_to='books/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['title']
        verbose_name = "Kitob"
        verbose_name_plural = "Kitoblar"

    def __str__(self):
        return self.title