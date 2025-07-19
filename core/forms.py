from django import forms
from .models import *

class DateInput(forms.DateInput):
    input_type = 'date'
class TimeInput(forms.TimeInput):
    input_type = 'time'
class ProfileForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'date': DateInput(),
            'year': DateInput(),
        }
       
        exclude = ['present','updated']

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['date'].widget.attrs['class'] = 'form-control'
        self.fields['year'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['sectioninfo'].widget.attrs['class'] = 'form-control'
        self.fields['classinfo'].widget.attrs['class'] = 'form-control'

       