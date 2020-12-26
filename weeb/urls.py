from django.urls import path
from . import views


app_name = 'weeb'

urlpatterns = [
    # path(r'', views.index, name='index'),
    path(r'', views.IndexView.as_view(), name='index'),
    # path(r'post/<str:pk>/', views.postDetail, name='postDetail'),
    path(r'post/<str:pk>/', views.PostDetailedView.as_view(), name='postDetail')
]

