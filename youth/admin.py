from django.contrib import admin

from .models import YouthActivity


@admin.register(YouthActivity)
class YouthActivityAdmin(admin.ModelAdmin):
    list_display = ('title', 'event_date', 'is_active')
    list_filter = ('is_active', 'event_date')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}