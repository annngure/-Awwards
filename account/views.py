from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib import auth,messages
from .models import *
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from rest_framework import viewsets
from .permission import IsAdminOrReadOnly

# Create your views here.



def index(request):
   
    return render(request,'index.html')

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
    project_list = Project.objects.order_by('title')
    context = {'project':project}

    return render(request, 'project.html',context)

def review(request):
    
    return render(request,'review.html')
 
def list(request):
    latest_review_list = Review.objects.all()
    context = {'list':list}
    return render(request,'list.html',context)

def user(request):

    return render(request,'user.html')


def view(request,id):
    try:
        project = Project.objects.get(pk = id)

    except DoesNotExist:
        raise Http404()

    current_user = request.user
    comments = Review.get_comment(Review, id)
    latest_review_list=Review.objects.all()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            design_rating = form.cleaned_data['design']
            content_rating = form.cleaned_data['content']
            usability_rating = form.cleaned_data['usability']
            comment = form.cleaned_data['comment']
            review = Review()
            review.project = project
            review.user = current_user
            review.comment = comment
            review.design= design
            review.content= content
            review.usability = usability
            review.save()

    else:
        form = ReviewForm()
        context={
           "project": project,
            'form':form,
            'comment':comment,
            'review':review
       }

    return render(request, 'image.html', context)

    return render(request,'view.html')

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

# serializer views
   
class ProfileViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAdminOrReadOnly,)
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer



class ProjectViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAdminOrReadOnly,)
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

# search for projects
def search_project(request):
    if request.method == 'GET':
        title = request.GET.get("title")
        # posts = Post.objects.filter(title__icontains=title).all()

    return render(request, 'search.html')

def user_list(request):
    user_list = User.objects.all()
    context = {'user_list': user_list}
    return render(request, 'user_list.html', context)


def new_project(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = current_user
            project.save()
        return redirect('index')

    else:
        form = NewProjectForm()
    context={
           "form": form 
           }
    return render(request, 'new_project.html',context )
