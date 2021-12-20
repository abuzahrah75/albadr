# from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
# from rest_framework import viewsets
from rest_framework.exceptions import PermissionDenied

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated



from django.contrib.auth import authenticate

from dokumen.models import Projek
from .serializers import ProjekSerializer

# for index
@api_view(['GET',])
def index(request):

    data ={
        "appname" : "TUGASAN"
    }

    return Response(data)

@api_view(['GET',])
def project_list(request):
    list_projek = Projek.objects.all()
    if request.method == "GET":
        serializer = ProjekSerializer(list_projek, many=True)
        return Response(serializer.data)
  

# # for test link
# @api_view(['GET',])
# def apiappdata(request):
#     data ={
#         "appname" : "TUGASAN",
#         "author" : "Abu Zahrah"
#     }

#     return Response(data)

# @api_view(['GET',])
# def list_untuk_beli(request):
#     untuk_beli = UntukBeli.objects.all()
#     if request.method == "GET":
#         serializer = UntukBeliSerializer(untuk_beli, many=True)
#         return Response(serializer.data)


# @api_view(['POST',])
# def save_untuk_beli(request):
#     nak_beli= UntukBeli()
#     if request.method == "POST":
#         serializer = UntukBeliSerializer(nak_beli, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['POST',])
# def edit_untuk_beli(request, pk):
#     nak_beli= UntukBeli.objects.get(id=pk)
#     if request.method == "POST":
#         serializer = UntukBeliSerializer(nak_beli, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['POST',])
# def delete_untuk_beli(request, pk):
#      nak_beli= UntukBeli.objects.get(id=pk)
#      if request.method == "POST":
#         nak_beli.delete()
#         data={'success': "item deleted"}
#         return Response(data, status=status.HTTP_200_OK)