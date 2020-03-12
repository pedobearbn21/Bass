from django.shortcuts import render
from django.views import View
from django.http import JsonResponse,HttpResponse
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model,authenticate,login
from Bass.apps.web.models import Post, Comment, WareHouse, Payment
from Bass.apps.api.serializers import PostSerializer, CommentSerializer, UserDetailsSerializer, PaymentSerializer, WareHouseSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework.views import APIView

# User Detail with Post
class UserDetailsView(generics.RetrieveUpdateAPIView):
    serializer_class = UserDetailsSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user

    def get_queryset(self):
        return get_user_model().objects.none()

# class UserTest(View):
def UserTest(request, username, password):
    user =  UserModel.objects.get(username=username,password=password)
    return HttpResponse(user, content_type="text/json")
    serializer_class = UserDetailsSerializer

def Topup(request,id,used):
        Pay = Payment.objects.get(user_id = id)
        Pay.user.username = 'TestChange'
        Pay.save()
        return HttpResponse(Pay.user, content_type="text/json")
    

# Random Control on Homepage
class PostRand(generics.ListAPIView):
    queryset = Post.objects.order_by('?','status')
    serializer_class = PostSerializer

# All Post List In DB
class PostList(generics.ListCreateAPIView) :
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class Postrud(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    lookup_field = 'id'
    serializer_class = PostSerializer

class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class Commentrud(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    lookup_field = 'id'
    serializer_class = CommentSerializer

class Shopcart(generics.ListCreateAPIView):
    
    # def post(self, *args, **kwargs):
    #     # Pay = Payment.objects.get(user_id = self.request.userid)
    #     WareHouse = WareHouse(
    #                     content=self.request.content,
    #                     video=self.request.video,
    #                     price=self.request.price,
    #                     user=self.request.userid
    #                 )
    #     if(WareHouse.save()):
    #         # Pay.price - self.request.price
    #         # Pay.save()
    #         return 'Success'
    #     else:
    #         return 'Failed'
    queryset = WareHouse.objects.all()
    serializer_class = WareHouseSerializer

class Shopcartrud(generics.RetrieveUpdateDestroyAPIView):
    queryset = WareHouse.objects.all()
    lookup_field = 'id'
    serializer_class = CommentSerializer