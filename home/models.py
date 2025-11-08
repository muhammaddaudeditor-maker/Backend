from django.db import models
from cloudinary.models import CloudinaryField


# ---------------- Media Uploads ----------------
class MediaFile(models.Model):
    title = models.CharField(max_length=255)
    file = CloudinaryField('file', blank=True, null=True, resource_type='auto')  # ✅ handle any type (image/video/pdf)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


# ---------------- Home Hero Section ----------------
class HomeHero(models.Model):
    title = models.CharField(max_length=200, help_text="Main title for the hero section")
    typewriter_phrases = models.TextField(
        help_text="Comma-separated phrases for typewriter effect (e.g., Cinematic Excellence, Visual Storytelling)"
    )
    subtitle = models.TextField(help_text="Subtitle or description for the hero section")

    # ✅ Cloudinary video field
    video = CloudinaryField(
        'video',
        blank=True,
        null=True,
        resource_type='video',  # ensures Cloudinary treats it as a video
    )

    primary_button_text = models.CharField(
        max_length=100, default="Watch Portfolio Reel", help_text="Text for the primary button"
    )
    secondary_button_text = models.CharField(
        max_length=100, default="View Our Work", help_text="Text for the secondary button"
    )
    is_active = models.BooleanField(default=True, help_text="Display this hero content on the website")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Home Hero"
        verbose_name_plural = "Home Hero Sections"
        ordering = ["-updated_at"]

    def __str__(self):
        return self.title


# ---------------- Home Stats ----------------

class HomeStat(models.Model):
    name = models.CharField(max_length=100, help_text="e.g., Projects Completed")
    value = models.CharField(max_length=20, help_text="Value for the stat (e.g., 500, 4M, 10K)")
    suffix = models.CharField(max_length=10, default="", help_text="Suffix for the stat (optional, e.g., '+')")
    icon = models.CharField(  # Changed from CloudinaryField to CharField as per your context
        max_length=50,
        choices=[
            ('Calendar', 'Calendar'),
            ('Users', 'Users'),
            ('Award', 'Award'),
            ('MapPin', 'MapPin'),
        ],
        default='Calendar',
    )
    order = models.PositiveIntegerField(default=0, help_text="Display order (lower numbers appear first)")
    is_active = models.BooleanField(default=True, help_text="Display this stat on the website")

    class Meta:
        ordering = ['order', 'name']
        verbose_name = "Home Stat"
        verbose_name_plural = "Home Stats"

    def __str__(self):
        return f"{self.name} - {self.value}{self.suffix}"


# ---------------- Home Intro ----------------
class HomeIntro(models.Model):
    title = models.CharField(max_length=200, help_text="Main title for the intro section")
    subtitle = models.TextField(help_text="Subtitle or description for the intro section")

    # ✅ Cloudinary image field
    image = CloudinaryField(
        'image',
        blank=True,
        null=True,
        resource_type='image',  # ensures Cloudinary treats it as an image
    )

    achievements = models.TextField(
        help_text="Comma-separated list of recent achievements (e.g., Vimeo Staff Pick Winner 2023, Wedding Wire Couples Choice Award)"
    )
    primary_button_text = models.CharField(
        max_length=100, default="View My Portfolio", help_text="Text for the primary button"
    )
    secondary_button_text = models.CharField(
        max_length=100, default="Contact Me", help_text="Text for the secondary button"
    )
    is_active = models.BooleanField(default=True, help_text="Display this intro content on the website")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Home Intro"
        verbose_name_plural = "Home Intro Sections"
        ordering = ["-updated_at"]

    def __str__(self):
        return self.title


# ---------------- Reusable Components ----------------
class HomeSkill(models.Model):
    title = models.CharField(max_length=100, help_text="e.g., Storytelling")
    description = models.TextField(help_text="Description of the skill")
    icon = models.CharField(
        max_length=50,
        choices=[
            ('PenTool', 'PenTool'),
            ('Palette', 'Palette'),
            ('Music', 'Music'),
            ('Cpu', 'Cpu'),
            ('MessageCircle', 'MessageCircle'),
            ('Edit3', 'Edit3'),
        ],
        default='PenTool',
    )
    order = models.PositiveIntegerField(default=0, help_text="Display order (lower numbers appear first)")
    is_active = models.BooleanField(default=True, help_text="Display this skill on the website")

    class Meta:
        ordering = ['order', 'title']
        verbose_name = "Home Skill"
        verbose_name_plural = "Home Skills"

    def __str__(self):
        return self.title


class HomeService(models.Model):
    title = models.CharField(max_length=100, help_text="e.g., Wedding Films")
    description = models.TextField(help_text="Description of the service")
    icon = models.CharField(
        max_length=50,
        choices=[
            ('Film', 'Film'),
            ('Play', 'Play'),
            ('Award', 'Award'),
        ],
        default='Film',
    )
    order = models.PositiveIntegerField(default=0, help_text="Display order (lower numbers appear first)")
    is_active = models.BooleanField(default=True, help_text="Display this service on the website")

    class Meta:
        ordering = ['order', 'title']
        verbose_name = "Home Service"
        verbose_name_plural = "Home Services"

    def __str__(self):
        return self.title


class HomeProcess(models.Model):
    title = models.CharField(max_length=100, help_text="e.g., Creative Planning")
    description = models.TextField(help_text="Description of the process step")
    icon = models.CharField(
        max_length=50,
        choices=[
            ('PenTool', 'PenTool'),
            ('Camera', 'Camera'),
            ('Edit3', 'Edit3'),
        ],
        default='PenTool',
    )
    order = models.PositiveIntegerField(default=0, help_text="Display order (lower numbers appear first)")
    is_active = models.BooleanField(default=True, help_text="Display this process step on the website")

    class Meta:
        ordering = ['order', 'title']
        verbose_name = "Home Process"
        verbose_name_plural = "Home Processes"

    def __str__(self):
        return self.title


class HomeTool(models.Model):
    title = models.CharField(max_length=100, help_text="e.g., Software")
    description = models.TextField(help_text="Description of the tool")
    icon = models.CharField(
        max_length=50,
        choices=[
            ('Laptop', 'Laptop'),
            ('Camera', 'Camera'),
            ('Workflow', 'Workflow'),
            ('Wifi', 'Wifi'),
        ],
        default='Laptop',
    )
    order = models.PositiveIntegerField(default=0, help_text="Display order (lower numbers appear first)")
    is_active = models.BooleanField(default=True, help_text="Display this tool on the website")

    class Meta:
        ordering = ['order', 'title']
        verbose_name = "Home Tool"
        verbose_name_plural = "Home Tools"

    def __str__(self):
        return self.title


class HomeFAQ(models.Model):
    question = models.CharField(max_length=200, help_text="e.g., What working hours are manageable for you?")
    answer = models.TextField(help_text="Answer to the FAQ")
    order = models.PositiveIntegerField(default=0, help_text="Display order (lower numbers appear first)")
    is_active = models.BooleanField(default=True, help_text="Display this FAQ on the website")

    class Meta:
        ordering = ['order', 'question']
        verbose_name = "Home FAQ"
        verbose_name_plural = "Home FAQs"

    def __str__(self):
        return self.question


class HomeCTA(models.Model):
    title = models.CharField(max_length=200, help_text="e.g., Ready to Start Your Project?")
    description = models.TextField(help_text="Description for the CTA section")
    button_text = models.CharField(max_length=100, default="Contact Me", help_text="Text for the CTA button")
    is_active = models.BooleanField(default=True, help_text="Display this CTA on the website")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Home CTA"
        verbose_name_plural = "Home CTAs"
        ordering = ["-updated_at"]

    def __str__(self):
        return self.title
