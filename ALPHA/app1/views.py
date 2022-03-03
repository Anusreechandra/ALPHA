from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def alpha(request):
    return render(request,'ALPHA find your job.html')

def login(request):
    return render(request, 'login.html')

def su(request):
    return render(request, 'su.html')