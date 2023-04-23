from rest_framework import viewsets
from rest_framework.response import Response
from .models import Post, PostRating
from .serializer import PostSerializer, PostRatingSerializer


# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer

    def get_queryset(self):
        posts = Post.objects.all()
        return posts
    
class PostRatingViewSet(viewsets.ModelViewSet):
    serializer_class = PostRatingSerializer

    def get_queryset(self):
        ratings = PostRating.objects.all()
        return ratings