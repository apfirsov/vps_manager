from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, viewsets, status
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response

from vps.models import VirtualPrivateServer
from .serializers import (
    VirtualPrivateServerSerializer, ChangeStatusVPSSerializer
)


class CreateRetrieveListViewSet(mixins.CreateModelMixin,
                                mixins.RetrieveModelMixin,
                                mixins.ListModelMixin,
                                viewsets.GenericViewSet):
    """Custom view set, only allowed: create, retrieve and get list."""
    pass


class VirtualPrivateServerViewSet(CreateRetrieveListViewSet):
    """VirtualPrivateServer view set."""

    lookup_field = 'uid'
    queryset = VirtualPrivateServer.objects.all()
    serializer_class = VirtualPrivateServerSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('cpu', 'ram', 'hdd', 'status')

    def get_serializer_class(self):
        if self.action == 'change_status':
            return ChangeStatusVPSSerializer
        return super().get_serializer_class()

    @action(methods=['POST'], detail=True)
    def change_status(self, request, uid=None):
        vps = get_object_or_404(VirtualPrivateServer, uid=uid)
        serializer = self.get_serializer(data=request.data, instance=vps)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
