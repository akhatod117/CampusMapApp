from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
#from django.contrib

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=52, default='Mary')
    #email = models.CharField(max_length=122, default='nope@null.com')

    def __str__(self):
        return self.name

class ClassSchedule(models.Model):
    #student=models.CharField(max_length=50)
    #the map hopefully here
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    #date_posted = models.DateTimeField(default=timezone.now)
    numClasses = models.IntegerField( default=0)
    #building=models.CharField(max_length=500, default='Building')    
    def __str__(self):
        return numClasses

class Class(models.Model):
    #schedule = models.ForeignKey(ClassSchedule, on_delete=models.CASCADE)
    className = models.CharField(max_length=122, default='New Class')
    building = models.CharField(max_length=500, default='Building') 
    x = models.CharField(max_length= 100, default='0.0')
    y = models.CharField(max_length=100, default='0.0')

    def __str__(self):
        return self.className

from django.contrib.auth.models import User
from django.http import request
from django import forms
class ForumPostForm(forms.Form):
    title_field = forms.CharField(label='Title')
    post = forms.CharField(label='Post')

class ForumPost(models.Model):
    #Title field - Limited to 100 characters
    title_field = models.CharField(max_length=100)

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    pub_date = models.DateTimeField('date published')
    #Text field - stores the text for the deep thought
    post = models.TextField(default="Post something...")

    def __str__(self):
        return self.title_field
