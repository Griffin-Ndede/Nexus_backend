from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from .models import Form1Video, Form2Video, Form3Video, Form4Video, Categories
from .serializers import Form1VideoSerializer, Form2VideoSerializer, Form3VideoSerializer, Form4VideoSerializer, CategoriesSerializer

class BaseVideoUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    serializer_class = None
    model_class = None

    def post(self, request, *args, **kwargs):
        video_serializer = self.serializer_class(data=request.data)
        if video_serializer.is_valid():
            video_serializer.save()
            return Response(video_serializer.data, status=status.HTTP_201_CREATED)
        return Response(video_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Form1VideoUploadView(BaseVideoUploadView):
    serializer_class = Form1VideoSerializer
    model_class = Form1Video

class Form2VideoUploadView(BaseVideoUploadView):
    serializer_class = Form2VideoSerializer
    model_class = Form2Video

class Form3VideoUploadView(BaseVideoUploadView):
    serializer_class = Form3VideoSerializer
    model_class = Form3Video

class Form4VideoUploadView(BaseVideoUploadView):
    serializer_class = Form4VideoSerializer
    model_class = Form4Video

class BaseVideoListView(APIView):
    serializer_class = None
    model_class = None

    def get(self, request, *args, **kwargs):
        videos = self.model_class.objects.all()
        video_serializer = self.serializer_class(videos, many=True, context={'request': request})
        return Response(video_serializer.data)

class Form1VideoListView(BaseVideoListView):
    serializer_class = Form1VideoSerializer
    model_class = Form1Video

class Form2VideoListView(BaseVideoListView):
    serializer_class = Form2VideoSerializer
    model_class = Form2Video

class Form3VideoListView(BaseVideoListView):
    serializer_class = Form3VideoSerializer
    model_class = Form3Video

class Form4VideoListView(BaseVideoListView):
    serializer_class = Form4VideoSerializer
    model_class = Form4Video

class CategoriesView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, *args, **kwargs):
        categories = Categories.objects.all()
        serializer = CategoriesSerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        categories_serializer = CategoriesSerializer(data=request.data)
        if categories_serializer.is_valid():
            categories_serializer.save()
            return Response(categories_serializer.data, status=status.HTTP_201_CREATED)
        return Response(categories_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
