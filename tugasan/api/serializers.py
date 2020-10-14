from rest_framework.authtoken.models import Token
from rest_framework import serializers

from tugasan.models import UntukBeli

class UntukBeliSerializer(serializers.ModelSerializer):
    class Meta:
        model = UntukBeli
        fields = "__all__"

