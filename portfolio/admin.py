# portfolio/admin.py

from django.contrib import admin
from django.utils.html import format_html
from .models import PortfolioCategory, Project


@admin.register(PortfolioCategory)
class PortfolioCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'icon', 'count', 'order', 'is_active']
    list_filter = ['is_active', 'icon']
    search_fields = ['name']
    list_editable = ['order', 'is_active']

    fieldsets = (
        ('Category Information', {
            'fields': ('name', 'icon', 'count')
        }),
        ('Display Settings', {
            'fields': ('order', 'is_active')
        }),
    )

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'views', 'likes', 'order', 'is_active', 'video_preview', 'updated_at']
    list_filter = ['is_active', 'category']
    search_fields = ['title', 'description', 'category__name']
    list_editable = ['order', 'is_active']

    fieldsets = (
        ('Project Information', {
            'fields': ('title', 'category', 'thumbnail', 'video', 'description', 'views', 'likes')
        }),
        ('Display Settings', {
            'fields': ('order', 'is_active')
        }),
    )

    def video_preview(self, obj):
        if obj.video:
            return format_html(
                '<video width="100" height="60" controls>'
                '<source src="{}" type="video/mp4"></video>',
                obj.video.url
            )
        return "No video"
    video_preview.short_description = 'Video Preview'