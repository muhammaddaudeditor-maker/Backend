# testimonials/admin.py
from django.contrib import admin
from .models import Testimonial


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['name', 'role', 'company', 'rating', 'is_active', 'order', 'created_at']
    list_filter = ['is_active', 'rating', 'created_at']
    search_fields = ['name', 'role', 'company', 'text']
    list_editable = ['is_active', 'order']
    readonly_fields = ['created_at']  # ← ONLY this exists!

    fieldsets = (
        ('Client Info', {
            'fields': ('name', 'role', 'company')
        }),
        ('Testimonial', {
            'fields': ('text', 'rating')
        }),
        ('Appearance', {
            'fields': ('avatar', 'avatar_url', 'gradient_color')
        }),
        ('Settings', {
            'fields': ('is_active', 'order', 'created_at')
        }),
    )