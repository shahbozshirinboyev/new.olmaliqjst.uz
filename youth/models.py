from django.db import models


class YouthActivity(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='youth/', blank=True, null=True)
    event_date = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-event_date', '-created_at']
        verbose_name = "Yoshlar faoliyati"
        verbose_name_plural = "Yoshlar faoliyati"

    def __str__(self):
        return self.title