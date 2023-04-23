from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=1000)

    def __str__(self) -> str:
        return self.title
    
class PostRating(models.Model):
    likes = models.BigIntegerField(default=0)
    dislikes = models.BigIntegerField(default=0)