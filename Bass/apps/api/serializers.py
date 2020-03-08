from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.core.serializers import serialize
from Bass.apps.web.models import Post, Comment, StackComment, Payment
# GET Model User
UserModel = get_user_model()


class UserDetailsSerializer(serializers.ModelSerializer):
    payments = serializers.SerializerMethodField('get_pay')
    def get_pay(self, obj):
        data = Payment.objects.filter(user = obj)[0]
        return data.price

    class Meta:
        model = UserModel
        fields = ('pk', 'username', 'email','payments')
        read_only_fields = ('email', )



class CommentSerializer(serializers.ModelSerializer):

    def to_representation(self, value):
        return { "content": value.content, "video": value.video, "price": value.price, "at_time": value.at_time }

    class Meta:
        model = Comment
        fields = ['id','content','post','video','price','price','at_time']

class PostSerializer(serializers.ModelSerializer):
    comment = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = Post
        fields = ['id','title', 'description','status','comment']