from django.db import models
from cloudinary.models import CloudinaryField

class SiteConfiguration(models.Model):
    """
    Single instance model for site-wide configuration
    """
    logo = CloudinaryField(
        'logo',
        folder='logo',
        blank=True,
        null=True,
        help_text='Upload your site logo (recommended size: 200x60px)'
    )
    site_name = models.CharField(
        max_length=100,
        default='Alex Rodriguez',
        help_text='Name displayed if no logo is uploaded'
    )
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Site Configuration'
        verbose_name_plural = 'Site Configuration'
    
    def __str__(self):
        return 'Site Configuration'
    
    def save(self, *args, **kwargs):
        # Ensure only one instance exists
        if not self.pk and SiteConfiguration.objects.exists():
            raise ValueError('Only one Site Configuration instance is allowed')
        return super().save(*args, **kwargs)
    
    @classmethod
    def get_config(cls):
        """Get or create the site configuration"""
        config, created = cls.objects.get_or_create(pk=1)
        return config