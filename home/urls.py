from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home-index"),
    path('home/cubaan/', views.cubaan, name="home-cubaan"),

]
