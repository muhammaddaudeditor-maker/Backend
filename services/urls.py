# services/urls.py

from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import (
    ServiceViewSet, ProcessStepViewSet,
    EquipmentCategoryViewSet,
    site_stats_view
)

from .views import UploadMediaView

urlpatterns = [
    path('upload/', UploadMediaView.as_view(), name='upload-media'),
]

router = SimpleRouter()
router.register(r'services', ServiceViewSet, basename='service')
router.register(r'process-steps', ProcessStepViewSet, basename='processstep')
router.register(r'equipment', EquipmentCategoryViewSet, basename='equipment')

urlpatterns = [
    path('', include(router.urls)),
    path('stats/', site_stats_view, name='site-stats'),
]