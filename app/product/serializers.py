from rest_framework import serializers
from app.product.models import TelegramUsers, DeviceSignals


class TelegramUsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = TelegramUsers
        fields = '__all__'


class DeviceSignalsSerializer(serializers.ModelSerializer):

    class Meta:
        model = DeviceSignals
        fields = '__all__'

