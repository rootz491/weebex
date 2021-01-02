from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
# generic
from django.views import generic
from .models import *
from .forms import PostForm

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


class PostView(generic.CreateView):
    template_name = 'weeb/post_form.html'
    model = Post
    fields = ['img', 'caption']




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
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def UploadPost(request, pk):
    user = get_object_or_404(User, pk=pk)
    profile = get_object_or_404(Profile, pk=user)


    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        form = PostForm(request.POST)


        # check whether it's valid:
        if form.is_valid():
            newPost = Post(commit=False)
            cd = form.cleaned_data
            newPost.img = cd['img']
            newPost.caption = cd['caption']
            newPost.profile = profile
            newPost.save()

            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        print(form.errors)
        return render(request, 'weeb/message.html', context={'message': 'Form is not valid!'})

    return render(request, 'weeb/message.html', context={'message': 'Make a POST request to upload a form'})