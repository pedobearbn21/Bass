from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.core.serializers import serialize
from Bass.apps.web.models import Post, Comment, WareHouse, Payment
# GET Model User
UserModel = get_user_model()



class WareHouseSerializer(serializers.ModelSerializer):

    def to_representation(self, value):
        return { "content": value.content, "video": value.video, "price": value.price}

    class Meta:
        model = WareHouse
        # fields = ['id','user','content','video','price','at_time']
        fields = '__all__'


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
        fields = ['id','title', 'user','description','status','comment']


class UserDetailsSerializer(serializers.ModelSerializer):
    payments = serializers.SerializerMethodField('get_pay')
    # post = PostSerializer(many=True,read_only=True)
    post = serializers.SerializerMethodField('get_post')
    warehouse = serializers.SerializerMethodField('get_warehouse')

    def get_pay(self, obj):
        data = Payment.objects.get(user = obj)
        return data.price

    def get_post(self,obj):
        data = Post.objects.filter(user= obj).values()
        serializer_class = PostSerializer
        return data
    
    def get_warehouse(self,obj):
        data = WareHouse.objects.filter(user= obj).values()
        serializer_class = WareHouseSerializer
        return data

    class Meta:
        model = UserModel
        fields = ('pk', 'username', 'email','payments','post', 'warehouse')
        read_only_fields = ('email', )

# Bad Smell
# มีการประกาศไว้แต่ยังไม่ได้เรัยกใช้

class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = '__all__'