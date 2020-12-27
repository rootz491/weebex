from django.shortcuts import render, reverse, redirect, get_object_or_404
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



# comment on posts
def PostComment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    profile = get_object_or_404(Profile, pk=request.user)

    if request.method == 'POST':
        comment = Comment()

        comment.comment = request.POST['comment']
        comment.post = post
        comment.profile = profile

        comment.save()

        return render(request, 'weeb/postDetailed.html', {'post': post})


# like on posts
def PostLike(request, id):
    post = Post.objects.get(pk=id)
    liked = False
    for user in post.likes.all():
        if user == request.user:
            liked = True
            break
    if liked:
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    post.save()
    return redirect('weeb:index')

