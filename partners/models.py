from django.db import models


class PartnerCategory(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ['name']
        verbose_name = "Hamkor kategoriyasi"
        verbose_name_plural = "Hamkor kategoriyalari"

    def __str__(self):
        return self.name


class Partner(models.Model):
    category = models.ForeignKey(PartnerCategory, on_delete=models.CASCADE, related_name='partners')
    name = models.CharField(max_length=255)
    website = models.URLField(blank=True)
    logo = models.ImageField(upload_to='partners/', blank=True, null=True)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['name']
        verbose_name = "Hamkor"
        verbose_name_plural = "Hamkorlar"

    def __str__(self):
        return self.name