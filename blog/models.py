from django.db import models


class Post(models.Model):

    title = models.CharField(max_length=100)
    content = models.TextField()
    thumbnail = models.ImageField(
        upload_to='blog/images/', blank=True)
    file_upload = models.FileField(
        upload_to='blog/files/%Y/%m/%d/', blank=True)
    views = models.IntegerField(default=0)
    like_count = models.JSONField(default=dict, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    author = models.ForeignKey("accounts.User", on_delete=models.CASCADE)

    def __str__(self):
        return f'[{self.pk}]{self.title} by {self.author}'

    def get_absolute_url(self):
        return f'blog/{self.pk}'

    def get_file_ext(self):
        return self.get_file_name().split('.')[-1]


class Content_image(models.Model):
    content_image = models.ImageField(upload_to='blog/images/', blank=True)
    post_id = models.ForeignKey('Post', on_delete=models.CASCADE)
