from django.shortcuts import render
from django.template import loader
from .models import Video
# Create your views here.

def index(request):
    videos = Video.objects.all()

    context = {
        "Videos" : videos,
    }

    return render(request,'../templates/mainApp/index.html',context)
