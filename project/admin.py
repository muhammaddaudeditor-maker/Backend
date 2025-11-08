# cinematography_backend/project/admin.py

from django.contrib import admin
from .models import PortfolioHero, Project

@admin.register(PortfolioHero)
class PortfolioHeroAdmin(admin.ModelAdmin):
    list_display = ['title', 'media_type', 'is_active', 'created_at']
    list_filter = ['is_active', 'media_type', 'created_at']
    search_fields = ['title', 'subtitle']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Content', {
            'fields': ('title', 'subtitle', 'button_text',)
        }),
        ('Media', {
            'fields': ('media_type', 'image', 'video')
        }),
        ('Settings', {
            'fields': ('is_active',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def save_model(self, request, obj, form, change):
        # Ensure only one hero section is active at a time
        if obj.is_active:
            PortfolioHero.objects.filter(is_active=True).update(is_active=False)
        super().save_model(request, obj, form, change)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'media_type', 'client', 'is_featured', 'is_published', 'order', 'created_at']
    list_filter = ['is_featured', 'is_published', 'media_type', 'created_at']
    search_fields = ['title', 'description', 'details', 'client']
    readonly_fields = ['created_at', 'updated_at']
    list_editable = ['order', 'is_featured', 'is_published']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'description', 'details')
        }),
        ('Media', {
            'fields': ('media_type', 'image', 'video', 'thumbnail')
        }),
        ('Additional Details', {
            'fields': ('client', 'project_url', 'technologies')
        }),
        ('Settings', {
            'fields': ('is_featured', 'is_published', 'order')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
