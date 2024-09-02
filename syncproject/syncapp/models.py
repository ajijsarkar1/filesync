from django.db import models
from django.contrib.auth.models import User

class Device(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

class FileUpload(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    file = models.FileField(upload_to='uploads/')
    timestamp = models.DateTimeField(auto_now_add=True)
