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

##def get_video_path(instance, file):
    #return f"videos/{instance.}"


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
    picture = models.ImageField(upload_to='BaseApp/intersecPic', blank=True)
    #roads

    def get_video(file_name):
        return
    
    def get_status():
        return 
    
    def __str__(self) -> str:
        return self.name

class Video(models.Model):
    video_name = models.CharField(max_length=150, default='video')
    #video_file = models.FileField(upload_to=, blank=True)
    length = models.IntegerField() #Seconds
    uploader = models.ForeignKey(to=User,null=True, blank=True, default=None, on_delete=models.CASCADE)
    status = models.IntegerField(max_length=3, default=2)
    date_record = models.DateTimeField(default=datetime.datetime.now())
    auth_level = models.IntegerField()
    intersection = models.ForeignKey(Intersection, on_delete=models.CASCADE, null=True,blank=True)

    def __str__(self) -> str:
        return self.video_name

class Summmary(models.Model):
    video = models.OneToOneField(Video, on_delete=models.CASCADE, null=True)
    n_vehicle = models.IntegerField()

    def get_video_result():
        return

class Hitbox(models.Model):
    hitbox_name = models.CharField(max_length=64, default="loop")
    x = models.IntegerField(default=0)
    y = models.IntegerField(default=0)
    #size (list)
    summary = models.ForeignKey(Summmary, on_delete=models.CASCADE, null=True, blank=True)
    #cars = models.FileField(upload_to=)
    def __str__(self) -> str:
        return ": " + str(self.hitbox_name)

    
class Follow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    intersection = models.ForeignKey(Intersection, on_delete=models.CASCADE)
    has_updated = models.BooleanField(default=False)
