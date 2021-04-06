from django.shortcuts import render

from .models import Class, ClassSchedule, Student
from .forms import ClassForm

def classInfo(request):
    class_form = ClassForm(request.POST)

    if class_form.is_valid():
        new_class = ClassForm.save()
    context = {
        
    }
    return render(request, 'cav_map/multiPath.html', {'form' : class_form})

#def scheduleInfo(request):

    #schedule_form = 
