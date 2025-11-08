# app: cv_upload/models.py
from django.db import models

class CVUpload(models.Model):
    title = models.CharField(max_length=200, default="My CV")
    # Use FileField. Upload path is MEDIA_ROOT/cv_files/
    cv_file = models.FileField(upload_to='cv_files/', null=True, blank=True)

    uploaded_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True, help_text="Only one CV can be active at a time")

    class Meta:
        verbose_name = "CV Upload"
        verbose_name_plural = "CV Uploads"
        ordering = ['-updated_at']

    def __str__(self):
        return f"{self.title} - {'Active' if self.is_active else 'Inactive'}"

    def save(self, *args, **kwargs):
        # Ensure only one active CV
        if self.is_active:
            CVUpload.objects.exclude(pk=self.pk).update(is_active=False)
        super().save(*args, **kwargs)

    @property
    def cv_url(self):
        """Return the URL for the CV file (works for local and cloud storage)."""
        if self.cv_file:
            return self.cv_file.url
        return None

    @property
    def download_url(self):
        """
        Return a URL intended to force download when possible.
        For Cloudinary-hosted files the URL structure may include '/upload/' and we can inject 'fl_attachment'.
        For local files this simply returns the file URL (servers often open PDF inline).
        """
        url = self.cv_url
        if not url:
            return None

        # If it looks like a Cloudinary URL, insert fl_attachment after upload/
        if '/upload/' in url:
            return url.replace('/upload/', '/upload/fl_attachment/')
        # Otherwise return local URL (or any storage-provided URL) as-is
        return url
