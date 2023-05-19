from django.urls import path
from .views import Cars2APIView, Cars2DetailView

urlpatterns = [
    path('', Cars2APIView.as_view()),
    path('<int:id>/', Cars2DetailView.as_view())
] # left ^ blank for endpoint at cars-app2/
# if i added 'cars2' endpoint would be cars-app2/cars2