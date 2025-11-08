from django.db import models
from cloudinary.models import CloudinaryField


# ---------------- Media Uploads ----------------
class MediaFile(models.Model):
    title = models.CharField(max_length=255)
    file = CloudinaryField('file', blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


# ---------------- Portfolio Hero Section ----------------
class PortfolioHero(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.TextField()
    button_text = models.CharField(max_length=100, default="Start Your Project")

    media_type = models.CharField(
        max_length=10,
        choices=[('image', 'Image'), ('video', 'Video')],
        default='image'
    )

    image = CloudinaryField('image', blank=True, null=True)
    video = CloudinaryField(
        'video',
        blank=True,
        null=True,
        resource_type='video',   # ✅ critical
        type='upload'
    )

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'portfolio_hero'
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def get_media_url(self):
        if self.media_type == 'image' and self.image:
            return self.image.url
        elif self.media_type == 'video' and self.video:
            return self.video.url
        return None


# ---------------- Projects ----------------
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    details = models.TextField()

    media_type = models.CharField(
        max_length=10,
        choices=[('image', 'Image'), ('video', 'Video')],
        default='image'
    )

    image = CloudinaryField('image', blank=True, null=True)
    video = CloudinaryField(
        'video',
        blank=True,
        null=True,
        resource_type='video',   # ✅ required for Cloudinary videos
        type='upload'
    )
    thumbnail = CloudinaryField('image', blank=True, null=True)

    client = models.CharField(max_length=200, blank=True, null=True)
    project_url = models.URLField(blank=True, null=True)
    technologies = models.CharField(max_length=500, blank=True, null=True)

    is_featured = models.BooleanField(default=False)
    is_published = models.BooleanField(default=True)
    order = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'projects'
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.title

    def get_media_url(self):
        if self.media_type == 'image' and self.image:
            return self.image.url
        elif self.media_type == 'video' and self.video:
            return self.video.url
        return None

    def get_thumbnail_url(self):
        if self.media_type == 'video' and self.thumbnail:
            return self.thumbnail.url
        elif self.media_type == 'image' and self.image:
            return self.image.url
        return None
