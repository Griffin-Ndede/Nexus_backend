from rest_framework import serializers
from .models import Video

class VideoSerializer(serializers.ModelSerializer):
    video_url = serializers.SerializerMethodField()  # Absolute URL for the video file
    cover_image_url = serializers.SerializerMethodField()  # Absolute URL for the cover image

    class Meta:
        model = Video
        fields = ('id', 'title', 'description', 'video_file', 'cover_image', 'uploaded_at', 'video_url', 'cover_image_url')  # Include the new field

    def get_video_url(self, obj):
        request = self.context.get('request')  # Get the request from the context
        if request:
            return request.build_absolute_uri(obj.video_file.url)  # Build the absolute URL
        return None

    def get_cover_image_url(self, obj):
        request = self.context.get('request')  # Get the request from the context
        if request and obj.cover_image:
            return request.build_absolute_uri(obj.cover_image.url)  # Build the absolute URL for the cover image
        return None
