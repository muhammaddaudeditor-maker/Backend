# serializers.py
from rest_framework import serializers
from .models import CVUpload

class CVUploadSerializer(serializers.ModelSerializer):
    cv_url = serializers.SerializerMethodField()

    class Meta:
        model = CVUpload
        fields = ['id', 'title', 'cv_url', 'uploaded_at', 'updated_at', 'is_active']

    def get_cv_url(self, obj):
        request = self.context.get('request')
        if obj.cv_file:
            return request.build_absolute_uri(obj.cv_file.url)
        return None
