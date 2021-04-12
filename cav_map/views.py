from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from .forms import ForumPostForm



def forum_post_create_view(request):
    form = ForumPostForm()
    if request.method == 'POST':
        form = ForumPostForm(request.POST)
        if form.is_valid():
            form.save()
            form = ForumPostForm()

    context = {'form': form}
    return render(request, "cav_map/createPost.html", context)

def social_view(request):
    my_context = {
        "users": User.objects.all(),
        "test": "woah no way"
    }
    return render(request, "cav_map/forum.html", my_context)
