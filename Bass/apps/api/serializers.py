from rest_framework import serializers
from Bass.apps.web.models import Post, Comment, StackComment

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'description']