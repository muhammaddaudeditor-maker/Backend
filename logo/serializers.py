from rest_framework import serializers
from .models import SiteConfiguration

class SiteConfigurationSerializer(serializers.ModelSerializer):
    logo_url = serializers.SerializerMethodField()
    
    class Meta:
        model = SiteConfiguration
        fields = ['site_name', 'logo_url']
    
    def get_logo_url(self, obj):
        """Return the Cloudinary URL for the logo"""
        if obj.logo:
            return obj.logo.url
        return None