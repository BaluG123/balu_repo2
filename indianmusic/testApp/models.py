from django.db import models
from django.utils import timezone
# Create your models here.
class Music(models.Model):
    artistimage=models.ImageField(null=True,blank=True,upload_to='images/')
    artistname=models.CharField(max_length=128)
    song=models.FileField(null=True,blank=True,upload_to='images/')
    songname=models.CharField(max_length=200)
    duration=models.FloatField()
    uploaded=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=['uploaded']

    def __str__(self):
        return self.songname

class Video(models.Model):
    video=models.FileField(null=True,blank=True,upload_to='videos/')
    image=models.ImageField(null=True,blank=True,upload_to='images/')
    title=models.CharField(max_length=200)
    uploaded=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=['-uploaded']

    def __str__(self):
        return self.title
