from rest_framework import serializers
from .models import Device, FileUpload

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'

class FileUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileUpload
        fields = '__all__'
