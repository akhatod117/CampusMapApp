from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
#from django.contrib

class Student(models.Model):
    
    name = models.CharField(max_length=52, default='Mary')
    email = models.CharField(max_length=122, default='nope@null.com')

    def __str__(self):
        return self.name

class ClassSchedule(models.Model):
    #student=models.CharField(max_length=50)
    #the map hopefully here
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)
    #building=models.CharField(max_length=500, default='Building')    
    def __str__(self):
        return 

class Class(models.Model):
    schedule = models.ForeignKey(ClassSchedule, on_delete=models.CASCADE)
    className=models.CharField(max_length=122, default='New Class')
    building=models.CharField(max_length=500, default='Building') 
    x = models.CharField(max_length= 100, default='0.0')
    y = models.CharField(max_length=100, default='0.0')

    def __str__(self):
        return self.building

