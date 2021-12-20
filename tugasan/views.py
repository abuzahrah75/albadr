from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response



def index(request):
    data={
        "appname": "TUGASAN",
    }
    return JsonResponse(data)

# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
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
        "appname" : "Tugasan : ",
        "tajuk_test": "Covid-19 Data" 
    }
    return JsonResponse(data)