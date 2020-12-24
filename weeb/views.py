from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.



def index(request):
    data = Post.objects.all()
    context = {
        'postObj': data,
    }
    return render(request, 'weeb/home.html', context)