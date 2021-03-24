from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.views.generic.edit import CreateView
from django.views.decorators.http import require_POST
from django.views.generic import TemplateView
from django.template import loader

from .models import ClassSchedule
from .forms import ClassForm

class ClassView(TemplateView):
    template_name='cavmap/classSchedule.html'
    
    def get(self, request):
        form=ClassForm()
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form=ClassForm(request.POST)
        if form.is_valid():
            form.save()
            form=ClassForm()
        args={'form':form}
        return HttpResponseRedirect(self.request.path_info)
