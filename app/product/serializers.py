from rest_framework import serializers
from app.product.models import DisplayCode, Points


class DisplayCodeSerializer(serializers.ModelSerializer):

    class Meta:
        model = DisplayCode
        fields = '__all__'


class PointsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Points
        fields = '__all__'


