from typing import Any, Dict
from rest_framework import serializers
from .models import Aircraft, Airline

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class AircraftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aircraft
        fields = '__all__'

class AirlineSerializer(serializers.ModelSerializer):
    aircraft_set = AircraftSerializer(many=True, read_only=True)

    class Meta:
        model = Airline
        fields = '__all__'

class CustomTOPSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        data['token'] = data.pop('access')
        return data