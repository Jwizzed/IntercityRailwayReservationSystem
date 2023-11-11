from django import forms
from .models import Route, Reservation, Station, Ticket, Seat, Train
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
User = get_user_model()


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
            route = Route.objects.get(id=route_id)
            self.fields['seat'].queryset = Seat.objects.filter(
                train=route.train,
                is_available=True
            )


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email', 'firstname', 'lastname', 'ciz_id', 'phone', 'birthdate')


class CustomUserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class SearchForm(forms.Form):
    query = forms.CharField(required=False, label='Search')
