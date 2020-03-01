from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from rest_framework import generics
# from rest_framework.viewsets import ModelViewSet
from Bass.apps.web.models import Post, Comment, StackComment
from Bass.apps.api.serializers import PostSerializer

class PostList(generics.ListCreateAPIView) :
    # def get(self, request):
        # post = Post.objects.all()
        # serializer = PostSerializer(post)
        # return JsonResponse(serializer.data)
    queryset = Post.objects.all()
    serializer_class  = PostSerializer