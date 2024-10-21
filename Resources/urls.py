from django.urls import path
from .views import VideoUploadView, VideoListView, CategoriesView

urlpatterns = [
    path('upload/', VideoUploadView.as_view(), name='video-upload'),
    path('videos/', VideoListView.as_view(), name='video-list'),
    path('categories/', CategoriesView.as_view(), name = 'Categories'),
]

