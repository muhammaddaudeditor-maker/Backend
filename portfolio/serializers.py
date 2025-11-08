# portfolio/serializers.py

from rest_framework import serializers
from .models import PortfolioCategory, Project


# ---------------- Project ----------------
class ProjectSerializer(serializers.ModelSerializer):
    video_url = serializers.SerializerMethodField()
    thumbnail_url = serializers.SerializerMethodField()
    category_info = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = [
            'id', 'title', 'category', 'category_info', 'thumbnail', 'thumbnail_url',
            'video', 'video_url', 'description', 'views', 'likes', 'order',
            'is_active', 'created_at', 'updated_at'
        ]

    def get_video_url(self, obj):
        try:
            return obj.video.url if obj.video else None
        except:
            return None

    def get_thumbnail_url(self, obj):
        try:
            return obj.thumbnail.url if obj.thumbnail else None
        except:
            return None

    def get_category_info(self, obj):
        if obj.category:
            return {
                "id": obj.category.id,
                "name": obj.category.name,
                "icon": obj.category.icon
            }
        return None

# ---------------- Portfolio Category ----------------
class PortfolioCategorySerializer(serializers.ModelSerializer):
    projects = serializers.SerializerMethodField()

    class Meta:
        model = PortfolioCategory
        fields = [
            'id', 'name', 'icon', 'count', 'projects', 'order', 'is_active'
        ]

    def get_projects(self, obj):
        # Only return active projects, ordered by 'order' and 'title'
        projects = obj.projects.filter(is_active=True).order_by('order', 'title')
        return ProjectSerializer(projects, many=True).data
