from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.pagination import LimitOffsetPagination
from .models import Snippets
from .serializer import SnippetsDetailSerializer, SnippetsListSerializer

# Create your views here.
class SnippetsListView(ListAPIView):
    queryset = Snippets.objects.all()
    serializer_class = SnippetsListSerializer
    pagination_class = LimitOffsetPagination
    # Pagination is only performed automatically if you're using the generic views or viewsets. If you're using a regular APIView, you'll need to call into the pagination API yourself to ensure you return a paginated response. 

class SnippetsDetailView(RetrieveAPIView):
    queryset = Snippets.objects.all()
    serializer_class = SnippetsDetailSerializer