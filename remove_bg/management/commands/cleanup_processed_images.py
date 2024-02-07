# photo_tools/management/commands/cleanup_processed_images.py
from django.core.management.base import BaseCommand
from django.utils import timezone
from models import Image

class Command(BaseCommand):
    help = 'Deletes processed images older than 10 minutes.'

    def handle(self, *args, **kwargs):
        ten_minutes_ago = timezone.now() - timezone.timedelta(minutes=10)
        old_images = Image.objects.filter(processed_at__lt=ten_minutes_ago)

        for image in old_images:
            image.processed_image.delete()
            image.delete()

        self.stdout.write(self.style.SUCCESS('Successfully deleted old processed images.'))
