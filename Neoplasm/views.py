from django.shortcuts import render
from .models import *

# Create your views here.
def homepage(request):
    return render(request, 'home.html')


def types(request):
    types = Cancer.objects.all()
    return render(request,'types.html',{'types':types})