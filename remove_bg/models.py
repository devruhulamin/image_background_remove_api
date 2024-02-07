from django.utils import timezone
from django.db import models



class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    processed_image = models.ImageField(upload_to='processed_images/', blank=True, null=True)
    processed_at = models.DateTimeField(default=timezone.now)


