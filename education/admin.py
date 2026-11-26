from django.contrib import admin
from django.utils.html import format_html

from .models import Assessment, Control, EducationDirection, EducationProcess, Graduate, Practice


class ImagePreviewMixin:
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="height: 64px; width: auto; border-radius: 6px;" />', obj.image.url)
        return "Rasm yo'q"

    image_preview.short_description = 'Rasm'


@admin.register(EducationDirection)
class EducationDirectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'duration_years', 'is_active', 'image')
    list_filter = ('is_active', 'departments')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(EducationProcess)
class EducationProcessAdmin(ImagePreviewMixin, admin.ModelAdmin):
    list_display = ('title', 'image_preview', 'created_at', 'updated_at')
    search_fields = ('title', 'content')
    readonly_fields = ('image_preview', 'created_at', 'updated_at')


@admin.register(Assessment)
class AssessmentAdmin(admin.ModelAdmin):
    list_display = ('title', 'updated_at')
    search_fields = ('title', 'content')


@admin.register(Control)
class ControlAdmin(admin.ModelAdmin):
    list_display = ('title', 'updated_at')
    search_fields = ('title', 'content')


@admin.register(Practice)
class PracticeAdmin(ImagePreviewMixin, admin.ModelAdmin):
    list_display = ('title', 'practice_type', 'partner_display', 'period', 'is_active', 'image_preview', 'updated_at')
    list_filter = ('is_active', 'practice_type', 'partner')
    search_fields = ('title', 'description', 'partner_name', 'partner__name')
    readonly_fields = ('image_preview', 'updated_at')
    fields = (
        'title', 'description', 'image', 'image_preview', 'partner', 'partner_name',
        'practice_type', 'period', 'sort_order', 'is_active', 'updated_at',
    )

    @admin.display(description='Hamkor')
    def partner_display(self, obj):
        return obj.partner_display or '—'


@admin.register(Graduate)
class GraduateAdmin(ImagePreviewMixin, admin.ModelAdmin):
    list_display = ('full_name', 'graduation_year', 'direction', 'position', 'is_active', 'image_preview')
    list_filter = ('is_active', 'graduation_year', 'direction')
    search_fields = ('first_name', 'last_name', 'middle_name', 'position', 'workplace')
    readonly_fields = ('image_preview',)
    fields = (
        'first_name', 'last_name', 'middle_name', 'image', 'image_preview',
        'graduation_year', 'direction', 'bio', 'position', 'workplace',
        'achievement', 'quote', 'sort_order', 'is_active',
    )

    @admin.display(description='F.I.Sh.')
    def full_name(self, obj):
        return obj.full_name
