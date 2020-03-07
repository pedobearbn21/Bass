from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from rest_framework import generics
# from rest_framework.viewsets import ModelViewSet
from Bass.apps.web.models import Post, Comment, StackComment
from Bass.apps.api.serializers import PostSerializer, CommentSerializer

class PostList(generics.ListCreateAPIView) :
    # Comments
    # Look Up for the way to get comment in formPost
    queryset = Post.objects.all()
    # def get_queryset(self):
    #     b =  list(Post.objects.all())
    #     for i in b:
    #         i.comment = []
    #         a = list(Comment.objects.filter(post = i))
    #         for j in a:
    #             i.comment.append(j)
    #     return b
    

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