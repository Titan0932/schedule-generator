from django import forms
from django.db import models
from main_app.models import modelMainForm,modelSubjects

from main_app.models import *


""" class mainForm(forms.Form):
    
    sun=forms.BooleanField(label='Sunday',required=False, initial=True)
    mun=forms.BooleanField(label='Monday',required=False)
    tues=forms.BooleanField(label='Tuesday',required=False)
    wed=forms.BooleanField(label='Wednesday',required=False)
    thu=forms.BooleanField(label='Thursday',required=False)     
    fri=forms.BooleanField(label='Friday',required=False)
    sat=forms.BooleanField(label='Saturday',required=False)
    numofSubs=forms.CharField(label='Number of Subjects',max_length=150)
    startTime=forms.TimeField(label='School Starts at?')
    endTime=forms.TimeField(label='School Ends at?') """

    
""" def clean(self):
        super().clean()
        sun=self.cleaned_data.get('sun')
        mon=self.cleaned_data.get('mon')
        tue=self.cleaned_data.get('tue')
        wed=self.cleaned_data.get('wed')
        thu=self.cleaned_data.get('thu')
        fri=self.cleaned_data.get('fri')
        sat=self.cleaned_data.get('sat')
        if not sun and not mon and  not wed and not thu and not fri and not sat and not tue:
            raise forms.ValidationError('Study ONE day?!!',code='Invalid Entry')
        if int(self.cleaned_data['numofSubs'])<1:
            raise forms.ValidationError('Study atleast ONE Subject?!')
        elif int(self.cleaned_data['numofSubs'])>10:
            raise forms.ValidationError('Too many subjects!!:((') """

class mainForm(forms.ModelForm):
    class Meta:
        model=modelMainForm
        fields='__all__'
        """ 'sun',
                    'mon',
                    'tues',
                    'wed',
                    'thu',
                    'fri',
                    'sat',
                    'numofSubs',
                    'startTime',
                    'endTime'] """ 
    def get_id(self):
        return 


    def clean(self):
        super().clean()
        sun=self.cleaned_data.get('sun')
        mon=self.cleaned_data.get('mon')
        tue=self.cleaned_data.get('tues')
        wed=self.cleaned_data.get('wed')
        thu=self.cleaned_data.get('thu')
        fri=self.cleaned_data.get('fri')
        sat=self.cleaned_data.get('sat')
        if not sun and not mon and  not wed and not thu and not fri and not sat and not tue:  #--------------------FIX THIS ERRORR---------------------
            raise models.ValidationError('Study ONE day?!!',code='Invalid Entry')
        if int(self.cleaned_data['numofSubs'])<1:
            raise models.ValidationError('Study atleast ONE Subject?!')
        elif int(self.cleaned_data['numofSubs'])>10:
            raise models.ValidationError('Too many subjects!!:((')


class SubForm(forms.Form):

     def __init__(self, num=None , *args, **kwargs):
        super(SubForm, self).__init__(*args, **kwargs)
        if num:
            for i in range(0,num):
                self.fields[f"Subject {i+1}"] = forms.CharField(max_length=100)
                


                

    
    
    