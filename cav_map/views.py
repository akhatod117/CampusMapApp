from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.views import generic
from .models import ForumPost, ForumPostForm
from django.http import HttpResponseRedirect
from datetime import datetime
from django.utils import timezone

def forum_post_create_view(request):
    if request.method == 'POST':
        form = ForumPostForm(request.POST)
        if form.is_valid():
            f = ForumPost()
            eastern = timezone('US/Eastern')
            f.title_field = form.cleaned_data['title_field']
            f.author = request.user
            f.pub_date = datetime.now(eastern)
            f.post = form.cleaned_data['post']
            f.save()
            return HttpResponseRedirect('/forum/')
    else:
        form = ForumPostForm()
        context = {'form': form}
    return render(request, "cav_map/createPost.html", context)

class forumPostView(generic.ListView):
    context_object_name = 'ps'
    template_name = 'cav_map/forum.html'
    def get_queryset(self):
        return ForumPost.objects.all().order_by('-pub_date')