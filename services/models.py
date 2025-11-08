from django.db import models
from django.core.validators import FileExtensionValidator
from cloudinary.models import CloudinaryField

# ---------------- MediaFile ----------------
class MediaFile(models.Model):
    title = models.CharField(max_length=255)
    file = CloudinaryField('file', blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


# ---------------- Services ----------------
class Service(models.Model):
    ICON_CHOICES = [
        ('Heart', 'Heart'),
        ('Home', 'Home'),
        ('User', 'User'),
        ('Palette', 'Palette'),
        ('Camera', 'Camera'),
    ]

    title = models.CharField(max_length=100)
    icon = models.CharField(max_length=50, choices=ICON_CHOICES, default='Camera')

    # ✅ Fixed: CloudinaryField with resource_type for video
    video = CloudinaryField(
        'video', 
        blank=True, 
        null=True,
        resource_type='video',  # ✅ CRITICAL: Specify resource_type
        type='upload'
    )

    description = models.TextField(help_text='Main service description')
    is_active = models.BooleanField(default=True, help_text='Display this service on the website')
    order = models.IntegerField(default=0, help_text='Display order (lower numbers appear first)')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', 'title']
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self):
        return self.title


# ---------------- Service Features ----------------
class ServiceFeature(models.Model):
    service = models.ForeignKey(
        Service,
        on_delete=models.CASCADE,
        related_name='features'
    )
    feature_text = models.CharField(max_length=100)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order', 'feature_text']
        verbose_name = 'Service Feature'
        verbose_name_plural = 'Service Features'

    def __str__(self):
        return f"{self.service.title} - {self.feature_text}"


# ---------------- Process Steps ----------------
class ProcessStep(models.Model):
    step_number = models.CharField(max_length=10, help_text='e.g., 01, 02, 03')
    title = models.CharField(max_length=100)
    description = models.TextField()
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']
        verbose_name = 'Process Step'
        verbose_name_plural = 'Process Steps'

    def __str__(self):
        return f"Step {self.step_number}: {self.title}"


# ---------------- Equipment ----------------
class EquipmentCategory(models.Model):
    name = models.CharField(max_length=100)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order', 'name']
        verbose_name = 'Equipment Category'
        verbose_name_plural = 'Equipment Categories'

    def __str__(self):
        return self.name


class EquipmentItem(models.Model):
    category = models.ForeignKey(
        EquipmentCategory,
        on_delete=models.CASCADE,
        related_name='items'
    )
    item_name = models.CharField(max_length=100)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order', 'item_name']
        verbose_name = 'Equipment Item'
        verbose_name_plural = 'Equipment Items'

    def __str__(self):
        return f"{self.category.name} - {self.item_name}"


# ---------------- Testimonials ----------------
class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100, help_text='e.g., Wedding Couple, Real Estate Agent')
    text = models.TextField(help_text='Testimonial content')
    rating = models.IntegerField(
        default=5,
        choices=[(i, i) for i in range(1, 6)],
        help_text='Rating from 1 to 5 stars'
    )
    is_active = models.BooleanField(default=True)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', '-created_at']
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonials'

    def __str__(self):
        return f"{self.name} - {self.role}"


# ---------------- Site Stats ----------------
class SiteStats(models.Model):
    projects_completed = models.IntegerField(default=500)
    happy_clients = models.IntegerField(default=300)
    industry_awards = models.IntegerField(default=15)
    client_satisfaction = models.IntegerField(default=98, help_text='Percentage')
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Site Statistics'
        verbose_name_plural = 'Site Statistics'

    def __str__(self):
        return f"Site Stats (Updated: {self.updated_at.strftime('%Y-%m-%d')})"

    def save(self, *args, **kwargs):
        # Ensure only one instance exists
        if not self.pk and SiteStats.objects.exists():
            raise ValueError('Only one SiteStats instance is allowed')
        return super().save(*args, **kwargs)