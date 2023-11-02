from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Station, Route, Reservation, Ticket
from .forms import RouteSearchForm, ReservationForm
from django.http import JsonResponse

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('main_page')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


@login_required
def main_page(request):
    if request.method == 'POST':
        form = RouteSearchForm(request.POST)
        if form.is_valid():
            # Extract information from form
            departure_station = form.cleaned_data['departure_station']
            terminal_station = form.cleaned_data['terminal_station']
            date = form.cleaned_data['date']

            # Fetch the routes based on form data
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
    # This might be handled within the main_page view above, triggered by POST request.
    # But if you want an AJAX-based search, you would use this view to return data for updating the table asynchronously.
    # ...
    pass


def pick_seat(request, route_id):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.passenger = request.user.passenger
            reservation.route_id = route_id
            reservation.save()
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors})

    form = ReservationForm()
    return render(request, 'pick_seat.html',
                  {'form': form, 'route_id': route_id})


@login_required
def ticket_information(request):
    tickets = request.user.passenger.reservation_set.all()
    return render(request, 'ticket_information.html', {'tickets': tickets})


@login_required
def ticket_detail(request, ticket_id):
    reservation = Reservation.objects.get(ticket__ticket_id=ticket_id)
    return render(request, 'ticket_detail.html', {'reservation': reservation})
