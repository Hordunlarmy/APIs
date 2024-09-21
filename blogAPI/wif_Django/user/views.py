from rest_framework import generics, permissions, status
from rest_framework.response import Response

from .models import User
from .serializers import SignUpSerializer


class SignUpView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SignUpSerializer
    permission_classes = [permissions.AllowAny]
