from django.contrib import admin

from .models import Department, DepartmentHead


@admin.register(DepartmentHead)
class DepartmentHeadAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'middle_name', 'phone', 'email')
    search_fields = ('last_name', 'first_name', 'middle_name', 'phone', 'email')


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'head')
    search_fields = ('name', 'head__last_name', 'head__first_name', 'head__middle_name', 'description')
    prepopulated_fields = {'slug': ('name',)}
