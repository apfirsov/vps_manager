from rest_framework import serializers
from vps.models import VirtualPrivateServer


class VirtualPrivateServerSerializer(serializers.ModelSerializer):
    """VPS model serializer."""

    class Meta:
        model = VirtualPrivateServer
        fields = ('uid', 'cpu', 'ram', 'hdd', 'status')
        read_only_fields = ('uid', 'status')


class ChangeStatusVPSSerializer(serializers.ModelSerializer):
    """Change status VPS serializer."""

    status = serializers.ChoiceField(
        choices=VirtualPrivateServer.STATUS_CHOICES,
        required=True
    )

    class Meta:
        model = VirtualPrivateServer
        fields = ('uid', 'cpu', 'ram', 'hdd', 'status')
        read_only_fields = ('uid', 'cpu', 'ram', 'hdd')
