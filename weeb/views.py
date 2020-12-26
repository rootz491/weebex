from django.shortcuts import render
from django.http import HttpResponse
# generic
from django.views import generic
from .models import *

# Create your views here.



class IndexView(generic.ListView):
    model = Post
    template_name = 'weeb/home.html'
    context_object_name = 'postObj'




def index(request):
    data = Post.objects.all()
    context = {
        'postObj': data,
    }
    print(data[1].likes.all())
    return render(request, 'weeb/home.html', context)




class PostDetailedView(generic.DetailView):
    model = Post
    template_name = 'weeb/postDetailed.html'
    context_object_name = 'post'






def postDetail(request, pk):
    data = Post.objects.filter(pk=pk)
    print(data[0])
    context = {
        'post': data[0],
    }
    return render(request, 'weeb/postDetailed.html', context)




class ProfileView(generic.DetailView):
    model = Profile