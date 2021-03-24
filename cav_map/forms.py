from django import forms
from .models import Thoughts

class ClassForm(forms.ModelForm):
    myClass=forms.CharField()
    building=forms.CharField()

    class Meta:
        model=ClassSchedule
        fields=('myClass','building')
