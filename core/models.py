from django.db import models
from django.utils import timezone


class Menu(models.Model):
    title = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    order = models.PositiveSmallIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order', 'id']
        verbose_name = "Menu"
        verbose_name_plural = "Menular"

    def __str__(self):
        return self.title


class About(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='about/', blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Texnikum haqida"
        verbose_name_plural = "Texnikum haqida"

    def __str__(self):
        return self.title


class Leadership(models.Model):
    full_name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    bio = models.TextField(blank=True)
    image = models.ImageField(upload_to='leadership/', blank=True, null=True)
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ['order', 'id']
        verbose_name = "Rahbariyat"
        verbose_name_plural = "Rahbariyat"

    def __str__(self):
        return f"{self.full_name} - {self.position}"


class MaterialBase(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='about/', blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Moddiy texnik baza"
        verbose_name_plural = "Moddiy texnik baza"

    def __str__(self):
        return self.title


class Document(models.Model):
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='documents/')
    description = models.TextField(blank=True)
    published_at = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Hujjat"
        verbose_name_plural = "Hujjatlar"

    def __str__(self):
        return self.title


class TopbarSettings(models.Model):
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=50, blank=True)
    telegram_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    youtube_url = models.URLField(blank=True)
    is_active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated_at', '-id']
        verbose_name = "Topbar sozlamasi"
        verbose_name_plural = "Topbar sozlamalari"

    def __str__(self):
        return self.email or self.phone or f"Topbar #{self.pk}"


class TechStat(models.Model):
    icon = models.CharField(max_length=50, help_text="Masalan: bi-bank")
    count = models.CharField(max_length=30, help_text="Masalan: 770+")
    name = models.CharField(max_length=120)
    order = models.PositiveSmallIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order', 'id']
        verbose_name = "Texnikum raqami"
        verbose_name_plural = "Texnikum raqamlari"

    def __str__(self):
        return f"{self.count} - {self.name}"


class Announcement(models.Model):
    title = models.CharField(max_length=220)
    content = models.TextField()
    image = models.ImageField(upload_to='announcements/', blank=True, null=True)
    published_at = models.DateField(default=timezone.localdate)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-published_at', '-created_at']
        verbose_name = "E'lon"
        verbose_name_plural = "E'lonlar"

    def __str__(self):
        return self.title
