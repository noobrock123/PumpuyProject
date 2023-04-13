from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

app_name = "BaseApp"

urlpatterns = [
    path('', views.index, name="index"),
    path('home', views.home_view, name="home"),
    path('login', views.login_view, name='login'),
    path('profile/<str:id>', views.profile_view, name='profile'),
    path('logout/', views.logout_view, name='logout'),
    path('search', views.search_intersection, name='searchIntersection'),
    path('add_intersection', views.add_intersection, name='insert_intersection'),
    path('intersection/<str:name>', views.intersection, name='intersection'),
    path('intersection/<str:name>/edit', views.edit, name='edit'),
#    path('intersection/<str:name>/insert', views.insert, name='insert'),
    path('intersection/<str:name>/upload', views.upload_video, name='upload'),
    path('intersection/<str:name>/search', views.search_video, name='searchVideo'),
    path('intersection/<str:name>/delete', views.delete_video, name="deleteVideo"),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)