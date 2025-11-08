# services/admin.py

from django.contrib import admin
from django.utils.html import format_html
from .models import (
    Service, ServiceFeature, ProcessStep, 
    EquipmentCategory, EquipmentItem, Testimonial, SiteStats
)


class ServiceFeatureInline(admin.TabularInline):
    model = ServiceFeature
    extra = 4
    fields = ['feature_text', 'order']


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'icon', 'is_active', 'order', 'video_preview', 'updated_at']
    list_filter = ['is_active', 'icon', 'created_at']
    search_fields = ['title', 'description']
    list_editable = ['is_active', 'order']
    inlines = [ServiceFeatureInline]
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'icon', 'video', 'description')
        }),
        ('Display Settings', {
            'fields': ('is_active', 'order')
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


@admin.register(ServiceFeature)
class ServiceFeatureAdmin(admin.ModelAdmin):
    list_display = ['service', 'feature_text', 'order']
    list_filter = ['service']
    search_fields = ['feature_text', 'service__title']
    list_editable = ['order']


@admin.register(ProcessStep)
class ProcessStepAdmin(admin.ModelAdmin):
    list_display = ['step_number', 'title', 'is_active', 'order']
    list_filter = ['is_active']
    search_fields = ['title', 'description']
    list_editable = ['is_active', 'order']
    
    fieldsets = (
        ('Step Information', {
            'fields': ('step_number', 'title', 'description')
        }),
        ('Display Settings', {
            'fields': ('is_active', 'order')
        }),
    )


class EquipmentItemInline(admin.TabularInline):
    model = EquipmentItem
    extra = 4
    fields = ['item_name', 'order']


@admin.register(EquipmentCategory)
class EquipmentCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'order', 'item_count']
    list_editable = ['order']
    inlines = [EquipmentItemInline]
    
    def item_count(self, obj):
        return obj.items.count()
    item_count.short_description = 'Number of Items'


@admin.register(EquipmentItem)
class EquipmentItemAdmin(admin.ModelAdmin):
    list_display = ['item_name', 'category', 'order']
    list_filter = ['category']
    search_fields = ['item_name', 'category__name']
    list_editable = ['order']


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['name', 'role', 'rating', 'is_active', 'order', 'created_at']
    list_filter = ['is_active', 'rating', 'created_at']
    search_fields = ['name', 'role', 'text']
    list_editable = ['is_active', 'order']
    
    fieldsets = (
        ('Client Information', {
            'fields': ('name', 'role')
        }),
        ('Testimonial Content', {
            'fields': ('text', 'rating')
        }),
        ('Display Settings', {
            'fields': ('is_active', 'order')
        }),
    )


@admin.register(SiteStats)
class SiteStatsAdmin(admin.ModelAdmin):
    list_display = [
        'projects_completed', 
        'happy_clients', 
        'industry_awards', 
        'client_satisfaction',
        'updated_at'
    ]
    
    fieldsets = (
        ('Statistics', {
            'fields': (
                'projects_completed',
                'happy_clients',
                'industry_awards',
                'client_satisfaction'
            )
        }),
    )
    
    def has_add_permission(self, request):
        # Allow adding only if no instance exists
        return not SiteStats.objects.exists()
    
    def has_delete_permission(self, request, obj=None):
        # Prevent deletion
        return False