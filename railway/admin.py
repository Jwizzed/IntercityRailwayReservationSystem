from django.contrib import admin

from .models import Station, Train, Route, Ticket, Reservation, Passenger, Seat

admin.site.register(Passenger)
admin.site.register(Station)
admin.site.register(Train)
admin.site.register(Route)
admin.site.register(Ticket)
admin.site.register(Reservation)
admin.site.register(Seat)
