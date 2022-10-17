from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import VirtualPrivateServerViewSet


router = DefaultRouter()
router.register('vps', VirtualPrivateServerViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]
