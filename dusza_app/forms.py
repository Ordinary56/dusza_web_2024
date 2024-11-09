from django import forms
class userForm(forms.Form):
    '''
    This form is responsible for handling user login
    '''
    username = forms.CharField(max_length=255,
                               label="Felhasználónév",
                               widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Írd be a felhasználóneved'}))
    password = forms.CharField(max_length=255,
                               label="Jelszó",
                               widget=forms.PasswordInput(attrs= {'class' : 'form-control'}))

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

class SchoolForm(forms.Form):
    '''
    This form is responsible for editing an existing school's data  
    '''
    pass
class CategoryForm(forms.Form):
    category = forms.CharField(max_length=255)

class ProgLangForm(forms.Form):
    programming_language = forms.CharField(max_length=30)