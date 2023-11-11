from django.core.validators import MinValueValidator
from django.contrib.auth.models import AbstractUser
from django.core.validators import EmailValidator
from django.utils import timezone

from django.db import models
import uuid


class AbstractModel(models.Model):
    """Abstract model class for generate unique id for each model."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        """Meta definition for Model."""

        abstract = True

    def __str__(self):
        """Unicode representation of Model."""
        return str(self.id)


class Passenger(AbstractUser, AbstractModel):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    ciz_id = models.CharField(max_length=9, blank=True)
    email = models.EmailField(validators=[EmailValidator])
    phone = models.CharField(max_length=15, blank=True)
    birthdate = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"


class Station(AbstractModel):
    station_name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    sub_dist = models.CharField(max_length=255)

    def __str__(self):
        return self.station_name


class Train(AbstractModel):
    train_type_str = models.CharField(max_length=255)
    manufacture_year = models.IntegerField(validators=[MinValueValidator(1900)])

    def __str__(self):
        return f"{self.train_type_str} - {self.id}"


class Seat(AbstractModel):
    train = models.ForeignKey(Train, on_delete=models.CASCADE, related_name='seats')
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"Seat {self.id} on train {self.train.id}"


class Route(AbstractModel):
    departure_station = models.ForeignKey(Station, on_delete=models.CASCADE, related_name='departing_routes')
    terminal_station = models.ForeignKey(Station, on_delete=models.CASCADE, related_name='arriving_routes')
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    route_name = models.CharField(max_length=255)
    train = models.ForeignKey(Train, on_delete=models.CASCADE)

    def __str__(self):
        return self.route_name


class Ticket(AbstractModel):
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    price = models.IntegerField(validators=[MinValueValidator(0)])
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id}"


class Reservation(AbstractModel):
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    rev_date = models.DateTimeField(default=timezone.now)
    from_station = models.ForeignKey(Station, on_delete=models.CASCADE, related_name='reservations_from_station')
    to_station = models.ForeignKey(Station, on_delete=models.CASCADE, related_name='reservations_to_station')

    def __str__(self):
        return f"Reservation {self.id} by {self.passenger.firstname}"
