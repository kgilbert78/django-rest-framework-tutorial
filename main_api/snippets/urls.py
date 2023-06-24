from django.urls import path, include
from .views import SnippetsDetailView, SnippetsListView

urlpatterns = [
    path('snippets/', SnippetsListView.as_view(), name='snippet-list'),
    path('detail/<int:pk>/', SnippetsDetailView.as_view(), name='snippet-detail')
]