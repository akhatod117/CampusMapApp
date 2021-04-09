from django.shortcuts import render, redirect

from .models import Class, ClassSchedule, Student
from .forms import ClassForm

def classInfo(request):

    #if request.method == 'POST':
        class_form = ClassForm(request.POST)
        
        if class_form.is_valid():
            
            new_class = class_form.save()
            print(class_form)
            print(new_class)
            #new_class.student = request.user        #set student to user logged in
            #new_class.save()
            #class_form.save()
            return redirect('routemaker/multiPath')
    #else:
     #   class_form = ClassForm()
    
        context = {
            
        }
        return render(request, 'cav_map/coordinateInputs.html', {'form' : class_form})

#def scheduleInfo(request):

    #schedule_form = 
