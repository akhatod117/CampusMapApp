from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User


def social_view(request):
    my_context = {
        "users": User.objects.all(),
        "test": "woah no way"
    }
    return render(request, "cav_map/forum.html", my_context)
