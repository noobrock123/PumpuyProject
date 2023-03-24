from ..models import Video
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
#import modules.processing as p
from . import scheduler

class video_manager:
    
    def upload(request):
        if request.method != 'POST':
            raise PermissionDenied
        
        post_data = request.POST
        schedule = scheduler.scheduler()
        result = scheduler.create_job()
        if result:
            print("err")
        Video.objects.create(
            video_name = post_data.get('file_name'),
            video_file = request.FILE.get('file'),
            uploader = request.user
        )
        return
    
    def download(request):
        if request.method != 'POST':
            raise PermissionDenied
        return
    
    def check_status():

        return
    
    def update_modified():

        return