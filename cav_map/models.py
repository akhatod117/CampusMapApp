from django.db import models

class ClassSchedule(models.Model):
    myClass=models.CharField(max_length=500, default='New Class')
    building=models.CharField(max_length=500, default='Building')    
    def __str__(self):
        return self.building
