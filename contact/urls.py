# contact/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ContactInfoViewSet,
    WhyChooseUsViewSet,
    HeroSectionViewSet,
    ContactMessageViewSet,
    contact_info_list,
    why_choose_us_list,
    hero_section_detail,
    submit_contact_message
)
from .views import UploadMediaView

router = DefaultRouter()
router.register(r'contact-info', ContactInfoViewSet, basename='contactinfo')
router.register(r'why-choose-us', WhyChooseUsViewSet, basename='whychooseus')
router.register(r'hero-sections', HeroSectionViewSet, basename='herosection')
router.register(r'messages', ContactMessageViewSet, basename='contactmessage')

urlpatterns = [
    # Router URLs
    path('', include(router.urls)),
    
    # Alternative simpler endpoints
    path('info/', contact_info_list, name='contact-info-list'),
    path('reasons/', why_choose_us_list, name='why-choose-us-list'),
    path('hero/<str:page>/', hero_section_detail, name='hero-section-detail'),
    path('submit/', submit_contact_message, name='submit-contact-message'),
    path('upload/', UploadMediaView.as_view(), name='upload-media'),
]