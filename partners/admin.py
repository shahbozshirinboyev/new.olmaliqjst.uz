from django.contrib import admin

from .models import Partner, PartnerCategory


@admin.register(PartnerCategory)
class PartnerCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'website', 'is_active')
    list_filter = ('category', 'is_active')
    search_fields = ('name', 'description', 'website')