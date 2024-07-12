from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login, logout

from .serializer import RegisterSerailizer, LoginSerailizer
from .models import User
# Create your views here.


class RegisterView(APIView):
    
    def post(self, request):
        serializer = RegisterSerailizer(data=request.data)
        
        if serializer.is_valid():
            password = serializer.validated_data.get('password')
            user = serializer.save()
            user.set_password(password)
            user.save()
            return Response({'user': "user registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class LoginView(APIView):
    
    def post(self, request, format=None):
        serializer = LoginSerailizer(data=request.data)
        
        if serializer.is_valid():
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            user  = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                return Response({'user': "You are loggedin successfully"}, status=status.HTTP_200_OK)
            else:
                return Response({"Error": "Please enter valid credentials."}, status=status.HTTP_404_NOT_FOUND)        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)