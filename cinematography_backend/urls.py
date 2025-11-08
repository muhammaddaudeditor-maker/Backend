import importlib

try:
    admin = importlib.import_module('django.contrib.admin')
except ImportError as e:
    raise ImportError("Django is not installed; install Django to run this project") from e

_urls = importlib.import_module('django.urls')
path = _urls.path
include = _urls.include

_conf = importlib.import_module('django.conf')
settings = _conf.settings

static = importlib.import_module('django.conf.urls.static').static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/portfolio/', include('portfolio.urls')),
    path('api/', include('services.urls')),
    path('api/about/', include('about.urls')),
    path('api/contact/', include('contact.urls')),
    path('api/', include('project.urls')),
    path('api/home/', include('home.urls')),
    path('', include('logo.urls')),
    path('api/', include('cv_upload.urls')),
    # If you want non-API versions:
    path('portfolio/', include('portfolio.urls')),
    path('about/', include('about.urls')),
    path('contact/', include('contact.urls')),
    path('home/', include('home.urls')),
    path('project/', include('project.urls')),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    

# Customize admin site
admin.site.site_header = "Cinematography Admin"
admin.site.site_title = "Cinematography Admin Portal"
admin.site.index_title = "Welcome to Cinematography Administration"