from __future__ import absolute_import, unicode_literals
from . import processing as proc
from celery import shared_task
from .process_chooser import process_chooser
from ..models import Video, Hitbox
from django.core.files import File

# import eventlet
import time

# eventlet.monkey_patch(os=True, builtins=True, subprocess=True)

class scheduler:

    def create_job(data, path, hitbox_id, video = None) -> int:
        pass
    
    def get_job_status():
        pass

class Celery(scheduler):

    @shared_task(bind=True)
    def create_job(self, video_id, video_name, hitbox_id, video_path = None) -> int:
        print("Hello")
        # p = proc.processing()
        # try:
        #     p.process(path, video)
        # except proc.EmptyFileError:
        #     return 1
        video_file = Video.objects.get(id=video_id, video_name=video_name)
        if hitbox_id is not None:
            hitbox = Hitbox.objects.get(hitbox_id=hitbox_id)
            hitbox_name = hitbox.hitbox_name
            hitbox_id = hitbox.video.id
        else:
            hitbox_name = None
            hitbox_id = None
        video_file.status = 1
        video_file.save()

        p = process_chooser()
        result = p.yolo_v7(video_id, video_path, hitbox_name, hitbox_id)
        if result == "finish":
            videofile = Video.objects.get(id=video_id, video_name=video_name)
            videofile.status = 0
            videofile.save()
    
class save_to_database:
    pass