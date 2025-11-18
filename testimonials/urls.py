# testimonials/urls.py
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import TestimonialViewSet

router = SimpleRouter()
router.register(r'testimonials', TestimonialViewSet, basename='testimonial')

urlpatterns = [
    path('', include(router.urls)),
]