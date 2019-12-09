from django.http import HttpResponse
from rest_framework import viewsets
from . import models, serializers
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters

from . import permissions

# Create your views here.


class UserProfileVeiwSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)

