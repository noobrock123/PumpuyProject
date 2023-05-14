from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

app_name = "BaseApp"

__intersection_link: str = "intersection/<str:name>"
urlpatterns = [
    path('', views.index, name="index"),
    path('home', views.home_view, name="home"),
    path('login', views.login_view, name='login'),
    path('signup', views.signup_view, name='signup'),
    path('profile/<str:id>', views.profile_view, name='profile'),
    path('logout/', views.logout_view, name='logout'),
    path('summary/', views.summary, name='summary'),
    path('search', views.search_intersection, name='searchIntersection'),
    path('add_intersection', views.add_intersection, name='insert_intersection'),
    path(__intersection_link, views.intersection, name='intersection'),
    path(__intersection_link + "/edit", views.edit, name='edit'),
    # path(__intersection_link + "/create_loops", views.create_loops, name='create_loops'),
#    path('intersection/<str:name>/insert', views.insert, name='insert'),
    path(__intersection_link + "/upload", views.upload_video, name='upload'),
    path(__intersection_link + "/process/<int:video_id>", views.process_video, name='process'),
    path(__intersection_link + "/search", views.search_video, name='searchVideo'),
    path(__intersection_link + "/delete", views.delete_video, name="deleteVideo"),
    path(__intersection_link + "/summary/<int:video_id>", views.summary, name="summary"),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)