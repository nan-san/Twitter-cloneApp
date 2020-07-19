from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# 投稿する際のデータベース設定
class Post(models.Model):
    content = models.TextField()
    author = models.ForeignKey(User.on_delete=models.CASCADE)
    date_posted = models.DateField(default=timezone.now)
    likes = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)

# 管理者が見れるようにするための設定
    def __str__(self):
        return self.content  

