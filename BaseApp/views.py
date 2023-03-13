from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse, HttpResponseRedirect
from BaseApp.models import Intersection

# Create your views here.
def index(request):
    intersection = Intersection.objects.all().order_by('last_update')
    return render(request, 'main.html', {'intersections': intersection})

def login_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('BaseApp:home'))

    if request.method == "POST":
        print(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('BaseApp:home'))
        return HttpResponseRedirect(reverse('BaseApp:login'))
    else:
        return render(request, 'login.html')
    
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('BaseApp:home'))

def intersection(request, name: str):
    if request.user.is_authenticated:
        intersection = Intersection.objects.get(name=name)
        return render(request, 'intersection.html', {
            'intersection' : intersection,
        })
    else:
        return render(request, 'login.html')

def edit(request, intersection_id):
    return render(request, 'edit.html')

def profile_view(request):
    return render(request, 'profile.html')