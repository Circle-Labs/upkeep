from django.shortcuts import render
from reminders.models import Person, Contact
from rest_framework import viewsets
from reminders.serializers import PersonSerializer, ContactSerializer

# Create your views here.

class PersonViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class ContactViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer