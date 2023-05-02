from django.db import models

# Create your models here.
class Courses(models.Model):
    name = models.CharField(max_length=50)
    duration_months = models.IntegerField()
    classroom = models.IntegerField()

    def __str__(self) -> str:
        return self.name
    

class Students(models.Model):
    first_name = models.CharField(max_length=20 )
    last_name = models.CharField(max_length=20)
    age = models.IntegerField()
    grade = models.IntegerField()
    courses = models.ManyToManyField(Courses)

    def __str__(self) -> str:
        return self.first_name + ' ' + self.last_name