from __future__ import absolute_import, unicode_literals
from . import processing as proc
from celery import shared_task

class scheduler:

    def create_job(data, path, video = None) -> int:
        pass
    
    def get_job_status():
        pass

class Celery(scheduler):

    @shared_task
    def create_job(data, path, video = None) -> int:
        p = proc.processing()
        try:
            p.process(path, video)
        except proc.EmptyFileError:
            return 1
    
class save_to_database:
    pass