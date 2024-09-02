from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.username

class Device(models.Model):
    user = models.ForeignKey(User, related_name='devices', on_delete=models.CASCADE)
    device_id = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"{self.user.username} - {self.device_id}"

class File(models.Model):
    device = models.ForeignKey(Device, related_name='files', on_delete=models.CASCADE)
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name
