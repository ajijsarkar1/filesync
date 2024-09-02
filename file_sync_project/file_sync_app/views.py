from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import User, Device, File
from .serializers import UserSerializer, DeviceSerializer, FileSerializer
import pika
import json

class FileViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        self.notify_other_devices(instance)

    def notify_other_devices(self, file_instance):
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()
        channel.queue_declare(queue='file_notifications')

        message = {
            'file': file_instance.file.url,
            'device_id': file_instance.device.device_id,
        }

        channel.basic_publish(exchange='', routing_key='file_notifications', body=json.dumps(message))
        connection.close()

class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserSessionView(viewsets.ViewSet):
    def create(self, request):
        user_id = request.data.get('user_id')
        device_id = request.data.get('device_id')
        if not user_id or not device_id:
            return Response({"error": "user_id and device_id are required"}, status=400)

        # Save or update user session and device information
        Device.objects.update_or_create(user_id=user_id, device_id=device_id)

        # Notify other devices
        self.notify_other_devices(user_id, device_id)

        return Response({"message": "Session started successfully"})

    def notify_other_devices(self, user_id, device_id):
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()
        queue_name = f"user_{user_id}_notifications"
        channel.queue_declare(queue=queue_name)

        message = {
            'user_id': user_id,
            'device_id': device_id,
            'event': 'session_started',
        }

        channel.basic_publish(exchange='', routing_key=queue_name, body=json.dumps(message))
        connection.close()
