from django.db import models

# moved PostRating above Post so it's defined before the reference to it in Post's ratings field definition
class PostRating(models.Model):
    likes = models.BigIntegerField(default=0)
    dislikes = models.BigIntegerField(default=0)
    
class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=1000)
    ratings = models.OneToOneField(PostRating, on_delete=models.CASCADE, null=True) 
    # cascade means delete the post's ratings when the post is deleted
    # OneToOneField will throw error if you try to assign the same ratings id to a second post id

    def __str__(self) -> str:
        return self.title
    