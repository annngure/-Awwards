from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib import auth,messages
from .models import *

# Create your views here.



def index(request):
    image=Image.objects.all()
    context={
        "image":image
    }
    return render(request,'index.html',context)

@login_required()
def profileView(request):
    current_user = request.user

    if request.method == 'POST':
        form = UpdateProfileForm(request.POST,request.FILES, instance = current_user.profile)
        if form.is_valid():
            image =form.save(commit = False)
            image.user = current_user
            image.save()
        return redirect ('index')

    else:
        form = UpdateProfileForm()
    context={
        "form":form
    }
    return render(request, 'profile.html',context)

@login_required()
def project(request):
    

    return render(request, 'project.html')

def review(request):
  
    return render(request,'review.html')

def list(request):
    

    return render(request, 'project.html')    

def registerView(request):
    if request.method=="POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Registration sucessful.")
            return redirect('login')   
    else:
        messages.error(request,"Invalid Information")
        form = NewUserForm()
    context={
        "form":form}
    return render(request,'registration/register.html',context)

def loginPage(request):
    if request.user.is_authenticated():
        return redirect('index')

    if request.method == "POST":
        username=request.POST.get("username")
        password = request.POST.get("password")
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
                auth.login(request,user)
                messages.info(request,"You are now logged in.")
                return redirect('index')
            
        else:
            messages.error(request,"Invalid username or password.")

    return render(request,'registration/login.html')

def logout(request):
    auth.logout(request)
    return redirect('login')