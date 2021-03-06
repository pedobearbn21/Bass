"""Bass URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers, serializers
from Bass.apps.api import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    # Rest-auth
        url(r'^rest-auth/', include('rest_auth.urls')),
        url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    #Detail User
        path('user/detail/', views.UserDetailsView.as_view(), name='rest_user_details'),
        path('user/<username>/<password>/', views.UserTest),
    # GenToken
        path('api-token-auth/', obtain_auth_token, name='api_token_auth'), 
    #Post
        path('Postlistrand', views.PostRand.as_view()),
        path('Postlist', views.PostList.as_view()),
        path('Postlist/<int:id>', views.Postrud.as_view()),
    # Comment
        path('Commentlist', views.CommentList.as_view()),
        path('Commentlist/<int:id>', views.Commentrud.as_view()),
    # Shopping
        path('Shopcart', views.Shopcart.as_view()),
        path('Shopcart/<int:id>', views.Shopcartrud.as_view()),
        path('Topup/<int:id>/income/<int:income>', views.Topup),
        path('Paid/<int:id>/cost/<int:cost>', views.Paid),
    # Test API
        path('ch/', views.ch)
]
