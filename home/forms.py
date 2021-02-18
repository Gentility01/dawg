from django import forms
from django.contrib.auth.models  import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
#import the profile models so as to enable updating

# creating a class to that will inherit from  the user creation form

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    last_name = forms.CharField()
    first_name = forms.CharField()
   
    class Meta:
        model = User
        fields = [
           'first_name',
           'last_name',
           'username',
           'email',
           'password1',
           'password2',
           
       ]
       
# NOTE: this form here is going to be used to repace the UserCreationForm form already existing in the views.py
# to do that import this form.py and this class and replace the UserCreationForm with the class name UserRegistrationForm

# bellow we are creating a modelsform to enable users update there profiles

class UserUpdateForm(forms.ModelForm):
   
    class Meta:
        model = User
        fields = [
           'first_name',
           'last_name',
           'username',
           'email',      
       ]
        
class profileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields =[
            'bio',
            'location',
        ]