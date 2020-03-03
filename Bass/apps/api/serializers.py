from rest_framework import serializers
from Bass.apps.web.models import Post, Comment, StackComment

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id','title', 'description','status']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id','content','post','video','price','price','at_time']