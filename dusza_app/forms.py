from typing import Any, Mapping
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.renderers import BaseRenderer
from django.forms.utils import ErrorList
from dusza_app.models import *

class UserForm(forms.ModelForm):
    '''
    This form is responsible for handling user login
    '''
    class Meta:
        model = User
        fields = ['username', 'password']
        labels = {
            'username' : "Felhasználónév",
            'password' : "Jelszó"
        }
        widgets = {
            'username' : forms.TextInput(attrs={'class': 'form-control'}),
            'password' : forms.PasswordInput(attrs={'class': 'form-control'})
        }
    

class TeamForm(forms.Form):
    '''
    This form is responsible for registering a team
    Note: Might get reused for editing an existing team too
    '''
    child_form = UserForm()
    
    def __init__(self,categories,languages,*args,**kwargs) -> None:
        super().__init__(*args,kwargs)
        self.fields = {  
            'team_name' : forms.CharField(label="Csapat neve"), 
            'school_name': forms.CharField(label="Iskola neve"), 
            'team_1_name': forms.CharField(label="Első csapattag neve"),
            'team_1_term': forms.CharField(label="Első csapattag  évfolyama"), 
            'team_2_name': forms.CharField(label="Második csapattag neve"),
            'team_2_term': forms.CharField(label="Második csapattag évfolyama"),
            'team_3_name': forms.CharField(label="Harmadik csapattag"),
            'team_3_term': forms.CharField(label="Harmadik csapattag évfolyama"),
            'extra_member_name': forms.CharField(required=False,label="Póttag neve"),
            'extra_member_term': forms.CharField(required=False,label="Póttag neve"),
            'mentor': forms.CharField(label="Felkészítő tanár neve"),
            'category': forms.ChoiceField(choices=categories, label="Választott kategória"),
            'language': forms.ChoiceField(choices=languages, label="Választott nyelv")
            } 

    def save(self, commit: bool = ...) -> Any:
        return super().save(commit)
    

class SchoolForm(forms.ModelForm):
    '''
    This form is responsible for editing an existing school's data  
    '''
    child_form = UserForm()
    class Meta:
        model = School
        fields = ['school_name', 'school_address', 'principal_name', 'principal_email']
        labels = {
            'school_name' : "Iskola neve",
            'school_address' : "Iskola címe",
            'principal_name' : "Igazgató neve",
            'principal_email' : "Igazgató email címe"
        }
        widgets = {
            'school_name' : forms.TextInput(attrs={'class' : 'form-control'}),
            'school_address' : forms.TextInput(attrs={'class' : 'form-control'}),
            'principal_name' : forms.TextInput(attrs={'class' : 'form-control'}),
            'principal_email' : forms.EmailInput(attrs={'class' : 'form-control'})
        }
    def save(self, commit: bool = ...) -> Any:
        parent = super().save(commit=False)
        if commit:
            parent.save()
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category']
        labels = {
            'category' : "Kategória"
        }
        widgets = {
            'category' : forms.TextInput(attrs={'class' : 'form-control'})
        }

class ProgLangForm(forms.ModelForm):
    class Meta:
        model = ProgLangs
        fields = ['language']
        labels = {
            'language' : 'Programozási nyelv'
        },
        widgets = {
            'language' : forms.TextInput(attrs={'class' : 'form-control'})
        }