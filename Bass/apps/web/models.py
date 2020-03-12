from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.


class Payment(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='payment' )
    price = models.IntegerField(default=0)

class Post(models.Model):
    title = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE ,related_name='post', default=1)
    description = models.TextField()
    status_type = (
    (1, 1),
    (2, 2),
    )
    status = models.IntegerField(choices=status_type, default=1)

class CommentABS(models.Model):
    content = models.TextField(default='')
    video = models.TextField(blank=True)
    price = models.DecimalField(max_digits=19, decimal_places=2 )
    at_time = models.DateTimeField(default=datetime.now)

    class Meta:
        abstract = True
        ordering = ['-at_time']

class Comment(CommentABS):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    post = models.ForeignKey(Post , related_name='comment',on_delete=models.CASCADE)

    def __str__(self):
        return 'Pid: {} ,Ptitle: {}'.format(self.post.id,self.post.title)


class WareHouse(CommentABS):
    user = models.ForeignKey(User, on_delete=models.CASCADE ,related_name='warehouse', default=1)

class Test(models.Model):
    Test = models.TextField()