from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Station, Route, Reservation, Ticket
from .forms import RouteSearchForm, ReservationForm
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .forms import ReservationForm
from .models import Route


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
            print(routes)
            return render(request, 'routes_list.html', {'routes': routes, 'form': form})
    else:
        form = RouteSearchForm()

    return render(request, 'main_page.html', {'form': form})


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
    reservation = get_object_or_404(Reservation, ticket__ticket_id=ticket_id, user=request.user)
    return render(request, 'ticket_detail.html', {'reservation': reservation})

