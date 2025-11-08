# app: cv_upload/admin.py
from django.contrib import admin
from django.utils.html import format_html
from .models import CVUpload

@admin.register(CVUpload)
class CVUploadAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active', 'uploaded_at', 'updated_at', 'cv_preview']
    list_filter = ['is_active', 'uploaded_at']
    search_fields = ['title']
    readonly_fields = ['uploaded_at', 'updated_at', 'cv_preview']

    fieldsets = (
        ('CV Information', {
            'fields': ('title', 'cv_file', 'is_active')
        }),
        ('Timestamps', {
            'fields': ('uploaded_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def cv_preview(self, obj):
        if obj.cv_file:
            # Show view button and download button
            view_link = format_html(
                '<a href="{}" target="_blank" style="margin-right:8px;">View CV</a>',
                obj.cv_url
            )
            download_link = format_html(
                '<a href="{}" target="_blank" style="background:#007bff;color:white;padding:4px 8px;border-radius:4px;text-decoration:none;">Download</a>',
                obj.download_url
            )
            return format_html('{}&nbsp;{}', view_link, download_link)
        return "No CV uploaded"

    cv_preview.short_description = "CV File"

    def save_model(self, request, obj, form, change):
        if obj.is_active:
            CVUpload.objects.exclude(pk=obj.pk).update(is_active=False)
        super().save_model(request, obj, form, change)
