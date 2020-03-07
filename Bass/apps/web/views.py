from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout

# Create your views here.
class MainPage(View):

    def Login(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            ...
        else:
            # Return an 'invalid login' error message.
            ...

    def Register(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(username,request.POST['email'],password)
        if(user.save()):
            return 'Success'
        else:
            return 'Failed'


    def logout_view(self,request):
        logout(request)
        # Redirect to a success page.
    