from django.db import models


class Airline(models.Model):
    name = models.CharField(max_length=100)
    callsign = models.CharField(max_length=100)
    founded_year = models.IntegerField()
    base_airport = models.CharField(max_length=100)

class Airport(models.Model):
    manufacturer_serial_number = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    operator_airline = models.ForeignKey(Airline, on_delete=models.SET_NULL, null=True)
    number_of_engines = models.IntegerField()
