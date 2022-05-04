from django.db import models
from django.conf import settings
from django.urls import reverse
from django.template.defaultfilters import slugify
from django.utils.text import slugify

from PIL import Image





class News(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True, unique_for_date="created_at")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='tweaks')
    content = models.TextField()
    image = models.ImageField(upload_to = 'uploads', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    class Meta:
        ordering = ['-created_at']