from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import Cars2Serializer
from .models import Cars2

# Create your views here.
class Cars2APIView(APIView):
    serializer_class = Cars2Serializer

    def get_queryset(self):
        cars2 = Cars2.objects.all()
        return cars2
    
    def get(self, request, *args, **kwargs):
        try:
            req_id = request.query_params['id']
            # print("id:", req_id)
            car2 = Cars2.objects.get(id=req_id)
            serializer = Cars2Serializer(car2)
        except:
            cars2 = self.get_queryset()
            serializer = Cars2Serializer(cars2, many=True)
        return Response(serializer.data)
    
    # nearly identical to create function override in cars-app CarViewSet. with APIView you won't be able to post data without adding this manually though.
    def post(self, request, *args, **kwargs):
        data = request.data
        new_car = Cars2.objects.create(car_brand=data["car_brand"], car_model=data["car_model"], car_year=data["car_year"], car_color=data["car_color"])

        new_car.save()

        serializer = Cars2Serializer(new_car)

        return Response(serializer.data)