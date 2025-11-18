# testimonials/serializers.py
from rest_framework import serializers
from .models import Testimonial

class TestimonialSerializer(serializers.ModelSerializer):
    avatar = serializers.SerializerMethodField()
    avatar_url = serializers.SerializerMethodField()
    color = serializers.CharField(source='gradient_color', default='from-purple-500 to-pink-500')

    class Meta:
        model = Testimonial
        fields = [
            'id', 'name', 'role', 'company',
            'text', 'rating',
            'avatar', 'avatar_url',
            'gradient_color', 'color', 'order', 'is_active'
        ]

    def get_avatar(self, obj):
        return obj.avatar_initials

    def get_avatar_url(self, obj):
        if obj.avatar_image:
            return obj.avatar_image.url
        return None