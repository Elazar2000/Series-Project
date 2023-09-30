from django import forms
from . models import Series

class seriesForm(forms.ModelForm):
    class Meta:
        model=Series
        fields = ['name','disc','year','img']
