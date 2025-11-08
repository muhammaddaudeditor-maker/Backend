# app: cv_upload/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CVUploadViewSet

router = DefaultRouter()
router.register(r'cv', CVUploadViewSet, basename='cv')

urlpatterns = [
    path('', include(router.urls)),
]
