# portfolio/views.py

from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser

from .models import PortfolioCategory, Project, MediaFile
from .serializers import PortfolioCategorySerializer, ProjectSerializer


# ---------------- Media Upload ----------------
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
            "file_url": getattr(media.file, 'url', None),
        })


# ---------------- Portfolio Categories ----------------
class PortfolioCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = PortfolioCategory.objects.filter(is_active=True).prefetch_related('projects')
    serializer_class = PortfolioCategorySerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['order', 'name']
    search_fields = ['name']
    ordering = ['order']



# ---------------- Projects ----------------
class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Project.objects.filter(is_active=True).select_related('category')
    serializer_class = ProjectSerializer
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    filterset_fields = ['category']
    ordering_fields = ['order', 'title']
    ordering = ['order']
