from django.db import models


class DepartmentHead(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True)
    position = models.CharField(max_length=200)
    scientific_degree = models.CharField(max_length=200, blank=True)
    experience_years = models.PositiveIntegerField(default=0)
    bio = models.TextField(blank=True)
    image = models.ImageField(upload_to='teachers/', blank=True, null=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=30, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']
        verbose_name = "Kafedra mudiri"
        verbose_name_plural = "Kafedra mudirlari"

    def __str__(self):
        return f"{self.last_name} {self.first_name}"


class Department(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    head = models.OneToOneField(
        DepartmentHead,
        on_delete=models.PROTECT,
        related_name='department',
    )
    image = models.ImageField(upload_to='departments/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']
        verbose_name = "Kafedra"
        verbose_name_plural = "Kafedralar"

    def __str__(self):
        return self.name
