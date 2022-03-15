from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

#Create the forms

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username","email","password1","password2")
        
    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class LoginForm(forms.Form):
    username =forms.CharField(max_length=50)
    password =forms.CharField(widget=forms.PasswordInput)


class UpdateProfile(forms.ModelForm):
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))
    class Meta:
        model = Profile
        fields = ['first_name','last_name','profile_image','bio','username']


class UpdateUserForm(forms.ModelForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username','email']

class CommentForm(forms.ModelForm):
    comment = forms.CharField(widget=forms.Textarea, max_length=1000)
    
    class Meta:
        model = Comment
        fields = ['comment']



       
