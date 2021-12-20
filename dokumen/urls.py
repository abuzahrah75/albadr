from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="dokumen-index"),
    # path('home/cubaan/', views.cubaan, name="home-cubaan"),
    # path('api/projects-list', views.projects_list, name="dokumen-projects-list"),

]
