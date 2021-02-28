from django.urls import path
from django.views.generic import RedirectView
from . import views


app_name = 'weeb'

urlpatterns = [
    # home page
    path(r'', views.IndexView.as_view(), name='index'),

    # search page
    path(r'search/', views.SearchView.as_view(), name='search'),

    # detailed post
    path(r'post/<str:pk>/', views.PostDetailedView.as_view(), name='postDetail'),

    # operations on post
    path(r'post/upload', views.UploadPost, name='uploadPost'),
    path(r'post/<str:pk>/delete', views.PostDeleteView.as_view(), name='postDelete'),
    path(r'post/<str:id>/like', views.PostLike, name='postLike'),
    path(r'post/<str:pk>/comment', views.PostComment, name='postComment'),
    path(r'post/<postPk>/comment/<commentPk>/delete', views.CommentDeleteView, name='commentDelete'),

    # profile
    path(r'<str:username>', views.profile, name='profile'),
    path(r'<pk>/edit', views.ProfileEditView.as_view(), name='profileEdit'),
    path(r'<str:username>/account/delete', views.userDelete, name='userDelete'),

    # register
    path(r'accounts/register', views.registerUser, name='register'),

    # landing
    path(r'welcome/', views.landing, name='landing'),

    # error handling
    path(r'favicon.ico', RedirectView.as_view(url='weeb/static/img/favicon.ico'))
]
