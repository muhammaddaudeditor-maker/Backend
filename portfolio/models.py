from django.db import models

# ---------------- Media Uploads ----------------
class MediaFile(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='media_files/', blank=True, null=True)  # Local server storage
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Media File"
        verbose_name_plural = "Media Files"

    def __str__(self):
        return self.title


# ---------------- Portfolio Category ----------------
class PortfolioCategory(models.Model):
    name = models.CharField(max_length=100, help_text='e.g., Wedding, Real Estate')
    icon = models.CharField(max_length=50, choices=[
        ('Sparkles', 'Sparkles'),
        ('Heart', 'Heart'),
        ('Building2', 'Building2'),
        ('MessageCircle', 'MessageCircle'),
        ('Film', 'Film'),
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
    thumbnail = models.ImageField(upload_to='portfolio/thumbnails/', blank=True, null=True)
    video = models.FileField(upload_to='portfolio/videos/', blank=True, null=True)
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
