# testimonials/admin.py
from django.contrib import admin
from .models import (
   Testimonial
)



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
