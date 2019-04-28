from django import forms

from .models import Client, Room, Manager, Booking, Comment

class ClientForm(forms.ModelForm):

    class Meta:
        model = Client
        fields = ('fio', 'pasport', 'reg_town', 'telephone')

class RoomForm(forms.ModelForm):

    class Meta:
        model = Room
        fields = ('number', 'room_type', 'places', 'status', 'price', 'status')

class SearchEngineForm(forms.Form):
    client = forms.ChoiceField()
 
    def __init__(self, *args, **kwargs):
        super(SearchEngineForm, self).__init__(*args, **kwargs)
        clientss = Client.objects.all().order_by('fio')
        for client in clientss:
            self.fields['client'].widget.choices.append((str(client.telephone), str(client)))

class ManagerForm(forms.ModelForm):

    class Meta:
        model = Manager
        fields = ('manager_name', 'salary', 'age',)

class BookingForm(forms.ModelForm):

    class Meta:
        model = Booking
        fields = ('number' , 'created_date' , 'book_room_type', 'book_room_places', 'arrival_date' , 'tenure',)

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('topic', 'text',)


