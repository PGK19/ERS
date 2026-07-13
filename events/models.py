# Models.py is used for defining the structure of the database tables. It contains classes that represent the data models in the application. In this case, it is used to define the Event and registration models, which will be used to store the details of the events and the registrations made by the users for those events.
# In simpler terms, it acts as a blueprint for the database, specifying what data will be stored and how it will be organized. Like a class in OOPs concept.

from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    venue = models.CharField(max_length=100)
    time = models.DateTimeField()
    fee = models.DecimalField(max_digits=10, decimal_places=2)
    seats = models.PositiveIntegerField()

#registration model must be created to store the registration details of the users for the events. It should have a foreign key to the Event model and a foreign key to the User model (from django.contrib.auth.models import User). The registration model should also have a field to store the number of seats booked by the user.

class Registration(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    seats_booked = models.PositiveIntegerField()
    status = models.CharField(max_length=20, choices=[('confirmed', 'Confirmed'), ('pending', 'Pending'), ('cancelled', 'Cancelled')], default = 'pending')
    timestamp = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=20, choices=[('paid', 'Paid'), ('unpaid', 'Unpaid')],default = 'unpaid')
    