from django.db import models
from datetime import datetime



types = [('employee','employee'),('visitor','visitor')]
class Profile(models.Model):
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    date = models.DateField()
    year = models.DateField()
    classinfo = models.IntegerField()
    sectioninfo = models.CharField(max_length=1)
    email = models.EmailField()
    present = models.BooleanField(default=False)
    image = models.ImageField()
    updated = models.DateTimeField(auto_now =True)
    def __str__(self):
        return self.first_name +' '+self.last_name


class LastFace(models.Model):
    last_face = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.last_face

