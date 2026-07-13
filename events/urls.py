# URLs.py is used for routing the requests to the appropriate views. It defines the URL patterns that map to the views in the application. 
# In simpler terms, it acts as a traffic controller, directing incoming requests to the correct view based on the URL.
from django.urls import path
from .views import EventListCreateView, EventDetailView, RegistrationListCreateView, RegistrationDetailView

urlpatterns = [
    path('events/', EventListCreateView.as_view(), name='event-list-create'),
    path('events/<int:pk>/', EventDetailView.as_view(), name='event-detail'),
    path('registrations/', RegistrationListCreateView.as_view(), name='registration-list-create'),
    path('registrations/<int:pk>/', RegistrationDetailView.as_view(), name='registration-detail'),
]