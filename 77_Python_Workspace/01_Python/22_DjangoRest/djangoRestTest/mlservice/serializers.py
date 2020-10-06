from mlservice.models import Request
from rest_framework import serializers

class RequestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Request
        fields = ('orderNumber', 'requestedDate')