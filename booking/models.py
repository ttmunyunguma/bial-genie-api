from datetime import datetime

from django.db import models


class Location(models.Model):
    city_name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    city_code = models.CharField(max_length=255)

    def __str__(self):
        return self.city_code


class Flight(models.Model):
    from_location = models.OneToOneField(Location, on_delete=models.CASCADE, related_name='from_location')
    to_destination = models.OneToOneField(Location, on_delete=models.CASCADE, related_name='to_destination')
    aircraft = models.CharField(max_length=255)
    flight_code = models.CharField(max_length=255)
    departure_date = models.DateTimeField()
    price_economy = models.CharField(max_length=255)
    price_business = models.CharField(max_length=255)
    price_first_class = models.CharField(max_length=255)
    max_capacity_economy = models.IntegerField()
    max_capacity_business = models.IntegerField()
    max_capacity_first_class = models.IntegerField()

    def __str__(self):
        return self.flight_code


class Booking(models.Model):
    departure_flight = models.OneToOneField(Flight, on_delete=models.CASCADE, related_name='departure_flight')
    return_flight = models.OneToOneField(Flight, on_delete=models.CASCADE, related_name='return_flight', null=True)

    def __str__(self):
        return self.departure_flight 


class Passenger(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)



