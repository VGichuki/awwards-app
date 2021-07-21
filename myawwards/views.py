from django.contrib.auth.models import User
from rest_framework import serializers
from myawwards.models import Project
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm, UpdateProfileForm,UpdateUserForm, PostForm , RatingsForm
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from .models import Project,Profile, Rating
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProfileSerializer, ProjectSerializer, UserSerializer

# Create your views here.
class ProjectList(APIView):
    def get(self, request, format=None):
        all_projects = Project.objects.all()
        serializers = ProjectSerializer(all_projects, many=True)
        return Response(serializers.data)


def home(request):
    project = Project.objects.all()
    return render(request, 'home.html', {'project': project})

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form= CreateUserForm
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Welcome' + user)
                return redirect('login')
        context={'form': form}
        return redirect(request,'register.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username =request.POST.get('username')
            password =request.POST.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username OR password is incorrect')
        context={}
        return render(request, 'login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def user_profile(request):
    return render(request, 'profile.html')

def update_user_profile(request, username):
    person=get_object_or_404(User, username=username)
    if request.user == person:
        return redirect('profile',username=request.user.username)
    context={'person':person}
    return redirect(request, 'updateprofile.html', context)

@login_required(login_url='login')
def edit_user_profile(request, username):
    user = User.objects.get(username=username)
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile', user.username)
    else:
        user_form = UpdateUserForm(instance = request.user)
        profile_form = UpdateProfileForm(instance = request.user.profile)
    context={'user_form':user_form, 'profile_form': profile_form}
    return redirect(request, 'editprofile.html', context)
@login_required(login_url='login')
def project(request):
    current_user = request.user
    if request.method == 'POST':
        form = PostForm(request.POST or None, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = current_user
            project.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'new_post.html', {'form': form})

# @login_required(login_url='login')
# def ratings(request, project):
#     project = Project.objects.get(title=project)
#     ratings = Rating.objects.filter(user=request.user, project=project).first()
#     rating_status = None
#     if ratings is None:
#         rating_status = False
#     else:
#         rating_status = True
#     if request.method == 'POST':
#         form = RatingsForm(request.POST)
#         if form.is_valid():
#             rate = form.save(commit=False)
#             rate.user = request.user
#             rate.project = project
#             rate.save()
#             project_ratings = Rating.objects.filter(project=project)

#             design_ratings = [design.design for design in project_ratings]
#             design_average = sum(design_ratings)/ len(design_ratings)

#             usability_ratings = [usability.usability for usability in project_ratings]
#             usability_average = sum(usability_ratings)/ len(usability_ratings)

#             content_ratings = [content.content for content in project_ratings]
#             content_average = sum(content_ratings) / len(content_ratings)

#             score = (design_average + usability_average + content_average)
#             print(score)
#             rate.design_average = round(design_average, 2)
#             rate.usability_average = round(usability_average, 2)
#             rate.content_average = round(content_average, 2)
#             rate.score = round(score, 2)
#             rate.save()
#             return HttpResponseRedirect(request.path_info)
#     else:
#         form = RatingsForm()
#     context ={'project': project, "rating_form" : form, 'rating_status': rating_status}
#     return redirect(request, 'project.html', context)




    

# @login_required(login_url='login')
# def search(request):
#     if 'serch_term' in request.GET and request.GET['search_term']:
#         term=request.GET.get('search_term')
#         try:
#             projects=Project.search_project(term)
#             message=f'{term}'
#             title=term
#             return redirect(request,'search.html', {'message':message,'title':title, 'projects':projects})
#         except Project.DoesNotExist:
#             message=f'{term}'
#             return redirect(request,'search.html', {'message':message,'title':title})


