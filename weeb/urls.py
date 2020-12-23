from django.urls import path
from . import views

app_name = 'weeb'

urlpatterns = [
    path(r'', views.index, name='index'),
]

