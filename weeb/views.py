from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.



def index(request):
    data = Post.objects.filter(user=request.user)
    context = {
        'postObj': data,
    }
    return render(request, 'weeb/home.html', context)



def postDetail(request, pk):
    data = Post.objects.filter(pk=pk)
    print(data[0])
    context = {
        'post': data[0],
    }
    return render(request, 'weeb/postDetailed.html', context)
