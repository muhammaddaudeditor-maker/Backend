# portfolio/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PortfolioCategoryViewSet, ProjectViewSet
from .views import UploadMediaView

router = DefaultRouter()
router.register(r'categories', PortfolioCategoryViewSet, basename='portfolio_category')
router.register(r'projects', ProjectViewSet, basename='project')

urlpatterns = [
    path('', include(router.urls)),
    path('upload/', UploadMediaView.as_view(), name='upload-media'),
]