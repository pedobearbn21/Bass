from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from rest_framework import generics

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


from django.contrib.auth.models import User
# from django.contrib.auth import authenticate, login
# from django.contrib.auth import logout

# from rest_framework.viewsets import ModelViewSet
from Bass.apps.web.models import Post, Comment, StackComment
from Bass.apps.api.serializers import PostSerializer, CommentSerializer

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

# User Control


class HelloView(APIView):

    def get(self, request):
        permission_classes = (IsAuthenticated,)           
        content = {'message': 'Hello, World!'}
        return Response(content)
    
    def post(self,request):
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(username,request.POST['email'],password)
        if(user.save()):
            return 'Success'
        else:
            return 'Failed'




# Create your views here.
# class MainPage(View):

#     def Login(self, request):
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return user
#         else:
#             pass

#     


#     def logout_view(self,request):
#         logout(request)
        # Redirect to a success page.