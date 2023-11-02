from django import forms
from .models import Route, Reservation, Station


class RouteSearchForm(forms.Form):
    departure_station = forms.ModelChoiceField(queryset=Station.objects.all())
    terminal_station = forms.ModelChoiceField(queryset=Station.objects.all())
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['ticket', 'from_station', 'to_station']
        widgets = {
            'from_station': forms.HiddenInput(),
            'to_station': forms.HiddenInput(),
            'ticket': forms.HiddenInput(),
        }
