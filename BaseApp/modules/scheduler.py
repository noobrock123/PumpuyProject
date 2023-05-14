from __future__ import absolute_import, unicode_literals
from . import processing as proc
from celery import shared_task
from .process_chooser import process_chooser
from ..models import Video

class scheduler:

    def create_job(data, path, video = None) -> int:
        pass
    
    def get_job_status():
        pass

class Celery(scheduler):

    @shared_task(bind=True)
    def create_job(self, video_id, video_name, video_path = None) -> int:
        print("Hello")
        # p = proc.processing()
        # try:
        #     p.process(path, video)
        # except proc.EmptyFileError:
        #     return 1
        video_file = Video.objects.get(id=video_id, video_name=video_name)
        video_file.status = 1
        video_file.save()

        p = process_chooser()
        result = p.yolo_v7(video_id, video_path)
        if result == "finish":
            video_file.status = 0
            localfile = open(f'./BaseApp/intersectionData/{video_file.intersection.name}/detect/{video_id}/{video_file.video_name}')
            video_file.result_video = File(localfile)
            video_file.save()
            localfile.close()
    
class save_to_database:
    pass