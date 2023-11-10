from django import forms
from .models import Route, Reservation, Station, Ticket


class RouteSearchForm(forms.Form):
    departure_station = forms.ModelChoiceField(queryset=Station.objects.all())
    terminal_station = forms.ModelChoiceField(queryset=Station.objects.all())
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))


class ReservationForm(forms.ModelForm):
    ticket = forms.ModelChoiceField(queryset=Ticket.objects.none())

    class Meta:
        model = Reservation
        fields = ['ticket', 'from_station', 'to_station']
        widgets = {
            'from_station': forms.HiddenInput(),
            'to_station': forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        route_id = kwargs.pop('route_id', None)
        super().__init__(*args, **kwargs)
        if route_id:
            self.fields['ticket'].queryset = Ticket.objects.filter(
                route_id=route_id,
                seat__is_available=True
            )
