from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'main.html') 

def login(request):
    return render(request, 'login.html')

def loging_in(request):
    if (request.method == 'GET'):
        raise PermissionDenied 
    else:
        return redirect(reverse('home'))


def test(request):
    return HttpResponse('BaseApp:home')
