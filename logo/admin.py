from django.contrib import admin
from .models import SiteConfiguration

@admin.register(SiteConfiguration)
class SiteConfigurationAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Logo & Branding', {
            'fields': ('logo', 'site_name'),
            'description': 'Upload your site logo or set the site name'
        }),
    )
    
    list_display = ('site_name', 'has_logo', 'updated_at')
    
    def has_logo(self, obj):
        return bool(obj.logo)
    has_logo.boolean = True
    has_logo.short_description = 'Logo Uploaded'
    
    def has_add_permission(self, request):
        # Only allow one instance
        if SiteConfiguration.objects.exists():
            return False
        return super().has_add_permission(request)
    
    def has_delete_permission(self, request, obj=None):
        # Prevent deletion of the config
        return False