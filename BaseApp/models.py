from django.db import models

# Create your models here.
class Intersection(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    location = models.CharField(max_length=200)
    latitude = models.FloatField()
    longtitude = models.FloatField()
    intersec_type = models.IntegerField()
    status = models.IntegerField()
    last_update = models.DateTimeField()
    drone_priority = models.IntegerField()
    #roads

    def get_video(file_name):
        return
    
    def get_status():
        return 

class Road(models.Model):
    road_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    go_to_most = models.IntegerField()
    go_to_nCars = models.IntegerField()
    #hitbox

class Hitbox(models.Model):
    hitbox_id = models.IntegerField()
    x = models.IntegerField()
    y = models.IntegerField()
    #size (list)

class Car(models.Model):
    car_type = models.CharField()
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

class Video(models.Model):
    #video_file
    length = models.IntegerField()
    #owner
    date_record = models.DateTimeField()
    intersection = models.OneToOneField(Intersection, on_delete=models.CASCADE)
    auth_level = models.IntegerField()
