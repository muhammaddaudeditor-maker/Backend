from rest_framework import serializers
from .models import Stat, CoreValue, TimelineEvent, Skill, AboutCTA, AboutTabContent

class StatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stat
        fields = ['id', 'name', 'value', 'suffix', 'icon', 'order', 'is_active']


class CoreValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoreValue
        fields = ['id', 'title', 'description', 'icon', 'order', 'is_active']


class TimelineEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimelineEvent
        fields = ['id', 'year', 'title', 'description', 'icon', 'order', 'is_active']


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['id', 'name', 'level', 'icon', 'order', 'is_active']


class AboutCTASerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutCTA
        fields = ['id', 'title', 'description', 'button_text', 'is_active', 'created_at', 'updated_at']


class AboutTabContentSerializer(serializers.ModelSerializer):
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
                return obj.image.url  # ✅ Proper Cloudinary URL
            except:
                return None
        return None
