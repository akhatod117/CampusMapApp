from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from .forms import ForumPostForm
from django.views.generic import ListView
from .models import ForumPost
from django.http import HttpResponseRedirect
from datetime import datetime

def forum_post_create_view(request):
    form = ForumPostForm()
    if request.method == 'POST':
        form = ForumPostForm(request.POST)
        if form.is_valid():
            f = ForumPost()
            f.title_field = form.cleaned_data['title_field']
            f.author = request.user
            f.pub_date = datetime.now()
            f.post = form.cleaned_data['post']
            f.save()
            return HttpResponseRedirect('/forum/')
    else:
        context = {'form': form}
    return render(request, "cav_map/createPost.html", context)

def social_view(request):
    my_context = {
        "users": User.objects.all(),
        "test": "woah no way"
    }
    return render(request, "cav_map/forum.html", my_context)

class forumPostView(ListView):
    context_object_name = 'ps'
    template_name = 'cav_map/forum.html'
    def get_queryset(self):
        return ForumPost.objects.all().order_by('-pub_date')