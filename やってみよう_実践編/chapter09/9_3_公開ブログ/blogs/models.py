from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    """個人または組織のブログを表す"""
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """ブログの文字列表現を返す"""
        return self.name

class BlogPost(models.Model):
    """個別の投稿を表す"""
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    
    title = models.CharField(max_length=500)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """投稿の文字列表現を返す"""
        if len(self.title) > 50:
            return f"{self.title[:50]}..."
        else:
            return self.title