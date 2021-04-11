from django import forms
from .models import Class, Student,  ClassSchedule
from django.forms import modelformset_factory

class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = ['className', 'building',]

ClassFormset = modelformset_factory(
            Class,
            fields=('className', 'building',),
            extra = 1,
            widgets={'name': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Class Name here'})

            }
        )

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', ]

class ScheduleForm(forms.ModelForm):
    class Meta:
        model = ClassSchedule
        fields = ['student']