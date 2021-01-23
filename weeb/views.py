from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
# auth and login
from django.contrib.auth import login, authenticate
# permission check
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required
# generic
from django.views.generic import View
from django.views import generic
from .models import *
from .forms import PostForm, RegisterForm, userDeleteForm
# flash messages
from django.contrib import messages
# regex to password check
import re
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

class IndexView(LoginRequiredMixin, generic.ListView):
    login_url = 'login'
    model = Post
    template_name = 'weeb/home.html'
    context_object_name = 'postObj'

    def get_queryset(self):
        """Return the last five posts."""
        return Post.objects.order_by('-createdAt')[:5]


class PostDetailedView(LoginRequiredMixin, generic.DetailView):
    model = Post
    template_name = 'weeb/postDetailed.html'
    context_object_name = 'post'


class PostDeleteView(LoginRequiredMixin, generic.DeleteView):
    login_url = 'login'
    model = Post
    success_url = reverse_lazy('weeb:index')


# class ProfileView(generic.DetailView):
#     model = Profile
#     template_name = 'weeb/profile.html'
#     context_object_name = 'profile'


class PostView(LoginRequiredMixin, generic.CreateView):
    login_url = 'login'
    template_name = 'weeb/post_form.html'
    model = Post
    fields = ['img', 'caption']


@login_required
def ProfileEdit(request, username):
    template_name = 'weeb/profile_form.html'




@login_required
# @permission_required('weeb.moderator', raise_exception=True)
def profile(request, username):
    u = get_object_or_404(User, username=username)
    p = get_object_or_404(Profile, pk=u)
    return render(request, 'weeb/profile.html', {'profile': p})


def userDelete(request, username):

    if request.method == 'POST':
        try:
            form = userDeleteForm(request.POST)
            user = User.objects.get(username=username)
            if request.user == user:
                pass
            else:
                print('forbidden')
                messages.add_message(request, messages.ERROR, 'forbidden')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

            # check whether it's valid:
            if form.is_valid():
                thatUSer = form.save(commit=False)
                password = thatUSer.password
                print(password)
                if user.check_password(password):
                    print('deleted!')
                    # user.delete()
                    messages.success(request, "The user is deleted")
                    return reverse('login')
                else:
                    messages.add_message(request, messages.ERROR, 'Wrong password. please try again!')
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        except User.DoesNotExist:
            messages.add_message(request, messages.ERROR, 'User doesn\'t exist')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        except Exception as e:
            messages.add_message(request, messages.ERROR, e)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


    # make a post request
    return render(request, 'front.html')



def CommentDeleteView(request, postPk, commentPk):
    if request.method == 'POST':
        try:
            post = Post.objects.get(pk=postPk)
            comment = Comment.objects.get(pk=commentPk)

            if not comment.user == request.user:
                messages.add_message(request, messages.WARNING, 'you don\'t own this comment!')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

            if not comment.post == post:
                messages.add_message(request, messages.WARNING, 'comment doesn\'t belong to this post')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

            comment.delete()
            messages.add_message(request, messages.INFO, 'comment deleted successfully')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        except Post.DoesNotExist:
            messages.add_message(request, messages.ERROR, 'post doesn\'t exists')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        except Comment.DoesNotExist:
            messages.add_message(request, messages.ERROR, 'comment doesn\'t exists')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))



# comment on posts
@login_required
def PostComment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        comment = Comment()

        comment.comment = request.POST['comment']
        comment.post = post
        comment.user = request.user

        comment.save()
        messages.add_message(request, messages.SUCCESS, 'comment added successfully')
        # return render(request, 'weeb/postDetailed.html', {'post': post})
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


# like on posts
@login_required
def PostLike(request, id):
    # post = Post.objects.get(pk=id)
    post = get_object_or_404(Post, pk=id)
    liked = False
    for user in post.likes.all():
        if user == request.user:
            liked = True
            break
    if liked:
        post.likes.remove(request.user)
        messages.add_message(request, messages.ERROR, 'Disliked')
    else:
        post.likes.add(request.user)
        messages.add_message(request, messages.SUCCESS, 'Liked')
    # post.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


# upload post
@login_required
def UploadPost(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        form = PostForm(request.POST or None, request.FILES or None)

        # check whether it's valid:
        if form.is_valid():
            newPost = form.save(commit=False)
            newPost.img = form.cleaned_data['img']
            newPost.caption = form.cleaned_data['caption']
            newPost.user = request.user
            newPost.save()

            return render(request, 'weeb/postDetailed.html', {'post': newPost})


        # print(form.errors)
        return render(request, 'weeb/post_form.html', context={'form': form, 'form.error': form.errors})

    form = PostForm()
    return render(request, 'weeb/post_form.html', {'form': form})




def registerUser(request):
    template_name = 'registration/register.html'

    # display blank form
    if request.method == 'GET':
        # form = RegisterForm()    ima manually creating form
        return render(request, template_name)      # , {'form': form})

        # process form data

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            newUser = form.save(commit=False)
            # clean (normalize) the data.
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']

            # EMAIL check
            existingUser = User.objects.filter(email=email)
            if existingUser:
                messages.add_message(request, messages.ERROR, 'email already registered')
                print('username already exists')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            # PASSWORD check
            reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,32}$"
                # compiling regex
            pat = re.compile(reg)
                # searching regex
            mat = re.search(pat, password)
            if mat:
                pass
            else:
                print(password)
                messages.add_message(request, messages.ERROR, 'Weak password!')
                messages.add_message(request, messages.INFO, 'password should be 8-32 characters long, with one aphabet (upper & lower-case) with atleast 1 special character.')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

            # creating new user
            newUser.set_password(password)      # password cannot be saved directly so this function will first hash it and then save it!
            newUser.save()
            print(newUser)
            # at this point, user data is stored into database.

            newProfile = Profile()
            newProfile.user = newUser
            newProfile.username = username
            newProfile.fullName = username
            newProfile.save()
            # user can add twitter handle and bio by editing profile.

            messages.add_message(request, messages.SUCCESS, 'Registered successfully')
            messages.add_message(request, messages.INFO, 'Please login to enjoy site')
            return redirect('login')


        # if form is not valid then,
        messages.add_message(request, messages.WARNING, 'something\'s wrong with user, contact admin')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
