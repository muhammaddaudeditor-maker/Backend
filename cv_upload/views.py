from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import CVUpload
from .serializers import CVUploadSerializer

class CVUploadViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CVUpload.objects.all()
    serializer_class = CVUploadSerializer
    
    @action(detail=False, methods=['get'])
    def active(self, request):
        """Get the currently active CV"""
        try:
            active_cv = CVUpload.objects.get(is_active=True)
            serializer = self.get_serializer(active_cv)
            return Response(serializer.data)
        except CVUpload.DoesNotExist:
            return Response(
                {'error': 'No active CV found'},
                status=status.HTTP_404_NOT_FOUND
            )