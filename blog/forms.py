from django import forms
from .models import Post  # Comment, Tag


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'thumbnail', 'file_upload']

    # thumbnail = forms.ImageField(required=False)
    # file_upload = forms.FileField(required=False)
