from django.core.validators import MinValueValidator
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

from django.db import models


class Passenger(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True)
    passport_number = models.CharField(max_length=9, blank=True)
    age = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"Passenger {self.username}"


class Station(models.Model):
    st_id = models.CharField(primary_key=True, max_length=255)
    station_name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    sub_dist = models.CharField(max_length=255)

    def __str__(self):
        return self.station_name


class Train(models.Model):
    train_id = models.CharField(primary_key=True, max_length=255)
    train_type = models.CharField(max_length=255)
    manufacture_year = models.IntegerField(validators=[MinValueValidator(1900)])

    def __str__(self):
        return f"{self.train_type} - {self.train_id}"


class Route(models.Model):
    route_id = models.CharField(primary_key=True, max_length=255)
    departure_station = models.ForeignKey(Station, on_delete=models.CASCADE, related_name='departing_routes')
    terminal_station = models.ForeignKey(Station, on_delete=models.CASCADE, related_name='arriving_routes')
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    route_name = models.CharField(max_length=255)
    train = models.ForeignKey(Train, on_delete=models.CASCADE)

    def __str__(self):
        return self.route_name


class Ticket(models.Model):
    ticket_id = models.CharField(primary_key=True, max_length=255)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    price = models.IntegerField(validators=[MinValueValidator(0)])

    def __str__(self):
        return f"{self.ticket_id}"


class Reservation(models.Model):
    rev_id = models.CharField(primary_key=True, max_length=255)
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    rev_date = models.DateTimeField(default=timezone.now)
    from_station = models.ForeignKey(Station, on_delete=models.CASCADE, related_name='reservations_from_station')
    to_station = models.ForeignKey(Station, on_delete=models.CASCADE, related_name='reservations_to_station')

    def __str__(self):
        return f"Reservation {self.rev_id} by {self.passenger.name}"
