from django.urls import path
from . import views


app_name = 'weeb'

urlpatterns = [
    # function based views
    # path(r'', views.index, name='index'),
    # path(r'post/<str:pk>/', views.postDetail, name='postDetail'),

    # class based views
    path(r'', views.IndexView.as_view(), name='index'),
    path(r'post/<str:pk>/', views.PostDetailedView.as_view(), name='postDetail'),
    path(r'<str:pk>/', views.ProfileView.as_view(), name='profile'),
]

