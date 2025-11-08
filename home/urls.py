# home/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HomeHeroViewSet, HomeStatViewSet, HomeIntroViewSet, HomeSkillViewSet, HomeServiceViewSet, HomeProcessViewSet, HomeToolViewSet, HomeFAQViewSet, HomeCTAViewSet
from .views import UploadMediaView

router = DefaultRouter()
router.register(r'hero', HomeHeroViewSet, basename='home_hero')
router.register(r'stats', HomeStatViewSet, basename='home_stat')
router.register(r'intro', HomeIntroViewSet, basename='home_intro')
router.register(r'skills', HomeSkillViewSet, basename='home_skill')
router.register(r'services', HomeServiceViewSet, basename='home_service')
router.register(r'processes', HomeProcessViewSet, basename='home_process')
router.register(r'tools', HomeToolViewSet, basename='home_tool')
router.register(r'faqs', HomeFAQViewSet, basename='home_faq')
router.register(r'cta', HomeCTAViewSet, basename='home_cta')

urlpatterns = [
    path('', include(router.urls)),
    path('upload/', UploadMediaView.as_view(), name='upload-media'),
]