from django.db import models

# Create your models here.
class Album(models.Model):
    name = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name
    
class Track(models.Model):
    album = models.ForeignKey(Album, related_name='tracks', on_delete=models.CASCADE)
    order = models.IntegerField()
    title = models.CharField(max_length=100)
    duration = models.IntegerField()

    class Meta:
        ordering = ['order']

    def __str__(self) -> str:
        return '%d: %s' % (self.order, self.title)