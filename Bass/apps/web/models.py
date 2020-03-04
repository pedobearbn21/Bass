from django.db import models
from datetime import datetime

# Create your models here.


class User(models.Model):
    Username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    status_type = (
    (1, 1),
    (2, 2),
    )
    status = models.IntegerField(choices=status_type, default=1)

class CommentABS(models.Model):
    # userid = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(default='')
    video = models.TextField(blank=True)
    price = models.DecimalField(max_digits=19, decimal_places=2 )
    at_time = models.DateTimeField(default=datetime.now)

    class Meta:
        abstract = True
        ordering = ['at_time']

class Comment(CommentABS):
    # userid = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post , related_name='comment',on_delete=models.CASCADE)

    def __str__(self):
        return 'Pid: {} ,Ptitle: {}'.format(self.post.id,self.post.title)


class StackComment(CommentABS):
    # stack = models.ForeignKey(Comment, on_delete=models.CASCADE)
    # at_time = models.DateTimeField(default=datetime.now)
    class Meta(CommentABS.Meta):
        db_table = 'Stack_Comment'

class Test(models.Model):
    Test = models.TextField()