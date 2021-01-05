from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from .models import *
import datetime

from PIL import Image



# class PostForm(forms.Form):
#     img = forms.ImageField(help_text='try to upload a square picture.')
#     caption = forms.CharField(max_length=100, help_text='length of caption should be less than 100 characters')
#
#     class Meta:
#         fields = ['img', 'caption']
#         model = Post
#
#     def clean_img(self):
#         data = self.cleaned_data['img']
#
#         original_width, original_height = data.size
#         size = (original_width*original_height)/1024
#         print(size)
#
#         # check if size is greater than 2MB
#         if size > 2000:
#             raise ValidationError(_('size\'s too big!'))
#
#         # returning cleaned data is necessary
#         return data


class PostForm(forms.ModelForm):
    class Meta:
        fields = ['img', 'caption']
        model = Post

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']