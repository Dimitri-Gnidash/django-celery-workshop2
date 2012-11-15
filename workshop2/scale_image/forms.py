from django import forms

from models import NotifyScaledImage


class NotifyScaledImageForm(forms.ModelForm):
    class Meta:
        model = NotifyScaledImage
