from django.db import models
from django.utils import timezone


class Client(models.Model):
    fio = models.CharField(max_length=200)
    pasport = models.CharField(max_length=50)
    reg_town = models.CharField(max_length=50)
    telephone = models.CharField(max_length=50)

    def publish(self):
        self.save()

    def __str__(self):
        return self.fio

class Room(models.Model):
	number = models.CharField(max_length=20)
	room_type = models.CharField(max_length=50)
	places = models.CharField(max_length=10)
	status = models.CharField(max_length=5)
	price = models.CharField(max_length=50)

	def publish(self):
		self.save()

	def __str__(self):
		return self.number

class Manager(models.Model):
    room = models.ForeignKey('blog.Room', on_delete=models.CASCADE, related_name='manager')
    manager_name = models.CharField(max_length=200)
    salary = models.CharField(max_length=50)
    age = models.CharField(max_length=5)

    def approve(self):
        self.save()

    def __str__(self):
        return self.manager_name

class Booking(models.Model):
	number = models.CharField(max_length=50)
	created_date = models.DateTimeField(default=timezone.now)
	book_room_type = models.CharField(max_length=50)
	book_room_places = models.CharField(max_length=10)
	arrival_date = models.DateTimeField(default=timezone.now)
	tenure = models.CharField(max_length=20)

	def publish(self):
		self.save()

	def __str__(self):
		return self.number

class Comment(models.Model):
    client = models.ForeignKey('blog.Client', on_delete=models.CASCADE, related_name='comments')
    topic = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def approve(self):
        self.save()

    def __str__(self):
        return self.text