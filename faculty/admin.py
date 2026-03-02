from django.contrib import admin

from .models import Teacher


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'department', 'position', 'experience_years')
    list_filter = ('department',)
    search_fields = ('first_name', 'last_name', 'position', 'scientific_degree')