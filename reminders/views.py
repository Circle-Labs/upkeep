from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse

import datetime

from reminders.models import Person, Contact
from rest_framework import viewsets
from reminders.serializers import PersonSerializer, ContactSerializer
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from reminders.forms import AddContactForm

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



def yourContacts(request, pk):
    user = get_object_or_404(Person, pk=pk)
    
    if request.method == 'POST':
        form = AddContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            data = form.cleaned_data
            contact = Contact(name=data['name'], phone=data['phone'], nextReminder=datetime.date.today, frequency=datetime.timedelta(days=4))
            contact.save()
            user.contact_set.add(contact)
            form=AddContactForm()
    else:
        form = AddContactForm()

    
    contacts = user.contact_set.all()

    context = {'contacts': contacts, 'person': user, 'form':form}
    return render(request, 'reminders/contacts.html', context)


def me(request, pk):
    user = get_object_or_404(Person, pk=pk)
    context = {'person': user}
    return render(request, 'reminders/me.html', context)

def update(request):
    return ""

class PersonUpdate(UpdateView):
    model = Person
    fields = ['name', 'email', 'phone']

class PersonCreate(CreateView):
    model = Person
    fields = ['name', 'email', 'phone']
    template_name = 'reminders/create_person_form.html'
    
    def get_success_url(self):
        return reverse('contacts', kwargs={
            'pk': self.object.pk,
        })

# def addContact(request, pk):
#     user = get_object_or_404(Person, pk=pk)
#     nextRem = 
#     freq = 
#     contact = Contact(name=, phone=, nextReminder=nextRem, frequency=freq)
#     user.contact_set.add(contact)