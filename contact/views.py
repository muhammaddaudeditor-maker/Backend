# contact/views.py

from rest_framework import viewsets, status
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from .models import ContactInfo, WhyChooseUs, HeroSection, ContactMessage
from .serializers import (
    ContactInfoSerializer, 
    WhyChooseUsSerializer, 
    HeroSectionSerializer,
    ContactMessageSerializer
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

class ContactInfoViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet for contact information (phone, email, address, etc.)
    """
    queryset = ContactInfo.objects.filter(is_active=True)
    serializer_class = ContactInfoSerializer
    ordering = ['order']


class WhyChooseUsViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet for "Why Choose Us" reasons
    """
    queryset = WhyChooseUs.objects.filter(is_active=True)
    serializer_class = WhyChooseUsSerializer
    ordering = ['order']


class HeroSectionViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet for hero sections
    """
    queryset = HeroSection.objects.filter(is_active=True)
    serializer_class = HeroSectionSerializer
    lookup_field = 'page'
    
    @action(detail=False, methods=['get'], url_path='page/(?P<page_name>[^/.]+)')
    def by_page(self, request, page_name=None):
        """
        Get hero section by page name
        Usage: /api/contact/hero-sections/page/contact/
        """
        try:
            hero = HeroSection.objects.get(page=page_name, is_active=True)
            serializer = self.get_serializer(hero)
            return Response(serializer.data)
        except HeroSection.DoesNotExist:
            return Response(
                {'error': f'Hero section for page "{page_name}" not found'},
                status=status.HTTP_404_NOT_FOUND
            )


class ContactMessageViewSet(viewsets.ModelViewSet):
    """
    ViewSet for contact messages
    Only POST is allowed for public users
    """
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer
    http_method_names = ['post']  # Only allow POST requests
    
    def create(self, request, *args, **kwargs):
        """
        Create a new contact message
        """
        serializer = self.get_serializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({
                'success': True,
                'message': 'Your message has been sent successfully! We will get back to you soon.',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        
        return Response({
            'success': False,
            'message': 'Please check your form and try again.',
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)


# Alternative function-based views for simpler endpoints

@api_view(['GET'])
def contact_info_list(request):
    """
    Get all active contact information
    """
    contact_info = ContactInfo.objects.filter(is_active=True).order_by('order')
    serializer = ContactInfoSerializer(contact_info, many=True, context={'request': request})
    return Response(serializer.data)


@api_view(['GET'])
def why_choose_us_list(request):
    """
    Get all active "Why Choose Us" reasons
    """
    reasons = WhyChooseUs.objects.filter(is_active=True).order_by('order')
    serializer = WhyChooseUsSerializer(reasons, many=True, context={'request': request})
    return Response(serializer.data)


@api_view(['GET'])
def hero_section_detail(request, page):
    """
    Get hero section for a specific page
    Usage: /api/contact/hero/contact/
    """
    try:
        hero = HeroSection.objects.get(page=page, is_active=True)
        serializer = HeroSectionSerializer(hero, context={'request': request})
        return Response(serializer.data)
    except HeroSection.DoesNotExist:
        return Response(
            {'error': f'Hero section for page "{page}" not found'},
            status=status.HTTP_404_NOT_FOUND
        )


@api_view(['POST'])
def submit_contact_message(request):
    """
    Submit a contact message
    """
    serializer = ContactMessageSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        return Response({
            'success': True,
            'message': 'Your message has been sent successfully! We will get back to you within 24 hours.',
            'data': serializer.data
        }, status=status.HTTP_201_CREATED)
    
    return Response({
        'success': False,
        'message': 'Please check your form and try again.',
        'errors': serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST)