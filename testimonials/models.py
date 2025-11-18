# testimonials/models.py
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Testimonial(models.Model):
    name = models.CharField(max_length=100, help_text="Client's full name")
    role = models.CharField(max_length=100, help_text="e.g. Startup Founder, Wedding Client")
    company = models.CharField(max_length=150, help_text="Company or event name")
    text = models.TextField(help_text="The testimonial quote")
    
    rating = models.PositiveSmallIntegerField(
        default=5,
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        help_text="Rating from 1 to 5 stars"
    )
    
    # Optional avatar image (you can upload real photos)
    avatar_image = models.ImageField(
        upload_to='testimonials/avatars/',
        blank=True,
        null=True,
        help_text="Optional client photo (falls back to initials)"
    )
    
    # Auto-generated initials (e.g. "JW")
    avatar_initials = models.CharField(max_length=3, blank=True, editable=False)
    
    # Tailwind gradient class
    gradient_color = models.CharField(
        max_length=100,
        default="from-indigo-500 to-purple-500",
        help_text="Tailwind gradient (e.g. from-indigo-500 to-purple-500)"
    )
    
    order = models.PositiveIntegerField(default=0, help_text="Display order (lower = first)")
    is_active = models.BooleanField(default=True, help_text="Show on website?")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', 'created_at']
        verbose_name = "Testimonial"
        verbose_name_plural = "Testimonials"

    def save(self, *args, **kwargs):
        # Auto-generate initials from name
        if not self.avatar_initials:
            parts = self.name.strip().split()
            initials = ""
            if len(parts) >= 2:
                initials = (parts[0][0] + parts[-1][0]).upper()
            elif parts:
                initials = parts[0][:2].upper()
            self.avatar_initials = initials or "??"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} ({self.company}) - {self.rating} stars"