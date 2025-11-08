# cinematography_backend/project/views.py

from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import PortfolioHero, Project
from .serializers import (
    PortfolioHeroSerializer,
    ProjectListSerializer,
    ProjectDetailSerializer
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


class PortfolioHeroViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet for portfolio hero section
    GET /api/portfolio-hero/ - Get active hero section
    """
    queryset = PortfolioHero.objects.filter(is_active=True)
    serializer_class = PortfolioHeroSerializer
    
    @action(detail=False, methods=['get'])
    def active(self, request):
        """Get the active hero section"""
        hero = self.queryset.first()
        if hero:
            serializer = self.get_serializer(hero)
            return Response(serializer.data)
        return Response({'detail': 'No active hero section found'}, status=404)


class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet for projects
    GET /api/projects/ - List all published projects
    GET /api/projects/{id}/ - Get project details
    GET /api/projects/featured/ - Get featured projects
    """
    queryset = Project.objects.filter(is_published=True)
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['is_featured', 'media_type']
    search_fields = ['title', 'description', 'details', 'client']
    ordering_fields = ['created_at', 'order', 'title']
    
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ProjectDetailSerializer
        return ProjectListSerializer
    
    @action(detail=False, methods=['get'])
    def featured(self, request):
        """Get featured projects"""
        featured_projects = self.queryset.filter(is_featured=True)
        serializer = self.get_serializer(featured_projects, many=True)
        return Response(serializer.data)