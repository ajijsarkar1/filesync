from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, DeviceViewSet, FileViewSet, UserSessionView

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'devices', DeviceViewSet)
router.register(r'files', FileViewSet)
router.register(r'user_sessions', UserSessionView, basename='user_sessions')

urlpatterns = [
    path('', include(router.urls)),
]
