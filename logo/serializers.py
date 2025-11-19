from rest_framework import serializers
from .models import SiteConfiguration

class SiteConfigurationSerializer(serializers.ModelSerializer):
    logo_url = serializers.SerializerMethodField()
    
    class Meta:
        model = SiteConfiguration
        fields = ['site_name', 'logo_url']
    
    def get_logo_url(self, obj):
        """Return full URL for ImageField"""
        if obj.logo:
            request = self.context.get('request')
            return request.build_absolute_uri(obj.logo.url) if request else obj.logo.url
        return None
