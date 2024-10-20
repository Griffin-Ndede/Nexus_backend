from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from .models import Video
from .serializers import VideoSerializer

class VideoUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        video_serializer = VideoSerializer(data=request.data)
        if video_serializer.is_valid():
            video_serializer.save()
            return Response(video_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(video_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VideoListView(APIView):
    def get(self, request, *args, **kwargs):
        videos = Video.objects.all()
        video_serializer = VideoSerializer(videos, many=True)
        return Response(video_serializer.data)
