from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from .models import Video
from .serializers import VideoSerializer, CategoriesSerializer
from .models import Categories

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
        video_serializer = VideoSerializer(videos, many=True, context={'request': request})  # Pass the request context
        return Response(video_serializer.data)

class CategoriesView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, *args, **kwargs):
        categories = Categories.objects.all()
        serializer = CategoriesSerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        Categoriess_serializer = CategoriesSerializer(data=request.data)
        if Categoriess_serializer.is_valid():
            Categoriess_serializer.save()
            return Response(Categoriess_serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('error', Categoriess_serializer.errors)
            return Response(Categoriess_serializer.errors, status=status.HTTP_400_BAD_REQUEST)