from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Snippets
from .serializer import SnippetsDetailSerializer, SnippetsListSerializer

# Create your views here.
class SnippetsListView(ListAPIView):
    queryset = Snippets.objects.all()
    serializer_class = SnippetsListSerializer

class SnippetsDetailView(RetrieveAPIView):
    queryset = Snippets.objects.all()
    serializer_class = SnippetsDetailSerializer