from typing import Any, Dict
from rest_framework import serializers
from .models import Aircraft, Airline

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class AircraftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aircraft
        fields = ['url', "manufacturer_serial_number", "type", "model", "operator_airline", "number_of_engines"]

class AirlineSerializer(serializers.ModelSerializer):
    aircraft_set = AircraftSerializer(many=True, read_only=True)

    class Meta:
        model = Airline
        fields = ['url', 'name', 'callsign', 'founded_year', 'base_airport', 'aircraft_set']

class CustomTOPSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        data['token'] = data.pop('access')
        return data