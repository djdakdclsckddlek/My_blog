from django import forms
from .models import Post, Comment  # Tag


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'thumbnail', 'file_upload']

class CommentForm(forms.ModelForm):
    recomment = forms.IntegerField(widget=forms.HiddenInput, required=False)
    class Meta:
        model = Comment
        fields = ['comment']