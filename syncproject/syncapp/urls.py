from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DeviceViewSet, FileUploadViewSet

router = DefaultRouter()
router.register(r'devices', DeviceViewSet)
router.register(r'uploads', FileUploadViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
