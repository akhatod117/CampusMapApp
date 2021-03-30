from django import forms
from .models import Class, ClassSchedule

class ClassForm(forms.ModelForm):
    className=forms.CharField()
    building=forms.CharField()

    class Meta:
        model=Class
        fields=('className','building')
        #fields=('__all__')
