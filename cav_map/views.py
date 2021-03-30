from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic, View
from django.utils import timezone
from django.views.decorators.http import require_POST
from django.template import loader

from .models import ClassSchedule, Class
from .forms import ClassForm

class ClassView(TemplateView):
    template_name='cav_map/classSchedule.html'
    form_class = ClassForm
    model = Class
    
    def get(self, request):
        form=ClassForm()
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        print("post request")
        form=ClassForm(request.POST)

        if form.is_valid():
            
            form.save()
            form=ClassForm()
            return HttpResponseRedirect(self.request.path_info)
        args={'form':form}
        #return HttpResponseRedirect(self.request.path_info)
        return render(request, self.template_name, args)
"""

def classAdd(request):
    form = ClassForm()
    args = {'form':form}
    return render(request, 'cav_map/class.html',args)

"""