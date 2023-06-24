from rest_framework import serializers
from .models import Snippets

class SnippetsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippets
        fields = ['id', 'title', 'code', 'language']

class SnippetsListSerializer(serializers.ModelSerializer):
    snippet_details = serializers.HyperlinkedIdentityField(view_name='snip:snippet-detail')
    # view_name = <namespace in main_api urls.py>:<name of detail path in this app's urls.py>
    class Meta:
        model = Snippets
        fields = ['title', 'snippet_details']