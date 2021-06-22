from django import forms
from .models import *


class blogform(forms.ModelForm):
    class Meta:
        model = blog
        fields = "__all__"
