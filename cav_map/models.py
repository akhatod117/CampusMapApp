from django.db import models
from django.contrib.auth.models import User
from django.http import request


class ForumPost(models.Model):
    #Title field - Limited to 100 characters
    title_field = models.CharField(max_length=100)

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    pub_date = models.DateTimeField('date published')
    #Text field - stores the text for the deep thought
    post = models.TextField(default="Post something...")

    def __str__(self):
        return self.title_field