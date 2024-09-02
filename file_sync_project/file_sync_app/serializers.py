from rest_framework import serializers
from .models import User, Device, File

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = '__all__'

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    devices = DeviceSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = ['username', 'devices']
