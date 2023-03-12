from django.contrib import admin
import BaseApp.models as models

# Register your models here.
class OrganizationAdminConfig(admin.ModelAdmin):
    model = models.Organization

#class AuthorityAdminConfig(admin.ModelAdmin):
#    model = models.Authority

class IntersectionAdminConfig(admin.ModelAdmin):
    model = models.Intersection

class RoadAdminConfig(admin.ModelAdmin):
    model = models.Road

class VideoAdminConfig(admin.ModelAdmin):
    model = models.Video

admin.site.register(models.Organization)
admin.site.register(models.Authority)
admin.site.register(models.Intersection)
admin.site.register(models.Road)
admin.site.register(models.Video)