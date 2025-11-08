from rest_framework import serializers
from .models import (
    Service, ServiceFeature, ProcessStep,
    EquipmentCategory, EquipmentItem, Testimonial, SiteStats
)


# ------------------- Service Feature -------------------
class ServiceFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceFeature
        fields = ['id', 'feature_text', 'order']


# ------------------- Service -------------------
class ServiceSerializer(serializers.ModelSerializer):
    features = ServiceFeatureSerializer(many=True, read_only=True)
    video_url = serializers.SerializerMethodField()
    
    class Meta:
        model = Service
        fields = [
            'id', 'title', 'icon', 'video', 'video_url',
            'description', 'features', 'is_active', 
            'order', 'created_at', 'updated_at',
        ]
    
    def get_video_url(self, obj):
        """Return Cloudinary video URL directly."""
        try:
            if obj.video:
                return obj.video.url  # Cloudinary provides full URL
        except Exception:
            return None
        return None


# ------------------- Process Step -------------------
class ProcessStepSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProcessStep
        fields = ['id', 'step_number', 'title', 'description', 'order', 'is_active']


# ------------------- Equipment Item -------------------
class EquipmentItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = EquipmentItem
        fields = ['id', 'item_name', 'order']


# ------------------- Equipment Category -------------------
class EquipmentCategorySerializer(serializers.ModelSerializer):
    items = EquipmentItemSerializer(many=True, read_only=True)
    
    class Meta:
        model = EquipmentCategory
        fields = ['id', 'name', 'items', 'order']


# ------------------- Testimonial -------------------
class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = [
            'id', 'name', 'role', 'text', 'rating',
            'is_active', 'order', 'created_at',
        ]


# ------------------- Site Stats -------------------
class SiteStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteStats
        fields = [
            'id', 'projects_completed', 'happy_clients',
            'industry_awards', 'client_satisfaction', 'updated_at',
        ]
