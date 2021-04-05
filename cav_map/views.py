from django.shortcuts import render

from .models import Class, ClassSchedule, Student

dummy = [
    {
        'className'
    }
]
def blog(request):
    return render(request, 'cav_map/data.html', ClassSchedule)
