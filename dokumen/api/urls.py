from django.urls import path
from . import apiviews

app_name = 'dokumen'

urlpatterns = [
   
    path('', apiviews.index, name="dokumen-api-index"),
    path('project/list', apiviews.project_list, name="dokumen-api-projek-list"),
   
    # path('home/cubaan/', views.cubaan, name="home-cubaan"),

]
    

