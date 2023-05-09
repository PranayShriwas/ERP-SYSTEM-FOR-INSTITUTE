from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'index.html')


def courses(request):
    return render(request, 'courses.html')


def dashboard(request):
    return render(request, 'dashboard.html')


def signup(request):
    return render(request, 'signup.html')


def viewstudents(request):
    return render(request, 'viewstudents.html')
