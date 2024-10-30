from django.shortcuts import render
from rest_framework.generics import CreateAPIView, RetrieveAPIView, ListAPIView, UpdateAPIView

from users.models import TGUser
from users.serializers import UserSerializer


# Create your views here.


class UserCreateView(CreateAPIView):
    queryset = TGUser.objects.all()
    serializer_class = UserSerializer


class CurrentUserApiView(RetrieveAPIView):
    queryset = TGUser.objects.all()
    serializer_class = UserSerializer

class UserListApiView(ListAPIView ):
    queryset = TGUser.objects.all()
    serializer_class = UserSerializer

class UserUpdateApiView(UpdateAPIView):
    queryset = TGUser.objects.all()
    serializer_class = UserSerializer
