# your_app_name/views.py
from django.utils import timezone

from rest_framework.parsers import MultiPartParser, FormParser
from django.core.files.base import ContentFile

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Image
from .serializers import ImageSerializer
from rembg import remove
class ImageListCreateAPIView(APIView):
    def get(self, request):
        images = Image.objects.all()
        serializer = ImageSerializer(images, many=True)
        return Response(serializer.data)
class RemoveBgAPIView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request):
        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
            image = serializer.validated_data['image']

            # Read the file content before closing the file
            image_content = image.read()

            # Process the image content
            processed_image_content = remove(image_content)

            # Save the processed image to the processed_image field
            processed_image = Image(image=image, processed_at=timezone.now())
            processed_image.processed_image.save('processed_image.png', ContentFile(processed_image_content))
            # Return JSON data with relevant details
            response_data = {
                'id': processed_image.id,
                'processed_at': processed_image.processed_at.isoformat(),
                'processed_image_url': processed_image.processed_image.url,
                'message': 'Image processed successfully!'
            }

            return Response(response_data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

















# class RemoveBgAPIView(APIView):
#     parser_classes = (MultiPartParser, FormParser)

#     def post(self, request):
#         serializer = ImageSerializer(data=request.data)
#         if serializer.is_valid():
#             image = serializer.validated_data['image']

#             # Read the file content before closing the file
#             image_content = image.read()

#             # Process the image content
#             processed_image_content = remove(image_content)

#             # Save the processed image to the processed_image field
#             processed_image = Image(image=image)
#             processed_image.processed_image.save('processed_image.png', ContentFile(processed_image_content))

#             return Response(serializer.data, status=status.HTTP_201_CREATED)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
