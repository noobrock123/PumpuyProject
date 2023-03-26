from django.db import models
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
import datetime

fs = FileSystemStorage(location='BaseApp/videos')

auth_select = (
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


class Video(models.Model):
    video_name = models.CharField(max_length=150, default='video')
    video_file = models.FileField(storage=fs, blank=True)
    length = models.IntegerField() #Seconds
    uploader = models.ForeignKey(to=User,null=True, blank=True, default=None, on_delete=models.CASCADE)
    status = models.IntegerField(max_length=3, default=2)
    date_record = models.DateTimeField(default=datetime.datetime.now())
    auth_level = models.IntegerField()

    def __str__(self) -> str:
        return self.video_name

fsIntersecPic = FileSystemStorage(location="BaseApp/static/images")
class Intersection(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    location = models.CharField(max_length=512)
    latitude = models.FloatField()
    longtitude = models.FloatField()
    intersec_type = models.IntegerField()
    status = models.IntegerField()
    owner = models.ForeignKey(Organization, on_delete=models.CASCADE, null=True, blank=True)
    last_update = models.DateTimeField(default=datetime.datetime.now())
    drone_priority = models.IntegerField(default=4)
    picture = models.ImageField(storage=fsIntersecPic, blank=True)
    videos = models.ManyToManyField(Video)
    #roads

    def get_video(file_name):
        return
    
    def get_status():
        return 
    
    def __str__(self) -> str:
        return self.name

class Road(models.Model):
    intersection = models.ForeignKey(Intersection, on_delete=models.CASCADE, null=True)
    road_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    go_to_most = models.IntegerField()
    go_to_nCars = models.IntegerField()

    def __str__(self) -> str:
        return self.intersection + ": " + self.road_id

class Hitbox(models.Model):
    hitbox_id = models.IntegerField()
    x = models.IntegerField()
    y = models.IntegerField()
    #size (list)
    road = models.ForeignKey(Road, on_delete=models.CASCADE, null=True)
    def __str__(self) -> str:
        return self.hitbox_id + ": " + self.road.road_id

class Car(models.Model):
    car_type = models.CharField(max_length=15)
    avg_speed = models.FloatField()
    #go_to (list, hitbox)

class Summmary(models.Model):
    #vehicle (Dictionary)
    n_vehicle = models.IntegerField()
    #direction (list, hitbox)
    #nCar_direction (list, [road, int])
    #avg_speed (list, [road, int])
    #cars(Car)

    def get_video_result():
        return
    
class Follow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    intersection = models.ForeignKey(Intersection, on_delete=models.CASCADE)
    has_updated = models.BooleanField(default=False)
