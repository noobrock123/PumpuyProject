from django.urls import path

from . import views

app_name = "BaseApp"

urlpatterns = [
    path('', views.index, name="index"),
    path('home', views.home_view, name="home"),
    path('login', views.login_view, name='login'),
    path('profile', views.profile_view, name='profile'),
    path('logout/', views.logout_view, name='logout'),
    path('intersection/<str:name>', views.intersection, name='intersection'),
    path('intersection/<str:name>/edit', views.edit, name='edit'),
    path('intersection/<str:name>/insert', views.insert, name='insert'),
]
