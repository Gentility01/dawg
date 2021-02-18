from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages 
# import the forms from forms.py
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserUpdateForm, profileUpdateForm
# this decorator is responsible for restricting access to the profile page unless you are logged in.


@login_required
def profile(request):  
    # pass the update forms into a variable
    # to populate this forms with the initial values pass the instance as an argument
    # attatch the post method for security purposes
    if request.method == 'POST': 
        userupdateform = UserUpdateForm(request.POST, instance = request.user)
        profileupdateform = profileUpdateForm(request.POST, request.FILES, instance = request.user.profile)
    else:
        userupdateform = UserUpdateForm(instance = request.user)
        profileupdateform = profileUpdateForm( instance = request.user.profile)
    
    # saving the forms
    if userupdateform.is_valid() and profileupdateform.is_valid():
        userupdateform.save()
        profileupdateform.save()
        messages.success(request, f'Account updated succedfully')
        return redirect('login')  
    #create a context for the forms and pass the contex to the profile page
    
    context = {
        'userupdateform':  userupdateform,
        'profileupdateform': profileupdateform
    }
    
    # this page is to be shown only when user is succesfully logged in
    return render(request, 'profile.html', context ) 