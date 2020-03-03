from django.shortcuts import render
# from django.http import HttpResponseRedirect, HttpResponse
# from django.urls import reverse

def index(request):
    context ={
        'tajuk': "Indeks alBadr",
        'isi': "Saya suka makan nasi sebab hari-hari saya makan nasi",
    }
    # return HttpResponse("testing")
    return render(request, 'home/temp.html', context)


def cubaan(request):
    from django.contrib.auth.models import User

    context={
        'myoutput': User.objects.all()
    }

    return render(request, 'home/cubaan.html', context)