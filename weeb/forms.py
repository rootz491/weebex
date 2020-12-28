from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime


class UploadPost(forms.Form):
    image = forms.DateField(help_text='Enter a date between now and 4 weeks (default 3).')
    caption = forms.CharField(max_length=100, blank=True,
                              help_text='length of caption should be less than 100 characters')

    def clean_image(self):
        data = self.cleaned_data['image']

        # check if date is not past
        if data < datetime.date.today():
            raise ValidationError(_('Invalid date - renewal in past'))

        # check if data is in allowed range ( +4 weeks from today)
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(_('Invalid date - renewal more than 4 weeks ahead.'))

        # returning cleaned data is necessary
        return data
