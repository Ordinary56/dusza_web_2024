from dataclasses import fields
from django import forms
from dusza_app.models import Category, ProgLangs, School

class userForm(forms.Form):
    '''
    This form is responsible for handling user login
    '''
    username = forms.CharField(max_length=255,
                               label="Felhasználónév",
                               widget=forms.TextInput(attrs={'class' : 'form-control  input100'}))
    password = forms.CharField(max_length=255,
                               label="Jelszó",
                               widget=forms.PasswordInput(attrs= {'class' : 'form-control input100'}))

class TeamForm(forms.Form):
    '''
    This form is responsible for registering a team
    Note: Might get reused for editing an existing team too
    '''
    username = forms.CharField(max_length=255)
    password = forms.CharField(max_length=255)
    team_name = forms.CharField(max_length=255)
    school_name= forms.CharField(max_length=255)
    member_1_name = forms.CharField(max_length=255)
    member_1_term = forms.CharField(max_length=10)
    member_2_name = forms.CharField(max_length=255)
    member_2_term = forms.CharField(max_length=10)
    member_3_name = forms.CharField(max_length=255)
    member_3_term = forms.CharField(max_length=10)
    mentor = forms.CharField(max_length=255)
    category = forms.CharField(max_length=255)
    programming_language = forms.CharField(max_length=30)

class SchoolForm(forms.ModelForm):
    '''
    This form is responsible for editing an existing school's data  
    '''
    class Meta:
        model = School
        fields = ['school_name', 'school_address', 'principal_name', 'principal_email']
        labels = {
            'schoolName' : "Iskola neve",
            'schoolAdress' : "Iskola címe",
            'principalName' : "Igazgató neve",
            'principalEmail' : "Igazgató email címe"
        }
        widgets = {
            'schoolName' : forms.TextInput(attrs={'class' : 'form-control'}),
            'schoolAddress' : forms.TextInput(attrs={'class' : 'form-control'}),
            'principalName' : forms.TextInput(attrs={'class' : 'form-control'}),
            'principalEmail' : forms.EmailInput(attrs={'class' : 'form-control'})
        }
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