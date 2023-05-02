from rest_framework import serializers
from .models import Courses, Students

class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = ['id', 'name', 'duration_months', 'classroom']


class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = ['id', 'first_name', 'last_name', 'age', 'grade', 'courses']
        depth = 1
