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
    
class CoursesViewSet(viewsets.ModelViewSet):
    serializer_class = CoursesSerializer

    def get_queryset(self):
        courses = Courses.objects.all()
        return courses