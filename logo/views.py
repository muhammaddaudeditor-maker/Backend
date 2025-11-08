from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import SiteConfiguration
from .serializers import SiteConfigurationSerializer

class SiteConfigurationView(APIView):
    """
    API endpoint to get site configuration including logo
    """
    def get(self, request):
        config = SiteConfiguration.get_config()
        serializer = SiteConfigurationSerializer(config)
        return Response(serializer.data, status=status.HTTP_200_OK)