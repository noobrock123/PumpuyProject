from django.urls import path

from . import views

app_name = "BaseApp"

urlpatterns = [
    path('', views.index, name="index"),
    path('home', views.home_view, name="home"),
    path('login', views.login_view, name='login'),
    path('profile/<str:id>', views.profile_view, name='profile'),
    path('logout/', views.logout_view, name='logout'),
    path('search', views.search_intersection, name='searchIntersection'),
    path('insert_intersection', views.insert_intersection, name='insert_intersection'),
    path('intersection/<str:name>', views.intersection, name='intersection'),
    path('intersection/<str:name>/edit', views.edit, name='edit'),
#    path('intersection/<str:name>/insert', views.insert, name='insert'),
    path('intersection/<str:name>/upload', views.upload_video, name='upload'),
    path('intersection/<str:name>/search', views.search_video, name='searchVideo'),
]
