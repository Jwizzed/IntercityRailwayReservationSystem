from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.utils import timezone
from .models import Station, Route, Reservation, Ticket, Train
from .forms import RouteSearchForm, ReservationForm
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .forms import ReservationForm
from .models import Route
from .forms import CustomUserCreationForm, CustomUserLoginForm, SearchForm



def main_page(request):
    return render(request, 'main_page.html')


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('railway:main_page')
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})


def signin(request):
    if request.method == 'POST':
        form = CustomUserLoginForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('railway:main_page')
    else:
        form = CustomUserLoginForm()
    return render(request, 'signin.html', {'form': form})


def all_routes(request):
    search_form = SearchForm(request.GET or None)
    if search_form.is_valid():
        query = search_form.cleaned_data.get('query', '')
        routes = Route.objects.filter(route_name__icontains=query)
    else:
        routes = Route.objects.all()
    now = timezone.now()
    return render(request, 'routes_list.html', {'routes': routes, 'now': now, 'search_form': search_form})


def all_stations(request):
    search_form = SearchForm(request.GET or None)
    if search_form.is_valid():
        query = search_form.cleaned_data.get('query', '')
        stations = Station.objects.filter(station_name__icontains=query)
    else:
        stations = Station.objects.all()

    return render(request, 'stations_list.html',
                  {'stations': stations, 'search_form': search_form})


def all_trains(request):
    search_form = SearchForm(request.GET or None)
    if search_form.is_valid():
        query = search_form.cleaned_data.get('query', '')
        trains = Train.objects.filter(train_type_str__icontains=query)
    else:
        trains = Train.objects.all()

    return render(request, 'trains_list.html',
                  {'trains': trains, 'search_form': search_form})

@login_required
def reservation(request):
    if request.method == 'POST':
        form = RouteSearchForm(request.POST)
        if form.is_valid():
            departure_station = form.cleaned_data['departure_station']
            terminal_station = form.cleaned_data['terminal_station']
            date = form.cleaned_data['date']

            routes = Route.objects.filter(
                departure_station=departure_station,
                terminal_station=terminal_station,
                departure_time__date=date
            )
            now = timezone.now()
            return render(request, 'routes_list.html', {'routes': routes, 'now': now})
    else:
        form = RouteSearchForm()

    return render(request, 'reservation.html', {'form': form})


@login_required
def cancel_reservation(request, reservation_id):
    try:
        reservation = Reservation.objects.get(id=reservation_id, passenger=request.user)
        ticket = reservation.ticket
        seat = ticket.seat
        seat.is_available = True
        seat.save()
        reservation.delete()
        return redirect('railway:ticket_information')
    except Reservation.DoesNotExist:
        return redirect('railway:main_page')


@login_required
def search_route(request):
    if request.method == 'GET':
        form = RouteSearchForm(request.GET)
        if form.is_valid():
            departure_station = form.cleaned_data['departure_station']
            terminal_station = form.cleaned_data['terminal_station']
            date = form.cleaned_data['date']

            routes = Route.objects.filter(
                departure_station=departure_station,
                terminal_station=terminal_station,
                departure_time__date=date
            )
            now = timezone.now()
            return render(request, 'routes_list.html', {'routes': routes, 'form': form, 'now': now})
    else:
        form = RouteSearchForm()

    return render(request, 'reservation.html', {'form': form})


@login_required
def pick_seat(request, route_id):
    route = get_object_or_404(Route, pk=route_id)

    if request.method == 'POST':
        form = ReservationForm(request.POST, route_id=route_id)

        if form.is_valid():
            selected_seat = form.cleaned_data['seat']
            if not selected_seat.is_available:
                return JsonResponse({'status': 'error', 'message': 'Seat not available'})

            selected_seat.is_available = False
            selected_seat.save()

            ticket = Ticket.objects.create(
                route=route,
                seat=selected_seat,
                price=0
            )

            Reservation.objects.create(
                passenger=request.user,
                ticket=ticket,
                from_station=route.departure_station,
                to_station=route.terminal_station,
            )

            return redirect('railway:ticket_detail', ticket_id=ticket.id)
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors})

    form = ReservationForm(route_id=route_id)
    return render(request, 'pick_seat.html', {'form': form, 'route_id': route_id})


@login_required
def ticket_information(request):
    tickets = Reservation.objects.filter(passenger=request.user)
    return render(request, 'ticket_information.html', {'tickets': tickets})


@login_required
def ticket_detail(request, ticket_id):
    try:
        reservation = Reservation.objects.get(ticket__id=ticket_id)
    except Reservation.DoesNotExist:
        return redirect('railway:main_page')

    return render(request, 'ticket_detail.html', {'reservation': reservation})

