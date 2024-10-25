from django.urls import path
from .views import (
    Form1VideoUploadView, Form1VideoListView,
    Form2VideoUploadView, Form2VideoListView,
    Form3VideoUploadView, Form3VideoListView,
    Form4VideoUploadView, Form4VideoListView,
    CategoriesView
)

urlpatterns = [
    # Form 1 Video URLs
    path('upload/form1/', Form1VideoUploadView.as_view(), name='form1-video-upload'),
    path('videos/form1/', Form1VideoListView.as_view(), name='form1-video-list'),

    # Form 2 Video URLs
    path('upload/form2/', Form2VideoUploadView.as_view(), name='form2-video-upload'),
    path('videos/form2/', Form2VideoListView.as_view(), name='form2-video-list'),

    # Form 3 Video URLs
    path('upload/form3/', Form3VideoUploadView.as_view(), name='form3-video-upload'),
    path('videos/form3/', Form3VideoListView.as_view(), name='form3-video-list'),

    # Form 4 Video URLs
    path('upload/form4/', Form4VideoUploadView.as_view(), name='form4-video-upload'),
    path('videos/form4/', Form4VideoListView.as_view(), name='form4-video-list'),

    # Categories
    path('categories/', CategoriesView.as_view(), name='categories'),
]
