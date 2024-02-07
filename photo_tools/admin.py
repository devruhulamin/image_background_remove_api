# photo_tools/admin.py
from django.contrib import admin
from remove_bg.models import Image

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'processed_at')
    search_fields = ('id', 'image__name')  # Adjust based on your model fields

# If you want to customize the admin further, you can do so in the ImageAdmin class
