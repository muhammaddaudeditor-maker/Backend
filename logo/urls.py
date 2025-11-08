from django.urls import path
from .views import SiteConfigurationView

urlpatterns = [
    path('api/site-config/', SiteConfigurationView.as_view(), name='site-config'),
]