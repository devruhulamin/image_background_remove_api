# your_app_name/urls.py
from django.urls import path
from .views import ImageListCreateAPIView,RemoveBgAPIView

urlpatterns = [
    path('images/', ImageListCreateAPIView.as_view(), name='image-list-create'),
    path('remove-bg/',RemoveBgAPIView.as_view(), name='remove_bg'),

]
