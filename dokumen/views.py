from django.shortcuts import render


def index(request):

    context={}
    return render(request,'dokumen/index.html', context)