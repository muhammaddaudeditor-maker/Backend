# testimonials/models.py
from django.db import models   # ← THIS WAS MISSING!


class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100, help_text='e.g., Wedding Couple, Real Estate Agent')
    company = models.CharField(max_length=100, blank=True, null=True)
    text = models.TextField(help_text='Testimonial content')
    rating = models.IntegerField(
        default=5,
        choices=[(i, i) for i in range(1, 6)],
        help_text='Rating from 1 to 5 stars'
    )
    avatar = models.CharField(max_length=10, blank=True, help_text="e.g. JD")
    avatar_url = models.URLField(blank=True, null=True)
    gradient_color = models.CharField(
        max_length=100,
        default="from-purple-500 to-pink-500",
        help_text="Tailwind gradient classes, e.g. from-blue-500 to-cyan-500"
    )
    is_active = models.BooleanField(default=True)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', '-created_at']
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonials'

    def __str__(self):
        return f"{self.name} - {self.rating} stars"