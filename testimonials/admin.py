# testimonials/admin.py
from django.contrib import admin
from .models import Testimonial

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['name', 'role', 'company', 'rating', 'order', 'is_active', 'created_at']
    list_filter = ['is_active', 'rating', 'created_at']
    search_fields = ['name', 'company', 'role', 'text']
    list_editable = ['order', 'is_active']
    readonly_fields = ['avatar_initials', 'created_at', 'updated_at']

    fieldsets = (
        ('Client Info', {
            'fields': ('name', 'role', 'company', 'avatar_image', 'avatar_initials')
        }),
        ('Testimonial', {
            'fields': ('text', 'rating', 'gradient_color')
        }),
        ('Settings', {
            'fields': ('order', 'is_active')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )