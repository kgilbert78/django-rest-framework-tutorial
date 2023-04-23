from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .serializer import CarSerializer
from ..models import Car

@api_view()
# @permission_classes([IsAuthenticated])
def drive(request):
    # print(request.query_params) 
        # url .../cars/?id=1 prints <QueryDict: {'id': ['1']}>
        # url .../cars/?id=1&key=25 prints <QueryDict: {'id': ['1'], 'key': ['25']}>
    # print(request.query_params['id']) # ^ prints 1
    # print(request.query_params['key']) # ^ prints 25
    id = None
    if request.query_params:
        params = list(request.query_params) # create list of the keys in param QueryDict
        if 'id' in params:
            id = int(request.query_params['id']) # convert from string for calculations
    return Response({"message": "vroom!", "id": id, "doubled-id": id*2})

class CarViewSet(viewsets.ModelViewSet):
    serializer_class = CarSerializer

    def get_queryset(self):
        car = Car.objects.all()
        return car
    
    def retrieve(self, request, *args, **kwargs):
        params = kwargs
        # print(params) # url .../car-data/Ford/ prints {'pk': 'Ford'}
        param_list = params['pk'].split('-')
        print(param_list) # ['Ford', 'Focus']
        selected_cars = Car.objects.filter(
            car_brand=param_list[0],
            car_model=param_list[1]
        )
        serializer = CarSerializer(selected_cars, many=True)
        return Response(serializer.data)