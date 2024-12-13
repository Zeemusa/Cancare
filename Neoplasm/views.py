from django.shortcuts import render,redirect
from .models import *
from .form import *
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def homepage(request):
    return render(request, 'home.html')


def cancer(request):
    cancer = Cancer.objects.all()
    return render(request,'types.html',{'cancer':cancer})


def disease(request,pk):
    cancer= Cancer.objects.get(id=pk)
    return render(request,'disease.html',{'cancer':cancer})


def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            #log in user 
            user = authenticate(username = username, password = password)
            login(request,user)
            return redirect('login')
        else:
            # messages.success(request("Whoops, There was a problem, Please try again"))
            return redirect('register')
    else:
        return render(request, 'register.html', {'form': form})
    
def login_user(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password = password)
        if user is not None:
            login(request,user)
            # messages.success(request("You Have Been Loged In"))
            return redirect('types')
        else:
            # messages.success(request("There Was An Error, Please Try Again"))
            return redirect('login') 
         
    else:
        return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('homepage')