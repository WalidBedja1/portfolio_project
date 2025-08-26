from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('projects/', views.project_list, name='project_list'),
    path('projects/recent/', views.recent_projects, name='recent_projects'),
    path('projects/<int:id>/', views.project_detail, name='project_detail'),
]