# about/views.py (Updated)

from rest_framework import viewsets, filters
from .models import Stat, CoreValue, TimelineEvent, Skill, AboutCTA, AboutTabContent
from .serializers import StatSerializer, CoreValueSerializer, TimelineEventSerializer, SkillSerializer, AboutCTASerializer, AboutTabContentSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from .models import MediaFile

class UploadMediaView(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request):
        file = request.data.get('file')
        title = request.data.get('title', 'Untitled')

        if not file:
            return Response({"error": "No file provided."}, status=400)

        media = MediaFile.objects.create(title=title, file=file)
        return Response({
            "id": media.id,
            "title": media.title,
            "file_url": media.file.url,
        })

class StatViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Stat.objects.filter(is_active=True)
    serializer_class = StatSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['order', 'name']
    ordering = ['order']

class CoreValueViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CoreValue.objects.filter(is_active=True)
    serializer_class = CoreValueSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['order', 'title']
    ordering = ['order']

class TimelineEventViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TimelineEvent.objects.filter(is_active=True)
    serializer_class = TimelineEventSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['order', 'year']
    ordering = ['order']

class SkillViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Skill.objects.filter(is_active=True)
    serializer_class = SkillSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['order', 'name']
    ordering = ['order']

class AboutCTAViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AboutCTA.objects.filter(is_active=True)
    serializer_class = AboutCTASerializer
    ordering = ['created_at']

class AboutTabContentViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AboutTabContent.objects.filter(is_active=True)
    serializer_class = AboutTabContentSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['tab_name']
    ordering = ['tab_name']