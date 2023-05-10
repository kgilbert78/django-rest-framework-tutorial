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
    

    def put(self, request, *args, **kwargs):
        id = request.query_params["id"]
        car_obj = Cars2.objects.get(id=id)
        # ^ make request to http://localhost:8000/cars-app2/?id=2 and don't include an id in the json
        # video makes requests to cars-app2/2/ instead of cars-app2/?id=2 - that didn't work on mine even after adding path for '<int:id>' to urlpatterns

        data = request.data

        # car_obj = Cars2.objects.get(id=data['id'])
        # ^ alt method i tried: make request to http://localhost:8000/cars-app2/ and put the id in the json

        car_obj.car_brand = data['car_brand']
        car_obj.car_model = data['car_model']
        car_obj.car_year = data['car_year']
        car_obj.car_color = data['car_color']

        car_obj.save()
        serializer = Cars2Serializer(car_obj)
        return Response(serializer.data)
    
