from django.db import models
from departments.models import Department
from django.core.exceptions import ValidationError
from partners.models import Partner


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
    TYPE_CHOICES = [
        ('ishlab_chiharish', 'Ishlab chiqarish amaliyoti'),
        ('pedagogik', 'Pedagogik amaliyot'),
        ('diplom_oldi', 'Diplom oldi amaliyoti'),
    ]

    title = models.CharField(max_length=200, verbose_name='Nomi')
    description = models.TextField(verbose_name='Tavsif')
    image = models.ImageField(upload_to='education/practice/', blank=True, null=True, verbose_name='Rasm')
    partner = models.ForeignKey(
        Partner,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='practices',
        verbose_name='Hamkor tashkilot',
    )
    partner_name = models.CharField(max_length=200, blank=True, verbose_name='Hamkor nomi (qo\'lda)')
    practice_type = models.CharField(max_length=30, choices=TYPE_CHOICES, blank=True, verbose_name='Amaliyot turi')
    period = models.CharField(max_length=50, blank=True, verbose_name='Davr')
    sort_order = models.PositiveSmallIntegerField(default=0, verbose_name='Tartib')
    is_active = models.BooleanField(default=True, verbose_name='Ko\'rsatilsin')
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['sort_order', '-updated_at']
        verbose_name = 'Amaliyot'
        verbose_name_plural = 'Amaliyotlar'

    def __str__(self):
        return self.title

    @property
    def partner_display(self):
        return self.partner.name if self.partner else self.partner_name


class Graduate(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='Ism')
    last_name = models.CharField(max_length=100, verbose_name='Familiya')
    middle_name = models.CharField(max_length=100, blank=True, verbose_name='Otasining ismi')
    image = models.ImageField(upload_to='education/graduates/', blank=True, null=True, verbose_name='Rasm')
    graduation_year = models.PositiveSmallIntegerField(verbose_name='Bitirgan yili')
    direction = models.ForeignKey(
        EducationDirection,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='graduates',
        verbose_name='Yo\'nalish',
    )
    bio = models.TextField(blank=True, verbose_name='Bitiruvchi haqida')
    position = models.CharField(max_length=200, blank=True, verbose_name='Hozirgi lavozimi')
    workplace = models.CharField(max_length=200, blank=True, verbose_name='Ish joyi')
    achievement = models.TextField(blank=True, verbose_name='Yutuqlari')
    quote = models.CharField(max_length=300, blank=True, verbose_name='Maslahati')
    sort_order = models.PositiveSmallIntegerField(default=0, verbose_name='Tartib')
    is_active = models.BooleanField(default=True, verbose_name='Ko\'rsatilsin')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['sort_order', '-graduation_year', 'last_name']
        verbose_name = 'Bitiruvchi'
        verbose_name_plural = 'Bitiruvchilar'

    def __str__(self):
        return self.full_name

    @property
    def full_name(self):
        return ' '.join(part for part in (self.last_name, self.first_name, self.middle_name) if part).strip()
