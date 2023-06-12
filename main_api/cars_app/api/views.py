from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .serializer import CarSerializer
from ..models import Car, Owner, ServicePlan

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
    throttle_scope = "cars_app"


    def get_queryset(self):
        car = Car.objects.all()
        return car
    
    def retrieve(self, request, *args, **kwargs):
        params = kwargs
        # print(params) # url .../car-data/Ford/ prints {'pk': 'Ford'}

        # print(params['pk'], params['pk'].isnumeric())
        if params['pk'].isnumeric():
            id=params['pk']
            id_match = Car.objects.get(pk=id)
            print("id_match", type(id_match), id_match)
            serializer = CarSerializer(id_match)
            return Response(serializer.data)

        if '-' in params['pk']:
            param_list = params['pk'].split('-')
            # print(param_list) # ['Ford', 'Focus']
            selected_cars = Car.objects.filter(
                car_brand=param_list[0],
                car_model=param_list[1]
            )
        else:
            selected_cars = Car.objects.filter(
                car_brand=params['pk']
            )
        # print("selected cars:", selected_cars)
        serializer = CarSerializer(selected_cars, many=True)
        return Response(serializer.data)
    
    def create(self, request, *args, **kwargs):
        data = request.data
        new_car = Car.objects.create(owner=Owner.objects.get(id=data["owner"]), service_plan=ServicePlan.objects.get(id=data["service_plan"]), car_brand=data["car_brand"], car_model=data["car_model"], car_year=data["car_year"], car_color=data["car_color"])

        # implement checks here before saving data
        # (check brand spellings, verify that years are numbers and within certain range, etc.)

        new_car.save()

        serializer = CarSerializer(new_car)

        return Response(serializer.data)

    # without this, the default behavior of delete does not return any data showing that the car with the id you specified in the url has been deleted.
    def destroy(self, request, *args, **kwargs):

        logged_in_user = request.user
        # print(logged_in_user, type(logged_in_user)) # admin <class 'django.contrib.auth.models.User'>
        if str(logged_in_user) == "admin":
            car = self.get_object()
            car.delete()

            brand = request.data['car_brand']
            model = request.data['car_model']
            year = request.data['car_year']
            color = request.data['car_color']

            response_message = {"message": f"{color} {year} {brand} {model} has been deleted"}
        else:
            response_message = {"message": "You do not have authorization to delete this."}

        return Response(response_message)
    
    # called update not put because using modelviewset, not api view
    def update(self, request, *args, **kwargs):
        car_obj = self.get_object()
        data = request.data
        # print("data:", data)

        # type id's for service_plan & owner in values for "service_plan" & "owner" in request json - frontend would look the plan or person up by name to get id
        service_plan = ServicePlan.objects.get(id=data["service_plan"])
        car_obj.service_plan = service_plan

        owner = Owner.objects.get(id=data["owner"])
        car_obj.owner = owner

        car_obj.car_brand = data['car_brand']
        car_obj.car_model = data['car_model']
        car_obj.car_year = data['car_year']
        car_obj.car_color = data['car_color']

        car_obj.save()
        serializer = CarSerializer(car_obj)
        return Response(serializer.data)
    
    def partial_update(self, request, *args, **kwargs):
        car_obj = self.get_object()
        data = request.data

        # check request data for field, if present update it, not present keep existing field data

        try:
            service_plan = ServicePlan.objects.get(id=data["service_plan"])
            car_obj.service_plan = service_plan
        except KeyError: # this will occur if field not in request data
            pass

        try:
            owner = Owner.objects.get(id=data["owner"])
            car_obj.owner = owner
        except KeyError:
            pass

        car_obj.car_brand = data.get('car_brand', car_obj.car_brand)
        car_obj.car_model = data.get('car_model', car_obj.car_model)
        car_obj.car_year = data.get('car_year', car_obj.car_year)
        car_obj.car_color = data.get('car_color', car_obj.car_color)

        car_obj.save()
        serializer = CarSerializer(car_obj)

        return Response(serializer.data)