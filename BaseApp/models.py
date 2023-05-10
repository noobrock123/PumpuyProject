from django.db import models
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
import datetime

auth_select = (
    (0, 'sys_admin'),
    (1, 'ผู้ดูแลองค์กร'),
    (2, 'ผู้ดูแลแยก'),
    (3, 'ผู้ดูแลการอัพโหลด')
)
# Create your models here.
class Organization(models.Model):
    name = models.CharField(max_length=128, null=False)

    def __str__(self) -> str:
        return self.name

class Authority(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    auth_level = models.IntegerField(choices=auth_select, default=3)
    organization = models.ForeignKey(Organization, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return self.user.username

def get_video_path(instance, file):
    intersec_name = instance.intersection.name
    return f"{intersec_name}/videos/{instance.id}/{file}"

def get_loop_path(instance, file):
    file_name = instance.video.video_file.name.split(".")[0]
    return f"{instance.video.intersection.name}/{instance.video.id}{file_name}/{file}"

def get_intersection_picture_path(instance, file):
    return f"{instance.name}/{file}"

class Intersection(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    location = models.CharField(max_length=512)
    latitude = models.FloatField()
    longtitude = models.FloatField()
    intersec_type = models.IntegerField()
    status = models.IntegerField()
    owner = models.ForeignKey(Organization, on_delete=models.CASCADE, null=True, blank=True)
    personel = models.ManyToManyField(to=User)
    last_update = models.DateTimeField(default=datetime.datetime.now())
    drone_priority = models.IntegerField(default=4)
    def get_name(self):
        return self.name
    picture = models.ImageField(upload_to=get_intersection_picture_path, blank=True)
    #roads


    def get_video(file_name):
        return
    
    def get_status():
        return 
    
    def delete(self, *args, **kwargs):
        self.picture.delete()
        super().delete(*args, **kwargs)

    def __str__(self) -> str:
        return self.name

class Video(models.Model):
    id = models.AutoField(primary_key=True)
    video_name = models.CharField(max_length=150, default='video')
    length = models.IntegerField() #Seconds
    uploader = models.ForeignKey(to=User,null=True, blank=True, default=None, on_delete=models.CASCADE)
    '''
    status
    0: processed complete and downloadable
    1: in process
    2: not process (pending)
    3: error
    '''
    status = models.IntegerField(default=2, max_length=3) 
    date_record = models.DateTimeField(default=datetime.datetime.now())
    auth_level = models.IntegerField()
    intersection = models.ForeignKey(Intersection, on_delete=models.CASCADE, null=True,blank=True)
    video_file = models.FileField(upload_to=get_video_path, blank=True, null=True)

    def __str__(self) -> str:
        return self.video_name

    def get_path(self):
        return self.video_file.name

    def delete(self, *args, **kwargs):
        self.video_file.delete()
        super().delete(*args, **kwargs)

class Summmary(models.Model):
    video = models.OneToOneField(Video, on_delete=models.CASCADE, null=True, blank=True)
    n_vehicle = models.IntegerField()

    def get_video_result():
        return

class Hitbox(models.Model):
    hitbox_id  =models.AutoField(primary_key=True, default=0)
    hitbox_name = models.CharField(max_length=64, default="loop")
    video = models.ForeignKey(Video, on_delete=models.CASCADE, null=True, blank=True)
    loops_file = models.FileField(upload_to=get_loop_path, null=True, blank=True)
    result_file = models.FileField(upload_to=get_loop_path, null=True, blank=True)
    def __str__(self) -> str:
        return ": " + str(self.hitbox_name)

    
class Follow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    intersection = models.ForeignKey(Intersection, on_delete=models.CASCADE)
    has_updated = models.BooleanField(default=False)
