from rest_framework import serializers
from .models import Post, PostRating

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'body', 'ratings']
        depth = 1

class PostRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostRating
        fields = ['id', 'likes', 'dislikes']