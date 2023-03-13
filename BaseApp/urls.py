from django.urls import path

from . import views

app_name = "BaseApp"

urlpatterns = [
    path('', views.index, name="home"),
    path('login', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('intersection/<str:name>/', views.intersection, name='intersection'),
    path('intersection/<int:intersection_id>/edit', views.edit, name='edit'),
]
