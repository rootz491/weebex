from django.urls import path
from django.views.generic import RedirectView
from . import views


app_name = 'weeb'

urlpatterns = [
    # function based views
    # path(r'', views.index, name='index'),
    # path(r'post/<str:pk>/', views.postDetail, name='postDetail'),

    # class based views
    path(r'', views.IndexView.as_view(), name='index'),
    path(r'post/<str:pk>/', views.PostDetailedView.as_view(), name='postDetail'),
    path(r'post/<str:pk>/delete', views.PostDeleteView.as_view(), name='postDelete'),
    path(r'post/<str:id>/like', views.PostLike, name='postLike'),
    path(r'post/<str:pk>/comment', views.PostComment, name='postComment'),
    path(r'<str:pk>/', views.ProfileView.as_view(), name='profile'),
    # path(r'<str:pk>/upload/post', views.UploadPost, name='uploadPost'),
    path(r'<str:pk>/upload/post', views.PostView.as_view(), name='uploadPost'),

    path(r'favicon.ico', RedirectView.as_view(url='weeb/static/img/favicon.ico')),
]

