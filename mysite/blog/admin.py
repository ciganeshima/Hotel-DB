from django.contrib import admin
from .models import Client, Room, Manager,Booking, Comment

admin.site.register(Client)
admin.site.register(Room)
admin.site.register(Manager)
admin.site.register(Booking)
admin.site.register(Comment)