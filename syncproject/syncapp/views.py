# from django.shortcuts import render

# # Create your views here.


from rest_framework import viewsets
from rest_framework.response import Response
from .models import Device, FileUpload
from .serializers import DeviceSerializer, FileUploadSerializer
import pika

class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

class FileUploadViewSet(viewsets.ModelViewSet):
    queryset = FileUpload.objects.all()
    serializer_class = FileUploadSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        # Notify other devices through RabbitMQ
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()
        channel.queue_declare(queue='file_uploads')

        channel.basic_publish(
            exchange='',
            routing_key='file_uploads',
            body=f'File uploaded by {instance.device.name} for user {instance.device.user.username}'
        )
        connection.close()
