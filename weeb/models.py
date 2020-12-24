from django.contrib.auth.models import User
from django.urls import reverse
from django.db import models
import uuid
# Create your models here.


class Profile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    username = models.CharField(max_length=30, blank=False)

    joinedOn = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username



class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='img', help_text='try to upload a square picture.')
    caption = models.CharField(max_length=100, blank=True, help_text='length of caption should be less than 100 characters')
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for each post')
    createdAt = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, blank=True, related_name='likes')

    class Meta:
        ordering = ['-createdAt']

    def __str__(self):
        return 'post @' + str(self.createdAt)




class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.CharField(max_length=150, null=False, help_text='length of comment should be less than 150 characters')

    def __str__(self):
        return self.comment[:15]