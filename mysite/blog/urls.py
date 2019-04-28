from django.urls import path,include
from . import views

urlpatterns = [
	path('', views.main_page, name = 'main_page'),
    path('clients/', views.client_list, name='client_list'),
    path('clients/new/', views.client_new, name='client_new'),
    path('clients/<pk>/', views.client_detail, name='client_detail'),
    path('clients/<pk>/edit/', views.client_edit, name='client_edit'),
    path('clients/<pk>/remove/', views.client_remove, name='client_remove'),
    path('client/<pk>/comment/', views.add_comment_to_client, name='add_comment_to_client'),
    path('rooms/', views.room_list, name='room_list'),
    path('rooms/new/', views.room_new, name='room_new'),
    path('managers/', views.managers, name= 'managers'),
    path('booking/', views.booking_list, name = 'booking_list'),
    path('booking/new/', views.booking_new, name='booking_new'),
    path('booking/<pk>/', views.booking_detail, name='booking_detail'),
    path('booking/<pk>/edit/', views.booking_edit, name='booking_edit'),
    path('booking/<pk>/remove/', views.booking_remove, name='booking_remove'),
    path('manager/<pk>/', views.manager_detail, name='manager_detail'),
    path('manager/<pk>/remove/', views.manager_remove, name='manager_remove'),
    path('rooms/<pk>/', views.room_detail, name='room_detail'),
    path('rooms/<pk>/manager/', views.add_manager_to_room, name='add_manager_to_room'),
    path('rooms/<pk>/remove/', views.room_remove, name='room_remove'),
    path('rooms/<pk>/edit/', views.room_edit, name='room_edit'),
    path('search/', views.search, name='search'),
]
