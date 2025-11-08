from django.db import models
from django.core.validators import FileExtensionValidator, MaxValueValidator, MinValueValidator
from cloudinary.models import CloudinaryField

# ---------------- Stats ----------------
class Stat(models.Model):
    name = models.CharField(max_length=100, help_text="e.g., Projects, Happy Clients")
    value = models.CharField(max_length=20, help_text="Value for the stat (e.g., '4M', '500+')")  # Changed to CharField
    suffix = models.CharField(max_length=10, default="", help_text="Optional suffix for the stat (e.g., '+')")  # Made optional
    icon = models.CharField(max_length=50, choices=[
        ('Briefcase', 'Briefcase'),
        ('Users', 'Users'),
        ('Award', 'Award'),
        ('Globe', 'Globe'),
    ], default='Briefcase')
    order = models.PositiveIntegerField(default=0, help_text="Display order (lower numbers appear first)")
    is_active = models.BooleanField(default=True, help_text="Display this stat on the website")

    class Meta:
        ordering = ['order', 'name']
        verbose_name = "Stat"
        verbose_name_plural = "Stats"

    def __str__(self):
        return f"{self.name} - {self.value}{self.suffix}"
#######################################################
class CoreValue(models.Model):
    title = models.CharField(max_length=100, help_text="e.g., Creative Precision")
    description = models.TextField(help_text="Description of the core value")
    icon = models.CharField(
        max_length=50,
        choices=[
             ('Film', 'Film - Creative Precision'),
            ('Users', 'Users - Clarity in Collaboration'),
            ('Heart', 'Heart - Calm Problem-Solving'),
            ('Lightbulb', 'Lightbulb - Growth-Driven Mindset'),
        ],
        default='Heart'
    )
    order = models.PositiveIntegerField(default=0, help_text="Display order (lower numbers appear first)")
    is_active = models.BooleanField(default=True, help_text="Display this core value on the website")

    class Meta:
        ordering = ['order', 'title']
        verbose_name = "Core Value"
        verbose_name_plural = "Core Values"

    def __str__(self):
        return self.title



# ---------------- Timeline ----------------
class TimelineEvent(models.Model):
    year = models.CharField(max_length=4, help_text="e.g., 2016")
    title = models.CharField(max_length=100, help_text="e.g., The Beginning")
    description = models.TextField(help_text="Description of the timeline event")
    icon = models.CharField(max_length=50, choices=[
        ('PlayCircle', 'PlayCircle'),
        ('Award', 'Award'),
        ('Briefcase', 'Briefcase'),
        ('Globe', 'Globe'),
        ('Sparkles', 'Sparkles'),
    ], default='PlayCircle')
    order = models.PositiveIntegerField(default=0, help_text="Display order (lower numbers appear first)")
    is_active = models.BooleanField(default=True, help_text="Display this event on the website")

    class Meta:
        ordering = ['order', 'year']
        verbose_name = "Timeline Event"
        verbose_name_plural = "Timeline Events"

    def __str__(self):
        return f"{self.year} - {self.title}"


# ---------------- Skills ----------------
class Skill(models.Model):
    name = models.CharField(max_length=100, help_text="e.g., Cinematography")
    level = models.PositiveIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        help_text="Skill level as a percentage (0-100)"
    )
    icon = models.CharField(max_length=50, choices=[
        ('Camera', 'Camera'),
        ('Sparkles', 'Sparkles'),
        ('Film', 'Film'),
        ('Zap', 'Zap'),
        ('Target', 'Target'),
        ('Eye', 'Eye'),
    ], default='Camera')
    order = models.PositiveIntegerField(default=0, help_text="Display order (lower numbers appear first)")
    is_active = models.BooleanField(default=True, help_text="Display this skill on the website")

    class Meta:
        ordering = ['order', 'name']
        verbose_name = "Skill"
        verbose_name_plural = "Skills"

    def __str__(self):
        return f"{self.name} - {self.level}%"


# ---------------- About CTA ----------------
class AboutCTA(models.Model):
    title = models.CharField(max_length=200, help_text="e.g., Let's Create Together")
    description = models.TextField(help_text="Description for the CTA section")
    button_text = models.CharField(max_length=100, default="Get In Touch", help_text="Text for the CTA button")
    is_active = models.BooleanField(default=True, help_text="Display this CTA on the website")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "About CTA"
        verbose_name_plural = "About CTAs"

    def __str__(self):
        return self.title


# ---------------- About Tabs ----------------
class AboutTabContent(models.Model):
    TAB_CHOICES = [
        ('story', 'Story'),
        ('process', 'Process'),
        ('philosophy', 'Philosophy'),
    ]

    tab_name = models.CharField(
        max_length=50,
        choices=TAB_CHOICES,
        unique=True,
        help_text="Name of the tab (Story, Philosophy, or Process)"
    )
    title = models.CharField(max_length=100, help_text="e.g., My Journey")
    content = models.TextField(help_text="Content for the tab, supports multiple paragraphs separated by newlines")

    image = CloudinaryField(
        resource_type='image',
        blank=True,
        null=True,
        help_text="Upload tab image"
    )

    is_active = models.BooleanField(default=True, help_text="Display this tab content on the website")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "About Tab Content"
        verbose_name_plural = "About Tab Contents"

    def __str__(self):
        return f"{self.tab_name.title()} - {self.title}"


# ---------------- Generic Media Upload ----------------
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

    def __str__(self):
        return self.title
