from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    head_name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='departments/', blank=True, null=True)
    phone = models.CharField(max_length=30, blank=True)
    email = models.EmailField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']
        verbose_name = "Kafedra"
        verbose_name_plural = "Kafedralar"

    def __str__(self):
        return self.name