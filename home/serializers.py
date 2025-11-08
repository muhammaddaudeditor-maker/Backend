# home/serializers.py

from rest_framework import serializers
from .models import (
    HomeHero, HomeStat, HomeIntro, HomeSkill,
    HomeService, HomeProcess, HomeTool, HomeFAQ, HomeCTA
)


# ---------------- Home Hero ----------------
class HomeHeroSerializer(serializers.ModelSerializer):
    video_url = serializers.SerializerMethodField()
    typewriter_phrases = serializers.SerializerMethodField()

    class Meta:
        model = HomeHero
        fields = [
            'id', 'title', 'typewriter_phrases', 'subtitle',
            'video', 'video_url', 'primary_button_text',
            'secondary_button_text', 'is_active',
            'created_at', 'updated_at'
        ]

    def get_video_url(self, obj):
        """Return Cloudinary video URL if available"""
        try:
            if obj.video:
                return obj.video.url  # ✅ Cloudinary full URL
        except:
            return None
        return None

    def get_typewriter_phrases(self, obj):
        """Split comma-separated phrases"""
        return obj.typewriter_phrases.split(',') if obj.typewriter_phrases else []


# ---------------- Home Stats ----------------
# home/serializers.py
class HomeStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeStat
        fields = ['id', 'name', 'value', 'suffix', 'icon', 'order', 'is_active']

    def validate_value(self, value):
        """Validate that the value is a number optionally followed by a suffix like M or K."""
        import re
        if not re.match(r'^\d+[MK]?$', value):
            raise serializers.ValidationError("Value must be a number optionally followed by 'M' or 'K' (e.g., '4M', '500', '10K').")
        return value


# ---------------- Home Intro ----------------
class HomeIntroSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    achievements = serializers.SerializerMethodField()

    class Meta:
        model = HomeIntro
        fields = [
            'id', 'title', 'subtitle', 'image', 'image_url',
            'achievements', 'primary_button_text',
            'secondary_button_text', 'is_active',
            'created_at', 'updated_at'
        ]

    def get_image_url(self, obj):
        """Return Cloudinary image URL if available"""
        try:
            if obj.image:
                return obj.image.url  # ✅ Cloudinary URL
        except:
            return None
        return None

    def get_achievements(self, obj):
        """Split comma-separated achievements"""
        return obj.achievements.split(',') if obj.achievements else []


# ---------------- Home Skill ----------------
class HomeSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeSkill
        fields = ['id', 'title', 'description', 'icon', 'order', 'is_active']


# ---------------- Home Service ----------------
class HomeServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeService
        fields = ['id', 'title', 'description', 'icon', 'order', 'is_active']


# ---------------- Home Process ----------------
class HomeProcessSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeProcess
        fields = ['id', 'title', 'description', 'icon', 'order', 'is_active']


# ---------------- Home Tool ----------------
class HomeToolSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeTool
        fields = ['id', 'title', 'description', 'icon', 'order', 'is_active']


# ---------------- Home FAQ ----------------
class HomeFAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeFAQ
        fields = ['id', 'question', 'answer', 'order', 'is_active']


# ---------------- Home CTA ----------------
class HomeCTASerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeCTA
        fields = ['id', 'title', 'description', 'button_text', 'is_active', 'created_at', 'updated_at']
