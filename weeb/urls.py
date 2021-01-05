from django.urls import path
from django.views.generic import RedirectView
from . import views


app_name = 'weeb'

urlpatterns = [
    # function based views
    # path(r'', views.index, name='index'),
    # path(r'post/<str:pk>/', views.postDetail, name='postDetail'),

    # class based views

    # home page
    path(r'', views.IndexView.as_view(), name='index'),

    # detailed post
    path(r'post/<str:pk>/', views.PostDetailedView.as_view(), name='postDetail'),

    # operations on post
    path(r'post/<str:pk>/delete', views.PostDeleteView.as_view(), name='postDelete'),
    path(r'post/<str:id>/like', views.PostLike, name='postLike'),
    path(r'post/<str:pk>/comment', views.PostComment, name='postComment'),

    # profile
    path(r'<str:username>', views.profile, name='profile'),
    # path(r'<str:pk>/', views.ProfileView.as_view(), name='profile'),

    # post upload
    path(r'post/upload', views.UploadPost, name='uploadPost'),
    # path(r'post/upload', views.PostView.as_view(), name='uploadPost'),

    # register
    path(r'account/register', views.registerUser, name='register'),

    # error handling
    path(r'favicon.ico', RedirectView.as_view(url='weeb/static/img/favicon.ico')),
]



