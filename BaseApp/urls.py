from django.urls import path

from . import views

app_name = "BaseApp"

urlpatterns = [
    path('', views.index, name="home"),
    path('login', views.login, name='login'),
    path('loging_user', views.loging_in, name='loging_in'),
    path('test', views.test, name='test')
]
