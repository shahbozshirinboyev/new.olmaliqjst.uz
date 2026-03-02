from django.contrib import admin

from .models import Department


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'head_name', 'phone', 'email')
    search_fields = ('name', 'head_name', 'description')
    prepopulated_fields = {'slug': ('name',)}