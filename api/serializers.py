from rest_framework  import serializers
from django.contrib.auth.models import User, Group
from .models import Device, CustomUser, CustomGroup

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'url')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('name',)

class DeviceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta():
        model = Device
        #fields = ('id','name', 'serial', 'fw_version', 'dev_model')
        fields = '__all__'
        #read_only_fields = ('date_created',)
