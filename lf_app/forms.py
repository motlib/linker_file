'''Forms used in the `loc` application.'''

from django import forms
from django.shortcuts import redirect

from .models import Link


class LinkForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = ['url', 'title', 'notes', 'tags']
