from django.shortcuts import render
from django.http import JsonResponse

def index(request):
    data={
        "appname": "TUGASAN",
    }
    return JsonResponse(data)

def apiappdata(request):
    data={
        "menu": [
            {
                "modul":"satu",
                "link":"/"
            },
            {
                "modul":"dua",
                "link":"/"
            },
            {
                "modul":"tiga",
                "link":"/"
            },
            {
                "modul":"empat",
                "link":"/"
            },
        ],
        "appname" : "FROM API/APPDATA",
        "tajuk_test": "Covid-19 Data" 
    }
    return JsonResponse(data)