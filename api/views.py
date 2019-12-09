from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User, Group
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import RetrieveUpdateDestroyAPIView

# Create your views here.

from rest_framework import generics, viewsets
from .serializers import DeviceSerializer, UserSerializer, GroupSerializer
from .models import Device

def index(request):
    return HttpResponse("<html><h1>This is from my first app</html></h1>")

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class DeviceListViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all().order_by('serial')
    serializer_class = DeviceSerializer

    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()

class DeviceDetailViewSet(RetrieveUpdateDestroyAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    #lookup_url_kwarg = 'id'
    lookup_field = 'id'

"""
    def perform_destroy(self, instance):
        instance.delete()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
"""
