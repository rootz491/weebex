from django.contrib.auth.models import User
from django.urls import reverse
from django.db import models
import uuid
# image customisation
from PIL import Image  # to modify the image before storing/uploading
from io import BytesIO  # to open file in binary formal
from django.core.files.uploadedfile import InMemoryUploadedFile  # to save image in memory / upload customised image
import sys  # to get size of output file.


# Create your models here.


class Profile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    username = models.CharField(max_length=30, help_text='should only contains alphabetic or numeric character.')
    fullName = models.CharField(max_length=60, help_text='60 characters or less.')  # new
    bio = models.TextField(max_length=140, help_text='140 characters or less.')  # new
    twitterHandle = models.CharField(max_length=40, help_text='40 characters or less.')  # new
    joinedOn = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username


class Post(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='img', help_text='try to upload a square picture.')
    caption = models.CharField(max_length=100, blank=True,
                               help_text='length of caption should be less than 100 characters')
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for each post')
    createdAt = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, blank=True, related_name='likes')

    class Meta:
        ordering = ['-createdAt']

    def __str__(self):
        return 'post @' + str(self.createdAt)



    # customizing image before uploading
    def save(self):
        # Opening the uploaded image
        im = Image.open(self.img)

        output = BytesIO()

        # Resize/modify the image
        # im = im.resize((500, 500))

        # testing
        print(sys.getsizeof(output))

        # after modifications, save it to the output
        im.save(output, format='JPEG', optimize=True, quality=40)
        output.seek(0)

        # change the ImageField value to be the newly modified image value
        self.img = InMemoryUploadedFile(output, 'ImageField', "%s.jpg" % self.img.name.split('.')[0], 'image/jpeg',
                                        sys.getsizeof(output), None)

        super(Post, self).save()




class Comment(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='user_comment')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_comment')
    comment = models.CharField(max_length=150, null=False,
                               help_text='length of comment should be less than 150 characters')
    likes = models.ManyToManyField(User, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-createdAt']

    def __str__(self):
        return 'comment @' + str(self.profile.username) + ' ' + str(self.id)
