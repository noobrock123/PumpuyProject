from ..models import Video, Intersection
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
# import modules.processing as p
from .process_chooser import process_chooser
from . import scheduler

class video_manager:
    
    def upload(self, request, name, video_file: Video):
        if request.method != 'POST':
            raise PermissionDenied
        
        data = request.POST
        schedule = scheduler.Celery()
        '''
        Video.objects.create(
            video_name = video_name,
            length = 300,
            uploader = request.user,
            auth_level = 4,
            intersection = Intersection.objects.get(name=name),
            video_file = video_file, # Add ref of the video file to Video obj so we can update and delete ltr // Allumilie
        )
        '''
        p = process_chooser()
        file = ""
        video_file.status = 2
        video_file.save()
        video_path = video_file.get_path()
        # result =  p.yolo_v7(video_file)
        result = schedule.create_job.delay(video_file.id, video_file.video_name, video_path)
        # print(result)
        if result:
            print("Job Received")
    
    def download(request):
        if request.method != 'POST':
            raise PermissionDenied
        return
    
    def check_status():

        return
    
    def update_modified():

        return
