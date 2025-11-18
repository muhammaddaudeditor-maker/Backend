# about/serializers.py

from rest_framework import serializers
from .models import Stat, CoreValue, TimelineEvent, Skill, AboutCTA, AboutTabContent

# ---------------- Stats ----------------
class StatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stat
        fields = ['id', 'name', 'value', 'suffix', 'icon', 'order', 'is_active']


# ---------------- Core Values ----------------
class CoreValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoreValue
        fields = ['id', 'title', 'description', 'icon', 'order', 'is_active']


# ---------------- Timeline Events ----------------
class TimelineEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimelineEvent
        fields = ['id', 'year', 'title', 'description', 'icon', 'order', 'is_active']


# ---------------- Skills ----------------
class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['id', 'name', 'level', 'icon', 'order', 'is_active']


# ---------------- About CTA ----------------
class AboutCTASerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutCTA
        fields = ['id', 'title', 'description', 'button_text', 'is_active', 'created_at', 'updated_at']


# ---------------- About Tabs ----------------
class AboutTabContentSerializer(serializers.ModelSerializer):
    # Use server file URL instead of Cloudinary
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = AboutTabContent
        fields = [
            'id',
            'tab_name',
            'title',
            'content',
            'image_url',
            'is_active',
            'created_at',
            'updated_at'
        ]

    def get_image_url(self, obj):
        if obj.image:
            try:
                # Returns the file URL relative to MEDIA_URL
                return obj.image.url
            except:
                return None
        return None
