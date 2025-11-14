# app: cv_upload/urls.py
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import CVUploadViewSet

router = SimpleRouter()
router.register(r'cv', CVUploadViewSet, basename='cv')

urlpatterns = [
    path('', include(router.urls)),
]
