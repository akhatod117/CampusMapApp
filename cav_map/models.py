from django.db import models

class ClassSchedule(models.Model):
    mySchedule=models.CharField(max_length=500, default='Schedule')
    #building=models.CharField(max_length=500, default='Building')    
    def __str__(self):
        return self.mySchedule

class Class(models.Model):
    schedule = models.ForeignKey(ClassSchedule, on_delete=models.CASCADE)
    className=models.CharField(max_length=500, default='New Class')
    building=models.CharField(max_length=500, default='Building') 

    def __str__(self):
        return self.building
