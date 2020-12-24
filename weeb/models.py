from django.db import models
import uuid

# Create your models here.


class Post(models.Model):
    img = models.ImageField(upload_to='img', help_text='try to upload a square picture.')
    caption = models.CharField(max_length=100, blank=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for each post')

    def __str__(self):
        return 'post'


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