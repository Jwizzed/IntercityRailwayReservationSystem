from django import forms
from .models import Route, Reservation, Station, Ticket, Seat, Train


class RouteSearchForm(forms.Form):
    departure_station = forms.ModelChoiceField(queryset=Station.objects.all())
    terminal_station = forms.ModelChoiceField(queryset=Station.objects.all())
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))


class ReservationForm(forms.ModelForm):
    seat = forms.ModelChoiceField(queryset=Seat.objects.none())

    class Meta:
        model = Reservation
        fields = ['seat']

    def __init__(self, *args: object, **kwargs: object) -> object:
        route_id = kwargs.pop('route_id', None)
        super().__init__(*args, **kwargs)
        if route_id:
            route = Route.objects.get(route_id=route_id)
            self.fields['seat'].queryset = Seat.objects.filter(
                train=route.train,
                is_available=True
            )
