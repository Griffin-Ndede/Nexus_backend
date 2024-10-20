from rest_framework import serializers
from .models import Video

class VideoSerializer(serializers.ModelSerializer):
    video_url = serializers.SerializerMethodField()  # Add this line for the absolute URL

    class Meta:
        model = Video
        fields = ('id', 'title', 'description', 'video_file', 'uploaded_at', 'video_url')  # Include the new field

    def get_video_url(self, obj):
        request = self.context.get('request')  # Get the request from the context
        if request:
            return request.build_absolute_uri(obj.video_file.url)  # Build the absolute URL
        return None
