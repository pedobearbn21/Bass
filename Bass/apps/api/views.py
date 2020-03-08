from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
# from rest_framework.viewsets import ModelViewSet
from Bass.apps.web.models import Post, Comment, StackComment
from Bass.apps.api.serializers import PostSerializer, CommentSerializer, UserDetailsSerializer



class UserDetailsView(generics.RetrieveUpdateAPIView):
    serializer_class = UserDetailsSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user

    def get_queryset(self):
        return get_user_model().objects.none()



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