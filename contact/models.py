from django.db import models
from cloudinary.models import CloudinaryField


# ---------------- Media Uploads ----------------
class MediaFile(models.Model):
    title = models.CharField(max_length=255)
    file = CloudinaryField(
        resource_type='auto',
        blank=True,
        null=True,
        help_text="Upload any media file (image, video, etc.)"
    )
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Media File"
        verbose_name_plural = "Media Files"
        ordering = ['-uploaded_at']

    def __str__(self):
        return self.title


# ---------------- Contact Info ----------------
class ContactInfo(models.Model):
    ICON_CHOICES = [
        ('Phone', 'Phone'),
        ('Mail', 'Mail'),
        ('MapPin', 'MapPin'),
        ('Clock', 'Clock'),
    ]

    icon = models.CharField(max_length=50, choices=ICON_CHOICES, help_text="Select an icon to represent the contact method")
    title = models.CharField(max_length=100, help_text="Label for the contact info (e.g., 'Email Us')")
    info = models.CharField(max_length=200, help_text="The actual contact information (e.g., example@email.com)")
    link = models.URLField(max_length=500, blank=True, help_text="Optional link (e.g., mailto:, tel:, or map link)")
    order = models.PositiveIntegerField(default=0, help_text="Display order (lower numbers appear first)")
    is_active = models.BooleanField(default=True, help_text="Show or hide this contact info item")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order']
        verbose_name = 'Contact Information'
        verbose_name_plural = 'Contact Information'

    def __str__(self):
        return f"{self.title} - {self.info}"


# ---------------- Why Choose Us ----------------
class WhyChooseUs(models.Model):
    ICON_CHOICES = [
        ('Award', 'Award'),
        ('Star', 'Star'),
        ('Heart', 'Heart'),
        ('Camera', 'Camera'),
        ('Users', 'Users'),
        ('TrendingUp', 'TrendingUp'),
    ]

    icon = models.CharField(max_length=50, choices=ICON_CHOICES)
    title = models.CharField(max_length=100, help_text="Heading for this feature (e.g., 'Award Winning Team')")
    description = models.TextField(help_text="Short description of why clients should choose you")
    order = models.PositiveIntegerField(default=0, help_text="Display order (lower numbers appear first)")
    is_active = models.BooleanField(default=True, help_text="Show or hide this item on the website")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order']
        verbose_name = 'Why Choose Us'
        verbose_name_plural = 'Why Choose Us'

    def __str__(self):
        return self.title


# ---------------- Hero Section ----------------
class HeroSection(models.Model):
    PAGE_CHOICES = [
        ('contact', 'Contact Page'),
        ('services', 'Services Page'),
        ('home', 'Home Page'),
        ('about', 'About Page'),
    ]

    MEDIA_TYPE_CHOICES = [
        ('video', 'Video'),
        ('image', 'Image'),
    ]

    page = models.CharField(max_length=50, choices=PAGE_CHOICES, unique=True, help_text="Assign this hero section to a specific page")
    title = models.CharField(max_length=200, help_text="Main heading text for the hero section")
    subtitle = models.TextField(help_text="Short description or subtitle")
    description = models.TextField(blank=True, help_text="Optional longer text for the hero section")
    badge_text = models.CharField(max_length=100, blank=True, help_text="Small text badge (optional)")
    badge_icon = models.CharField(max_length=50, blank=True, help_text="Icon for the badge (e.g., MessageSquare, Award)")

    media_type = models.CharField(max_length=10, choices=MEDIA_TYPE_CHOICES, default='video')

    # ✅ Cloudinary fields (safe for both image and video)
    video = CloudinaryField(
        resource_type='video',
        blank=True,
        null=True,
        help_text="Upload background video"
    )
    image = CloudinaryField(
        resource_type='image',
        blank=True,
        null=True,
        help_text="Upload background image"
    )

    is_active = models.BooleanField(default=True, help_text="Show or hide this hero section on the assigned page")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Hero Section'
        verbose_name_plural = 'Hero Sections'

    def __str__(self):
        return f"Hero Section - {self.get_page_display()}"

    def get_media_url(self):
        """Returns correct Cloudinary URL depending on the selected media type."""
        if self.media_type == 'video' and self.video:
            return self.video.url
        elif self.media_type == 'image' and self.image:
            return self.image.url
        return None


# ---------------- Contact Messages ----------------
class ContactMessage(models.Model):
    name = models.CharField(max_length=100, help_text="Name of the sender")
    email = models.EmailField(help_text="Email address of the sender")
    whatsapp = models.CharField(max_length=20, blank=True, help_text="Optional WhatsApp number")
    subject = models.CharField(max_length=200, help_text="Message subject")
    message = models.TextField(help_text="Message content")
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False, help_text="Mark as read after viewing in admin")
    replied = models.BooleanField(default=False, help_text="Mark if you have replied to this message")
    admin_notes = models.TextField(blank=True, help_text="Internal notes for admins (not shown to users)")

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Contact Message'
        verbose_name_plural = 'Contact Messages'

    def __str__(self):
        return f"{self.name} - {self.subject} ({self.created_at.strftime('%Y-%m-%d')})"
