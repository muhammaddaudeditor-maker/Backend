# testimonials/apps.py
from django.apps import AppConfig

class TestimonialsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'testimonials'           # ← must match folder name
    