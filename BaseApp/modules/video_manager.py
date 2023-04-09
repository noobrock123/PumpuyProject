from ..models import Video, Intersection
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
#import modules.processing as p
from . import scheduler

class video_manager:
    
    def upload(self, request, name, video_file, video_name):
        if request.method != 'POST':
            raise PermissionDenied
        
        data = request.POST

        path = f"intersectionData/{video_file}"
        schedule = scheduler.Celery()
        Video.objects.create(
            video_name = video_name,
            length = 300,
            uploader = request.user,
            auth_level = 4,
            intersection = Intersection.objects.get(name=name) 
        )
        result = schedule.create_job.delay(path, video_file)
        if result:
            print("err")
    
    def download(request):
        if request.method != 'POST':
            raise PermissionDenied
        return
    
    def check_status():

        return
    
    def update_modified():

        return