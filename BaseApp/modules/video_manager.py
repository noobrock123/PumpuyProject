from ..models import Video
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
#import modules.processing as p
from . import scheduler

class video_manager:
    
    def upload(self, request, name, video_file):
        if request.method != 'POST':
            raise PermissionDenied
        
        data = request.POST
        path = f"intersectionData/{name}/videos/{video_file}"
        schedule = scheduler.Celery()
        result = schedule.create_job.delay(path, video_file)
        if result:
            print("err")
        #Video.objects.create(
        #    video_name = post_data.get('file_name'),
        #    video_file = request.FILE.get('file'),
        #    uploader = request.user
        #)
    
    def download(request):
        if request.method != 'POST':
            raise PermissionDenied
        return
    
    def check_status():

        return
    
    def update_modified():

        return