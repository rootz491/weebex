from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
# generic
from django.views import generic
from .models import *

# Create your views here.






#   function based

def postDetail(request, pk):
    data = Post.objects.filter(pk=pk)
    print(data[0])
    context = {
        'post': data[0],
    }
    return render(request, 'weeb/postDetailed.html', context)


def index(request):
    data = Post.objects.all()
    context = {
        'postObj': data,
    }
    print(data[1].likes.all())
    return render(request, 'weeb/home.html', context)








#   class based views

class IndexView(generic.ListView):
    model = Post
    template_name = 'weeb/home.html'
    context_object_name = 'postObj'


class PostDetailedView(generic.DetailView):
    model = Post
    template_name = 'weeb/postDetailed.html'
    context_object_name = 'post'


class PostDeleteView(generic.DeleteView):
    model = Post
    success_url = reverse_lazy('weeb:index')


class ProfileView(generic.DetailView):
    model = Profile
    template_name = 'weeb/profile.html'
    context_object_name = 'profile'




def PostLike(request, id):
    post = Post.objects.get(pk=id)
    if post.is_liked(request.user):
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    post.save()
    return redirect('weeb:index')
