# services/views.py

from rest_framework import viewsets, filters
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import (
    Service, ProcessStep, EquipmentCategory,
    Testimonial, SiteStats
)
from .serializers import (
    ServiceSerializer, ProcessStepSerializer,
    EquipmentCategorySerializer, TestimonialSerializer,
    SiteStatsSerializer
)

from rest_framework.views import APIView
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

class ServiceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Service.objects.filter(is_active=True).prefetch_related('features')
    serializer_class = ServiceSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['order', 'created_at', 'title']
    search_fields = ['title', 'description']
    ordering = ['order']


class ProcessStepViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ProcessStep.objects.filter(is_active=True)
    serializer_class = ProcessStepSerializer
    ordering = ['order']


class EquipmentCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = EquipmentCategory.objects.all().prefetch_related('items')
    serializer_class = EquipmentCategorySerializer
    ordering = ['order']


class TestimonialViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Testimonial.objects.filter(is_active=True)
    serializer_class = TestimonialSerializer
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    filterset_fields = ['rating']
    ordering = ['order', '-created_at']


@api_view(['GET'])
def site_stats_view(request):
    """Get the latest site statistics"""
    try:
        stats = SiteStats.objects.first()
        if stats:
            serializer = SiteStatsSerializer(stats, context={'request': request})
            return Response(serializer.data)
        return Response({
            'projects_completed': 500,
            'happy_clients': 300,
            'industry_awards': 15,
            'client_satisfaction': 98
        })
    except Exception as e:
        return Response({'error': str(e)}, status=500)