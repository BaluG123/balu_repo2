from django.shortcuts import render
from testApp.models import Music,Video

# Create your views here.
def music_view(request):
    music_list = Music.objects.all()
    return render(request,'testApp/musics.html',{'music_list':music_list})

def video_iew(request):
    video_list=Video.objects.all()
    return render(request,'testApp/video_list.html',{'video_list':video_list})  
