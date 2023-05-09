from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.functional import SimpleLazyObject
from BaseApp.models import Intersection, Organization, Video, Authority
from django.core.files.storage import FileSystemStorage
from .modules import video_manager
from . import views

import os

# Create your views here.
def index(request):
    return HttpResponseRedirect(reverse('BaseApp:home'))

def home_view(request):
    intersection = Intersection.objects.all().order_by('last_update')
    return render(request, 'main.html', 
        {
        'intersections': intersection,
        'username': request.user.username,
        'auth_level': get_auth_level(request.user),
        })

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

def signup_view(request):
    return render(request, 'register.html')

def intersection(request, name: str):
    if request.user.is_authenticated:
        # try:
        intersection = Intersection.objects.get(name=name)
        videos = Video.objects.filter(intersection=intersection)
        # except Intersection.DoesNotExist:
        #     return HttpResponseRedirect(reverse('BaseApp:home'))
        # print(intersection.picture)
        return render(request, 'intersection.html', {
            'auth_level': get_auth_level(request.user),
            'intersection' : intersection,
            'videos': videos,
        })
    else:
        return render(request, 'login.html')

def edit(request, name):
    return render(request, 'edit.html')

def summary(request) :
    return render(request, 'summary.html')

def profile_view(request, id):
    if request.user.is_authenticated:
        organization = Authority.objects.get(user=request.user).organization   # get organization //Allumilie & noobrock123 (Mar 30. 2023)
        intersection = Intersection.objects.filter(owner=organization).order_by('last_update')   # filter only intersections that in this organization //Allumilie & noobrock123 (Mar 30, 2023)
        return render(request, 'profile.html', {
            'user' : request.user,
            'organization' : organization.name,
            'intersections' : intersection,
        })
    else:
        return render(request, 'login.html')
    
def add_intersection(request):
    if request.method == 'POST':
        data = request.POST
        print(request.FILES.get('picture').name)
        Intersection.objects.create(
            name=data['name'],
            location=data['address'],
            latitude=data['latitude'],
            longtitude=data['longtitude'],
            intersec_type=4,
            status=0,
            owner=Authority.objects.get(user=request.user).organization,
            picture=request.FILES.get('picture'),
        )
        return redirect('/home')
    return render(request, 'insert_intersection.html')

def upload_video(request, name):
    if request.user.is_authenticated:
        if request.method == 'POST':
            file = request.FILES.get("video_file")
            file_name = file.name.split(".")[0]

            video = Video.objects.create(
                video_name=file_name,
                uploader=request.user,
                length=1,
                auth_level=3,
                intersection=Intersection.objects.get(name=name),
                video_file=file
            )
            request.session['video'] = video.id
            return redirect("BaseApp:process", name = name)
        #return HttpResponse('This page is work in progess') # just a placeholder for frontend to make page for it and if you make the page just change HttpResonse to render //Allumlie
        return render(request, "upload.html")
    else:
        return render(request, 'login.html')
    
def process_video(request, name):
    if request.method == "POST":
        if "video" in request.session:
            video = Video.objects.get(id=request.session['video'])
            del request.session['video']
        manager = video_manager.video_manager()
        manager.upload(request, name,)
    if request.user.is_authenticated == False:
        return redirect("BaseApp:login")
    if "video" not in request.session:
        return redirect("BaseApp:home")
    video = Video.objects.get(id=request.session['video'])
    return render(request, "edit.html", {"video": request.session['video'], "name": video.video_name})
        
    
    
def search_intersection(request):
    query = request.POST.get("query")    
    option = request.POST.get("options")
    try:
        if option == 'owner':
            filter = option + '__name' + '__icontains'  # owner is forienge key so its need to do special filter
        else:
            filter = option + '__icontains'
    except (TypeError):     # catch error when user search directly in url //Allumilie
        filter = 'name__icontains'

    try:
        intersection = Intersection.objects.filter(**{filter : query})
    except (ValueError):    # catch error when user search directly in url // Allumilie
        intersection = Intersection.objects.filter(**{filter : ''})
    return render(request, 'main.html',{
        'intersections': intersection,
        'username': request.user.username,
    })

def search_video(request, name):
    if request.user.is_authenticated:
        query = request.POST.get("query")
        option = request.POST.get("options")
        try:
            filter = option + '__icontains'
        except (TypeError): # catch error when user search directly in url // Allumilie
            filter = 'video_name__icontains'
        
        intersection = Intersection.objects.get(name=name)  # Get video in that intersection //Allumilie
        try:
            videos = intersection.videos.filter(**{filter : query})
        except (ValueError):    # catch error when user search directly in url //Allumilie
            videos = intersection.videos.filter(**{filter : ''})
        print(intersection.videos)
        return render(request, 'intersection.html',{
            'videos': videos,
            'intersection': intersection,
        })
    else:
        return render(request, 'login.html')
    
def delete_video(request, name):
    if request.user.is_authenticated:
        if request.method == 'POST':
            query = request.POST.get("query")

            fs = FileSystemStorage

            video = Video.objects.get(id=query)
            video.delete()
            #os.chdir('..')

            print('delete video successfully')
            
        return redirect("BaseApp:intersection", name=name)
    else:
        return render(request, 'login.html')

#Below this line, the code MUST not be used in urls.py
def get_auth_level(user: SimpleLazyObject) -> int: 
    try:
        auth_level: int = Authority.objects.get(user=user).auth_level
    except:
        auth_level = 7
    finally:
        return auth_level