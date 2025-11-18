# testimonials/serializers.py
from rest_framework import serializers
from .models import (
     Testimonial
)


class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = [
            'id', 'name', 'role', 'text', 'rating',
            'is_active', 'order', 'created_at',
        ]

