from django.db import models
from core.models import TimestampedModel
from accounts.models import User

class Post(TimestampedModel):

    title = models.CharField(max_length=100)
    content = models.TextField()
    thumbnail = models.ImageField(
        upload_to='blog/images/', blank=True, null=True)
    file_upload = models.FileField(
        upload_to='blog/files/%Y/%m/%d/', blank=True, null=True)
    views = models.IntegerField(default=0)
    like_count = models.IntegerField(default=0)
    author = models.ForeignKey(
        "accounts.User", on_delete=models.CASCADE, related_name='posts')
    comments_count = models.IntegerField(default=0)
    
    def __str__(self):
        return f'[{self.pk}]{self.title} by {self.author}'

    def get_absolute_url(self):
        return f'blog/{self.pk}'

    def get_file_ext(self):
        return self.get_file_name().split('.')[-1]
    
    def update_comments_count(self):
        self.comments_count = self.comments.count()
        self.save()

class Comment(TimestampedModel):
    author = models.ForeignKey("accounts.User", on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    #댓글
    comment = models.CharField(max_length=1000)
    # 대댓글 
    recomment = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE, related_name='recomments')

class Like(TimestampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)