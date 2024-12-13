from django.shortcuts import render,redirect
from .models import *
from .form import *
from django.contrib.auth import authenticate, login,logout
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
            return redirect('home')
        else:
            # messages.success(request("Whoops, There was a problem, Please try again"))
            return redirect('register')
    else:
        return render(request, 'register.html', {'form': form})