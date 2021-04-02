from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class ClassSchedule(models.Model):
    #student=models.CharField(max_length=50)
    #the map hopefully here
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    #building=models.CharField(max_length=500, default='Building')    
    def __str__(self):
        return self.mySchedule

class Class(models.Model):
    schedule = models.ForeignKey(ClassSchedule, on_delete=models.CASCADE)
    className=models.CharField(max_length=500, default='New Class')
    building=models.CharField(max_length=500, default='Building') 

    def __str__(self):
        return self.building