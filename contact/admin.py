# contact/admin.py

from django.contrib import admin
from django.utils.html import format_html
from .models import ContactInfo, WhyChooseUs, HeroSection, ContactMessage


@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ['title', 'icon', 'info', 'is_active', 'order', 'updated_at']
    list_filter = ['is_active', 'icon']
    search_fields = ['title', 'info']
    list_editable = ['is_active', 'order']
    
    fieldsets = (
        ('Contact Information', {
            'fields': ('icon', 'title', 'info', 'link')
        }),
        ('Display Settings', {
            'fields': ('is_active', 'order')
        }),
    )


@admin.register(WhyChooseUs)
class WhyChooseUsAdmin(admin.ModelAdmin):
    list_display = ['title', 'icon', 'is_active', 'order', 'updated_at']
    list_filter = ['is_active', 'icon']
    search_fields = ['title', 'description']
    list_editable = ['is_active', 'order']
    
    fieldsets = (
        ('Content', {
            'fields': ('icon', 'title', 'description')
        }),
        ('Display Settings', {
            'fields': ('is_active', 'order')
        }),
    )


@admin.register(HeroSection)
class HeroSectionAdmin(admin.ModelAdmin):
    list_display = ['page', 'title', 'media_type', 'media_preview', 'is_active', 'updated_at']
    list_filter = ['page', 'media_type', 'is_active']
    search_fields = ['title', 'subtitle', 'description']
    list_editable = ['is_active']
    
    fieldsets = (
        ('Page Selection', {
            'fields': ('page',),
            'description': 'Select which page this hero section is for'
        }),
        ('Content', {
            'fields': ('title', 'subtitle', 'description', 'badge_text', 'badge_icon')
        }),
        ('Media', {
            'fields': ('media_type', 'video', 'image'),
            'description': 'Upload either a video or image based on media_type selection'
        }),
        ('Settings', {
            'fields': ('is_active',)
        }),
    )
    
    def media_preview(self, obj):
        if obj.media_type == 'video' and obj.video:
            return format_html(
                '<video width="150" height="90" controls>'
                '<source src="{}" type="video/mp4"></video>',
                obj.video.url
            )
        elif obj.media_type == 'image' and obj.image:
            return format_html(
                '<img src="{}" width="150" height="90" style="object-fit: cover;" />',
                obj.image.url
            )
        return "No media"
    media_preview.short_description = 'Media Preview'


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'status_badge', 'created_at']
    list_filter = ['is_read', 'replied', 'created_at']
    search_fields = ['name', 'email', 'whatsapp', 'subject', 'message']
    readonly_fields = ['name', 'email', 'whatsapp', 'subject', 'message', 'created_at']
    list_per_page = 25
    
    fieldsets = (
        ('Message Details', {
            'fields': ('name', 'email', 'whatsapp', 'subject', 'message', 'created_at')
        }),
        ('Status', {
            'fields': ('is_read', 'replied', 'admin_notes')
        }),
    )
    
    def status_badge(self, obj):
        if obj.replied:
            color = 'green'
            status = 'Replied'
        elif obj.is_read:
            color = 'orange'
            status = 'Read'
        else:
            color = 'red'
            status = 'Unread'
        
        return format_html(
            '<span style="background-color: {}; color: white; padding: 5px 10px; '
            'border-radius: 5px; font-weight: bold;">{}</span>',
            color, status
        )
    status_badge.short_description = 'Status'
    
    actions = ['mark_as_read', 'mark_as_replied']
    
    def mark_as_read(self, request, queryset):
        queryset.update(is_read=True)
        self.message_user(request, f"{queryset.count()} messages marked as read.")
    mark_as_read.short_description = "Mark selected as read"
    
    def mark_as_replied(self, request, queryset):
        queryset.update(is_read=True, replied=True)
        self.message_user(request, f"{queryset.count()} messages marked as replied.")
    mark_as_replied.short_description = "Mark selected as replied"