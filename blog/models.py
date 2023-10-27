from django.db import models
from core.models import TimestampedModel


class Post(TimestampedModel):

    title = models.CharField(max_length=100)
    content = models.TextField()
    thumbnail = models.ImageField(
        upload_to='blog/images/', blank=True, null=True)
    file_upload = models.FileField(
        upload_to='blog/files/%Y/%m/%d/', blank=True, null=True)
    views = models.IntegerField(default=0)
    like_count = models.JSONField(default=dict, null=True, blank=True)
    author = models.ForeignKey(
        "accounts.User", on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return f'[{self.pk}]{self.title} by {self.author}'

    def get_absolute_url(self):
        return f'blog/{self.pk}'

    def get_file_ext(self):
        return self.get_file_name().split('.')[-1]


class Content_image(models.Model):
    content_image = models.ImageField(upload_to='blog/images/', blank=True)
    post_id = models.ForeignKey('Post', on_delete=models.CASCADE)
