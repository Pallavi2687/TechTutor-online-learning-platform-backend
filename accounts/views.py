from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions
from .serializers import RegisterSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenSerializer  # Make sure this is in accounts/serializers.py


class RegisterView(generics.CreateAPIView):
    serializer_class   = RegisterSerializer
    permission_classes = [permissions.AllowAny]

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenSerializer
