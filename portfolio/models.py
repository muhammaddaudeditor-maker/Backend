from django.db import models
from django.core.validators import FileExtensionValidator
from cloudinary.models import CloudinaryField

# ---------------- Media Uploads ----------------
class MediaFile(models.Model):
    title = models.CharField(max_length=255)
    file = CloudinaryField('file', blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


# ---------------- Portfolio Category ----------------
class PortfolioCategory(models.Model):
    name = models.CharField(max_length=100, help_text='e.g., Wedding, Real Estate')
    icon = models.CharField(max_length=50, choices=[
        ('Sparkles', 'Sparkles'),   # For All Projects
        ('Heart', 'Heart'),         # For Weddings
        ('Building2', 'Building2'), # For Real Estate
        ('MessageCircle', 'MessageCircle'), # For Talking Head
        ('Film', 'Film'),           # For Commercial
    ], default='Sparkles')
    count = models.IntegerField(default=0, help_text='Number of projects in this category')
    order = models.IntegerField(default=0, help_text='Display order (lower numbers appear first)')
    is_active = models.BooleanField(default=True, help_text='Display this category on the website')

    class Meta:
        ordering = ['order', 'name']
        verbose_name = 'Portfolio Category'
        verbose_name_plural = 'Portfolio Categories'

    def __str__(self):
        return self.name


# ---------------- Projects ----------------
class Project(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(PortfolioCategory, on_delete=models.CASCADE, related_name='projects')
    thumbnail = CloudinaryField('image', blank=True, null=True)
    video = CloudinaryField(
        'video', 
        blank=True, 
        null=True,
        resource_type='video',
        type='upload'
    ) 
    description = models.TextField(help_text='Project description')
    views = models.CharField(max_length=10, default='0', help_text='e.g., 12.5K')
    likes = models.CharField(max_length=10, default='0', help_text='e.g., 2.1K')
    order = models.IntegerField(default=0, help_text='Display order (lower numbers appear first)')
    is_active = models.BooleanField(default=True, help_text='Display this project on the website')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', 'title']
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    def __str__(self):
        return self.title