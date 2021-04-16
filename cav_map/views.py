from django.shortcuts import render, redirect

from .models import Route


""" def createSchedule(request):
    schedule_form = ScheduleForm() """
'''
def create_class_model_form(request):
    template_name = 'cav_map/coordinateInputs.html'
    #heading_message = 'Model Formset Demo'
    if request.method == 'GET':
        # we don't want to display the already saved model instances
        formset = ClassFormset(queryset=Class.objects.none())
    elif request.method == 'POST':
        formset = ClassFormset(request.POST)
        if formset.is_valid():
            for form in formset:
                # only save if name is present
                if form.cleaned_data.get('className'):
                    form.save()
            return redirect('1/multiPath')
    return render(request, template_name, {
        'formset': formset,
    })
'''

'''def classInfo(request):
        i = 0
    #if request.method == 'POST':
        class_form = ClassForm(request.POST)
        classes_form = [6]
        
        if class_form.is_valid():
            
            new_class = class_form.save()
            print(class_form)
            print(new_class.className, new_class.building)
            #classes_form[i] = new_class
            i + 1

            #new_class.student = request.user        #set student to user logged in
            #new_class.save()
            #class_form.save()
            return redirect('1/multiPath')
    #else:
     #   class_form = ClassForm()
    
        context = {
            
        }
        return render(request, 'cav_map/coordinateInputs.html', {'form' : class_form})

#def scheduleInfo(request):

    #schedule_form = 
'''
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.views import generic
from .models import ForumPost, ForumPostForm
from django.http import HttpResponseRedirect
import datetime
from pytz import timezone
import json


def forum_post_create_view(request):
    if request.method == 'POST':
        form = ForumPostForm(request.POST)
        if form.is_valid():
            f = ForumPost()
            f.title_field = form.cleaned_data['title_field']
            f.author = request.user
            f.pub_date = datetime.datetime.utcnow()-datetime.timedelta(hours=4)
            f.post = form.cleaned_data['post']
            f.save()
            return HttpResponseRedirect('/forum/')
    else:
        form = ForumPostForm()
        context = {'form': form}
    return render(request, "cav_map/createPost.html", context)

def create_class(request):
    template = 'cav_map/multiPath.html'
    if request.method  == 'POST':
        request_getdata = request.POST.get("urls", "None")
        lst = json.loads(request_getdata)
        entry = Route.objects.filter(user=request.user).first()
        if entry:
            r = Route.objects.get(user=request.user)
        else:
            r = Route()
            r.user = request.user
        r.urls = lst
            #new_class = Class.objects.get()
        r.save()
    return render(request, template)
def create_class2(request):
    entry = Route.objects.filter(user=request.user).first()
    if entry:
        context = {'urls': json.dumps(Route.objects.get(user=request.user).urls)}
    else:
        url = '/routemaker/'
        resp_body = '<script>alert("No Saved Route Found!");\
             window.location="%s"</script>' % url
        return HttpResponse(resp_body)
    template = 'cav_map/savedMP.html'
    return render(request, template, context)
class forumPostView(generic.ListView):
    context_object_name = 'ps'
    template_name = 'cav_map/forum.html'
    def get_queryset(self):
        return ForumPost.objects.all().order_by('-pub_date')
