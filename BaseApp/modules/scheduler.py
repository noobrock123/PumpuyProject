from . import processing as proc

class scheduler:

    def create_job() -> int:
        pass
    
    def get_job_status():
        pass

class Celery(scheduler):

    def create_job() -> int:
        p = proc.processing()
        try:
            p.process()
        except proc.EmptyFileError:
            return 1
    