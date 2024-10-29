from rest_framework import serializers
from .models import Form1Video, Form2Video, Form3Video, Form4Video, Categories


class HomeSerializer(serializers.Serializer):
    message = serializers.CharField()
    
class BaseVideoSerializer(serializers.ModelSerializer):
    video_url = serializers.SerializerMethodField()  # Absolute URL for the video file
    cover_image_url = serializers.SerializerMethodField()  # Absolute URL for the cover image

    class Meta:
        fields = ('id', 'title', 'description', 'video_file', 'cover_image', 'uploaded_at', 'video_url', 'cover_image_url')

    def get_video_url(self, obj):
        request = self.context.get('request')
        if request:
            return request.build_absolute_uri(obj.video_file.url)
        return None

    def get_cover_image_url(self, obj):
        request = self.context.get('request')
        if request and obj.cover_image:
            return request.build_absolute_uri(obj.cover_image.url)
        return None

# Define serializers for each form
class Form1VideoSerializer(BaseVideoSerializer):
    class Meta(BaseVideoSerializer.Meta):
        model = Form1Video

class Form2VideoSerializer(BaseVideoSerializer):
    class Meta(BaseVideoSerializer.Meta):
        model = Form2Video

class Form3VideoSerializer(BaseVideoSerializer):
    class Meta(BaseVideoSerializer.Meta):
        model = Form3Video

class Form4VideoSerializer(BaseVideoSerializer):
    class Meta(BaseVideoSerializer.Meta):
        model = Form4Video

class CategoriesSerializer(serializers.ModelSerializer):
    image_url = serializers.ImageField(required=False)

    class Meta:
        model = Categories
        fields = "__all__"
