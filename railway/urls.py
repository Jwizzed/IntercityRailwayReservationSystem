from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
app_name = 'railway'
urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('signup/', views.signup, name='signup'),
    path('signin/', auth_views.LoginView.as_view(template_name='signin.html'), name='signin'),
    path('reservation/', views.reservation, name='reservation'),
    path('cancel/<uuid:reservation_id>/', views.cancel_reservation,
         name='cancel_reservation'),
    path('routes/', views.all_routes, name='all_routes'),
    path('routes/search/', views.search_route, name='search_route'),
    path('seats/pick/<route_id>/', views.pick_seat, name='pick_seat'),
    path('tickets/', views.ticket_information, name='ticket_information'),
    path('tickets/<ticket_id>/', views.ticket_detail, name='ticket_detail'),
]


