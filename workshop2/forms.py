from django import forms


class ScaleImageForm(forms.Form):
    notify = forms.EmailField()
    image = forms.FileField()
    name = forms.CharField(max_length=255)
