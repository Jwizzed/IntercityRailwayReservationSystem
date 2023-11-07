from django.urls import path, include
from . import views
app_name = 'railway'
urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('routes/search/', views.search_route, name='search_route'),
    path('seats/pick/<int:route_id>/', views.pick_seat, name='pick_seat'),
    path('tickets/', views.ticket_information, name='ticket_information'),
    path('tickets/<int:ticket_id>/', views.ticket_detail, name='ticket_detail'),
    path('reservation/create/<int:route_id>/', views.create_reservation, name='create_reservation'),
]
