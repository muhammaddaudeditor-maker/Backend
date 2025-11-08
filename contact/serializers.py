# contact/serializers.py

from rest_framework import serializers
from .models import ContactInfo, WhyChooseUs, HeroSection, ContactMessage


class ContactInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInfo
        fields = ['id', 'icon', 'title', 'info', 'link', 'order']


class WhyChooseUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhyChooseUs
        fields = ['id', 'icon', 'title', 'description', 'order']


class HeroSectionSerializer(serializers.ModelSerializer):
    media_url = serializers.SerializerMethodField()

    class Meta:
        model = HeroSection
        fields = [
            'id', 'page', 'title', 'subtitle', 'description',
            'badge_text', 'badge_icon', 'media_type',
            'media_url', 'is_active', 'updated_at'
        ]

    def get_media_url(self, obj):
        """
        Return Cloudinary URL for either image or video
        depending on the media_type.
        """
        try:
            if obj.media_type == 'video' and obj.video:
                return obj.video.url  # ✅ Cloudinary URL
            elif obj.media_type == 'image' and obj.image:
                return obj.image.url  # ✅ Cloudinary URL
        except:
            return None
        return None


class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = ['id', 'name', 'email', 'whatsapp', 'subject', 'message', 'created_at']
        read_only_fields = ['id', 'created_at']

    def validate_email(self, value):
        """Validate email format"""
        if not value or '@' not in value:
            raise serializers.ValidationError("Please provide a valid email address.")
        return value

    def validate_name(self, value):
        """Validate name is not empty"""
        if not value or len(value.strip()) < 2:
            raise serializers.ValidationError("Name must be at least 2 characters long.")
        return value.strip()

    def validate_whatsapp(self, value):
        """Validate WhatsApp number"""
        if not value or len(value.strip()) < 10:
            raise serializers.ValidationError("Please provide a valid WhatsApp number.")
        return value.strip()
