from django.contrib import admin
from django.utils.html import format_html

from .models import Assessment, EducationDirection, EducationProcess, Practice


@admin.register(EducationDirection)
class EducationDirectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'duration_years', 'is_active', 'image')
    list_filter = ('is_active', 'departments')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(EducationProcess)
class EducationProcessAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_preview', 'created_at', 'updated_at')
    search_fields = ('title', 'content')
    readonly_fields = ('image_preview', 'created_at', 'updated_at')

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="height: 48px; width: auto; border-radius: 6px;" />', obj.image.url)
        return "Rasm yo'q"

    image_preview.short_description = 'Rasm'


@admin.register(Assessment)
class AssessmentAdmin(admin.ModelAdmin):
    list_display = ('title', 'updated_at')
    search_fields = ('title', 'content')


@admin.register(Practice)
class PracticeAdmin(admin.ModelAdmin):
    list_display = ('title', 'partner_name', 'updated_at')
    search_fields = ('title', 'partner_name', 'content')
