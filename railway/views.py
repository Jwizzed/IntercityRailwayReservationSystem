from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Station, Route, Reservation, Ticket
from .forms import RouteSearchForm, ReservationForm
from django.http import JsonResponse


def signup(request):
    print('signup method', request.method)
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

            login(request, user)
            return redirect('railway:main_page')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


@login_required
def main_page(request):
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
            return render(request, 'routes_list.html', {'routes': routes})
    else:
        form = RouteSearchForm()

    return render(request, 'main_page.html', {'form': form})


def search_route(request):
    # ...
    pass


@login_required
def pick_seat(request, route_id):
    route = get_object_or_404(Route, pk=route_id)
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.route = route
            reservation.save()
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors})

    form = ReservationForm(initial={'from_station': route.departure_station, 'to_station': route.terminal_station})
    return render(request, 'pick_seat.html', {'form': form, 'route_id': route_id})


@login_required
def ticket_information(request):
    tickets = Reservation.objects.filter(user=request.user)
    return render(request, 'ticket_information.html', {'tickets': tickets})


@login_required
def ticket_detail(request, ticket_id):
    reservation = get_object_or_404(Reservation, ticket__ticket_id=ticket_id, user=request.user)
    return render(request, 'ticket_detail.html', {'reservation': reservation})


@login_required
def create_reservation(request, route_id):
    route = get_object_or_404(Route, pk=route_id)
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.route = route
            reservation.save()
            return redirect('ticket_detail', ticket_id=reservation.ticket.ticket_id)
    else:
        form = ReservationForm(initial={'from_station': route.departure_station, 'to_station': route.terminal_station})
    return render(request, 'pick_seat.html', {'form': form, 'route_id': route_id})
