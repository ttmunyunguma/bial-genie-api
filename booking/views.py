from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from . import serializers, models


class BookingsView(APIView):
    permission_classes = [IsAuthenticated, ]

    def get(self, request, *args, **kwargs):
        return Response({'success': 'Booking Works'}, status=status.HTTP_200_OK)


class LocationView(generics.ListAPIView):
    serializer_class = serializers.LocationSerializer
    queryset = models.Location.objects.all()


class FlightView(generics.ListAPIView):
    serializer_class = serializers.FlightSerializer
    queryset = models.Flight.objects.all()

