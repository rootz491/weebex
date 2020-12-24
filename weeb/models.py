from django.db import models
from uuid import uuid4 as uuid

# Create your models here.


class Post(models.Model):
    img = models.ImageField(upload_to='img')
    caption = models.CharField(max_length=100, null=True)
    id = models.UUIDField(default=uuid(), primary_key=True)

    def __str__(self):
        return 'post -> ' + self.id


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    likes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.likes


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.CharField(max_length=150, null=False)

    def __str__(self):
        return self.comment[:15]