from rest_framework import serializers

from . import models


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Location
        fields = '__all__'


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Flight
        fields = '__all__'

