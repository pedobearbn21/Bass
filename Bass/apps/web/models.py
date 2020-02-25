from django.db import models
from datetime import datetime

# Create your models here.


class User(models.Model):
    Username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

class Comment(models.Model):
    # userid = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return 'Pid: {} ,Ptitle: {}'.format(self.post.id,self.post.title)

class StackComment(models.Model):
    stack = models.ForeignKey(Comment, on_delete=models.CASCADE)
    at_time = models.DateTimeField(default=datetime.now)

class Test(models.Model):
    Test = models.TextField()