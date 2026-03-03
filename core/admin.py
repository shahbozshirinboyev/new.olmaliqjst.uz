from django.contrib import admin

from .models import About, Announcement, Document, Leadership, MaterialBase, Menu, TechStat, TopbarSettings


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'parent', 'order', 'is_active')
    list_filter = ('is_active', 'parent')
    search_fields = ('title', 'url')
    ordering = ('order',)


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'updated_at')
    search_fields = ('title', 'content')


@admin.register(Leadership)
class LeadershipAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'position', 'order')
    search_fields = ('full_name', 'position')
    ordering = ('order',)


@admin.register(MaterialBase)
class MaterialBaseAdmin(admin.ModelAdmin):
    list_display = ('title', 'updated_at')
    search_fields = ('title', 'description')


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_at', 'created_at')
    list_filter = ('published_at',)
    search_fields = ('title', 'description')


@admin.register(TopbarSettings)
class TopbarSettingsAdmin(admin.ModelAdmin):
    list_display = ('email', 'phone', 'telegram_url', 'instagram_url', 'youtube_url', 'is_active', 'updated_at')


@admin.register(TechStat)
class TechStatAdmin(admin.ModelAdmin):
    list_display = ('count', 'name', 'icon', 'order', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('count', 'name', 'icon')
    ordering = ('order', 'id')


@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_at', 'is_active')
    list_filter = ('is_active', 'published_at')
    search_fields = ('title', 'content')
    ordering = ('-published_at', '-created_at')
