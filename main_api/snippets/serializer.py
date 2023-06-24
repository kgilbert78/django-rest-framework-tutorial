from rest_framework import serializers
from .models import Snippets

class SnippetsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippets
        fields = ['id', 'title', 'code', 'language']

class SnippetsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippets
        fields = ['title']