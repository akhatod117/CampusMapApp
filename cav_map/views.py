from django.shortcuts import render, redirect

from .models import Class, ClassSchedule, Student
from .forms import ClassForm, ScheduleForm, StudentForm, ClassFormset

def createSchedule(request):
    schedule_form = ScheduleForm()
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