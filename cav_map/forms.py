from django import forms
from .models import Class, Student,  ClassSchedule

class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = ['schedule', 'className', 'building', 'x', 'y']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email']

class ScheduleForm(forms.ModelForm):
    class Meta:
        model = ClassSchedule
        fields = ['student', 'date_posted']