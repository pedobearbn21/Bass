from rest_framework import serializers
from django.http import JsonResponse
from django.core.serializers import serialize
from Bass.apps.web.models import Post, Comment, StackComment


class CommentSerializer(serializers.ModelSerializer):

    def to_representation(self, value):
        return { "content": value.content, "video": value.video, "price": value.price, "at_time": value.at_time }

    class Meta:
        model = Comment
        fields = ['id','content','post','video','price','price','at_time']

class PostSerializer(serializers.ModelSerializer):
    comment = CommentSerializer(many=True, read_only=True)

    # def get_comment(self, obj):
        # return  serialize('json', Comment.objects.filter(post = obj))
        # return obj.comment_set.filter(post = obj)
    class Meta:
        model = Post
        fields = ['id','title', 'description','status','comment']
        # fields = '__all__'