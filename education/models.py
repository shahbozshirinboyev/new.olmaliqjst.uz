from django.db import models
from departments.models import Department
from django.core.exceptions import ValidationError


class EducationDirection(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='education/directions/', blank=True, null=True)
    duration_years = models.PositiveSmallIntegerField(default=2)
    departments = models.ManyToManyField(Department, related_name='education_directions', blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['name']
        verbose_name = "Ta'lim yo'nalishi "
        verbose_name_plural = "Ta'lim yo'nalishlari "

    def __str__(self):
        return self.name


class EducationProcess(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='education/process/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "O'quv jarayoni "
        verbose_name_plural = "O'quv jarayoni "

    def __str__(self):
        return self.title


class Assessment(models.Model):
    title = models.CharField(max_length=200, blank=True)
    content = models.TextField(blank=True)
    image = models.ImageField(upload_to='education/assessment/', blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        if not self.title and not self.content and not self.image:
            raise ValidationError("Title, Content yoki Image dan kamida bittasi bo‘lishi kerak")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Baholash "
        verbose_name_plural = "Baholash "

    def __str__(self):
        return self.title or "No title"


class Control(models.Model):
    title = models.CharField(max_length=200, blank=True)
    content = models.TextField(blank=True)
    image = models.ImageField(upload_to='education/control/', blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        if not self.title and not self.content and not self.image:
            raise ValidationError("Title, Content yoki Image dan kamida bittasi bo‘lishi kerak")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Nazorat "
        verbose_name_plural = "Nazorat "

    def __str__(self):
        return self.title or "No title"


class Practice(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    partner_name = models.CharField(max_length=200, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Amaliyot "
        verbose_name_plural = "Amaliyot "

    def __str__(self):
        return self.title
