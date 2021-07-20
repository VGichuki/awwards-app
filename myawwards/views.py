from myawwards.models import Project
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from .models import Project,Profile
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def home(request):
    return render(request, 'home.html')

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
        return render(request,'register.html', context)

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


