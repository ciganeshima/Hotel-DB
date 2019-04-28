from django.shortcuts import render, get_object_or_404
from .models import Client,Room,Manager,Booking
from django.views.generic import ListView
from .forms import ClientForm, RoomForm, ManagerForm, BookingForm, CommentForm
from functools import reduce
import re
from django.shortcuts import redirect
from django.db.models import Q, Max, Min, Avg, Count
from django.views.generic import View
from .forms import SearchEngineForm

# Create your views here.
def main_page(request):
    count_room = Room.objects.count()
    return render(request, 'blog/main_page.html', {'count_room' : count_room})

def client_list(request):
    clients = Client.objects.order_by('fio')
    count_clients = Client.objects.count()
    return render(request, 'blog/client_list.html', {'clients':clients, 'count_clients': count_clients} )

def client_new(request):
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            client = form.save(commit=False)
            client.save()
            return redirect('client_detail', pk = client.pk)
    else:
        form = ClientForm()
    return render(request, 'blog/client_edit.html', {'form': form})

def client_detail(request, pk):
    client = get_object_or_404(Client, pk=pk)
    return render(request, 'blog/client_detail.html', {'client': client})

def client_remove(request, pk):
    client = get_object_or_404(Client, pk=pk)
    client.delete()
    return redirect('client_list')

def client_edit(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == "POST":
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            client = form.save(commit=False)
            client.save()
            return redirect('client_detail', pk=client.pk)
    else:
        form = ClientForm(instance=client)
    return render(request, 'blog/client_edit.html', {'form': form})

def room_list(request):
    max_price = Room.objects.all().aggregate(Max('price'))['price__max']
    need = Room.objects.get(price = max_price)
    min_price = Room.objects.all().aggregate(Min('price'))['price__min']
    minimum = Room.objects.get(price = min_price)
    average = Room.objects.all().aggregate(Avg('price'))['price__avg']
    lux =  Room.objects.filter(room_type = 'Lux').count()
    standart = Room.objects.filter(room_type= 'Standart').count()
    free =  Room.objects.filter(status = 'Yes').count()
    rooms = Room.objects.order_by('number')
    return render(request, 'blog/room_list.html', {'rooms':rooms, 'need' : need, 'minimum' : minimum, 'average' : average, 'free' : free, 'lux':lux, 'standart':standart} )

def room_detail(request, pk):
    room = get_object_or_404(Room, pk=pk)
    return render(request, 'blog/room_detail.html', {'room': room})

def room_new(request):
    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            room = form.save(commit=False)
            room.save()
            return redirect('room_detail', pk = room.pk)
    else:
        form = RoomForm()
    return render(request, 'blog/room_edit.html', {'form': form})

def room_remove(request, pk):
    room = get_object_or_404(Room, pk=pk)
    room.delete()
    return redirect('room_list')

def room_edit(request, pk):
    room = get_object_or_404(Room, pk=pk)
    if request.method == "POST":
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            room = form.save(commit=False)
            room.save()
            return redirect('room_detail', pk=room.pk)
    else:
        form = RoomForm(instance=room)
    return render(request, 'blog/room_edit.html', {'form': form})

def max(request):
    max_price = Room.objects.all().aggregate(Max('price'))['price__max']
    need = Room.objects.get(price = max_price)

def search(request):
    if 'search' in request.GET:
        search = request.GET['search']
        if not search:
            error = True
        else:
            rooms = Room.objects.filter(status__icontains = search)
            return render(request, 'blog/search.html', {'rooms' : rooms, 'search':search})

def managers(request):
    managers = Manager.objects.order_by('manager_name')
    max_salary = Manager.objects.all().aggregate(Max('salary'))['salary__max']
    need = Manager.objects.get(salary = max_salary)
    return render(request, 'blog/managers.html', {'managers':managers,'need' : need})

def add_manager_to_room(request, pk):
    room = get_object_or_404(Room, pk=pk)
    if request.method == "POST":
        form = ManagerForm(request.POST)
        if form.is_valid():
            manager = form.save(commit=False)
            manager.room = room
            manager.save()
            return redirect('room_detail', pk=room.pk)
    else:
        form = ManagerForm()
    return render(request, 'blog/add_manager_to_room.html', {'form': form})

def manager_remove(request, pk):
    manager = get_object_or_404(Manager, pk=pk)
    manager.delete()
    return redirect('room_detail', pk=manager.room.pk)

def manager_detail(request, pk):
    manager = get_object_or_404(Manager, pk=pk)
    return render(request, 'blog/manager_detail.html', {'manager': manager})

def booking_list(request):
    bookings = Booking.objects.order_by('number')
    count_bookings = Booking.objects.count()
    lux =  Booking.objects.filter(book_room_type = 'Lux').count()
    standart = Booking.objects.filter(book_room_type= 'Standart').count()
    return render(request, 'blog/booking_list.html', {'bookings':bookings, 'count_bookings': count_bookings, 'lux' : lux, 'standart' : standart} )

def booking_new(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.save()
            return redirect('booking_detail', pk = booking.pk)
    else:
        form = BookingForm()
    return render(request, 'blog/booking_edit.html', {'form': form})

def booking_detail(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    return render(request, 'blog/booking_detail.html', {'booking': booking})

def booking_remove(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    booking.delete()
    return redirect('booking_list')

def booking_edit(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    if request.method == "POST":
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.save()
            return redirect('booking_detail', pk=booking.pk)
    else:
        form = BookingForm(instance=booking)
    return render(request, 'blog/booking_edit.html', {'form': form})

def add_comment_to_client(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.client = client
            comment.save()
            return redirect('client_detail', pk=client.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_client.html', {'form': form})