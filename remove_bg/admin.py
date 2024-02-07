from django.contrib import admin
from .models import Image

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'image','processed_image', 'processed_at')
    search_fields = ('id', 'image__name')  # Adjust based on your model fields

