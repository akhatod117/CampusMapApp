from django import forms
from .models import Class, Student,  ClassSchedule

class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = ['className', 'building',]

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email']

class ScheduleForm(forms.ModelForm):
    class Meta:
        model = ClassSchedule
        fields = ['student']