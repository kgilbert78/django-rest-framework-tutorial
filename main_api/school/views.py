from rest_framework import viewsets
from rest_framework.response import Response
from .models import Courses, Students
from .serializer import CoursesSerializer, StudentsSerializer

# Create your views here.
class StudentsViewSet(viewsets.ModelViewSet):
    serializer_class = StudentsSerializer

    def get_queryset(self):
        students = Students.objects.all()
        return students
    
    def create(self, request, *args, **kwargs):
        data = request.data
        new_student = Students.objects.create(first_name=data['first_name'], last_name=data['last_name'], age=data['age'], grade=data['grade'])
        
        new_student.save()

        # practice changing this to a map function later :)
        for course in data['courses']:
            course_obj = Courses.objects.get(name=course['name'])
            new_student.courses.add(course_obj)
            # for POST request data format like this:
            # {
            #     "first_name": "Testy",
            #     "last_name": "McTesterson",
            #     "age": 15,
            #     "grade": 10,
            #     "courses": [{"name": "English"}, {"name": "Art"}, {"name": "Geometry"}]
            # }

        # for course_id in data['courses']:
        #     course_obj = Courses.objects.get(id=course_id)
        #     new_student.courses.add(course_obj)

            # for POST request data format like this:
            # {
            #     "first_name": "Testy",
            #     "last_name": "McTesterson",
            #     "age": 15,
            #     "grade": 10,
            #     "courses": [1,2,3]
            # }

            # or you could send the course names like ["English", "Art"] etc. and use name=course_name instead of id=course_id

        serializer = StudentsSerializer(new_student)

        return Response(serializer.data)
    
class CoursesViewSet(viewsets.ModelViewSet):
    serializer_class = CoursesSerializer

    def get_queryset(self):
        courses = Courses.objects.all()
        return courses