from rest_framework import filters, mixins, viewsets, status
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

    @action(methods=['POST',], detail=True)
    def change_status(self, request, uid=None):
        vps = get_object_or_404(VirtualPrivateServer, uid=uid)
        serializer = ChangeStatusVPSSerializer(data=request.data, instance=vps)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
