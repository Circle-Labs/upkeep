from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from datetime import timedelta
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from reminders.models import Person, Contact
from rest_framework import viewsets
from reminders.serializers import PersonSerializer, ContactSerializer
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from reminders.forms import AddContactForm, UpdateUserForm, CreateUserForm, CreatePersonForm

from reminders import utils

from reminders import tasks


def home_view(request):
    return render(request, 'reminders/home.html', {})

# ----------------------------
# API View Sets
# ----------------------------


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


# ----------------------------
# Authentication Related Views
# ----------------------------

# Will logout any logined users or send them to the login page
@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('user_login'))

# Will send a sms code to any existing user
# TODO: add fail page if number is not in DB
def verification_view(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('contacts'))

    if request.method == 'POST':
        person = Person.objects.get(phone=request.POST['phone'])
        code = utils.generate_sms_code()
        utils.send_sms_code(person.phone, code)
        person.sms_verify_code = code

        print(code)

        person.save()
        url = reverse('user_verify_code', kwargs={'number':request.POST['phone']})
        return HttpResponseRedirect(url)
    
    return render(request, 'reminders/send_code_form.html', {})

# Takes a supplied number and verification code and attempts to authenticate user
def login_view(request, number):

    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('contacts'))

    if request.method == 'POST':
        person = Person.objects.get(phone=request.POST['phone'])
        user = authenticate(phone=request.POST['phone'], code=request.POST['verify_code'])
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('contacts'))
            else:
                print('not active')
        else:
            print('invalid login')

    context = {'number':number}

    return render(request, 'reminders/login_form.html', context)



# ----------------------------
# New Account Views
# ----------------------------

# Creates new person
def create_person(request):
    user = request.user

    if request.method == 'POST':
        user_form = CreateUserForm(request.POST)
        person_form = CreatePersonForm(request.POST)

        if all((user_form.is_valid(), person_form.is_valid())):
            print(user_form.cleaned_data)
            print(user.username)
            user = user_form.save(commit=False)
            user.username = user_form.cleaned_data['first_name'].lower() + user_form.cleaned_data['last_name'].lower()
            user.save()
            person = person_form.save(commit=False)
            person.user = user
            person.sms_verify_code = 1
            person.save()
            user = authenticate(phone=person.phone, code=1)
            login(request, user)
            return HttpResponseRedirect(reverse('contacts'))
    else:
        user_form = CreateUserForm()
        person_form = CreatePersonForm()

    context = {'user_form':user_form, 'person_form':person_form}
    return render(request, 'reminders/create_person_form.html', context)


# ----------------------------
# Account Edit Views
# ----------------------------


@login_required
def your_contacts(request):
    user = request.user.person
    
    if request.method == 'POST':
        form = AddContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            data = form.cleaned_data 

            now = timezone.localtime(timezone.now())
            res = int(data['update_day']) - now.weekday()
            if res <= 0:
                res += 7
            dif = timedelta(days=res)
            new = now + dif
            new = new.replace(hour=data['update_time'].hour, minute=data['update_time'].minute, second=0, microsecond=0)

            contact = Contact(name=data['name'], phone=data['phone'], next_reminder=new, frequency=timedelta(weeks=1))
            contact.save()
            user.contact_set.add(contact)
            form=AddContactForm()
    else:
        form = AddContactForm()

    
    contacts = user.contact_set.all()

    context = {'contacts': contacts, 'person': user, 'form':form}
    return render(request, 'reminders/contacts.html', context)

@login_required
def declaim_contact(request, contact):
    user = request.user.person
    contact = Contact.objects.get(id=contact)
    user.contact_set.remove(contact)
    contact.delete()
    return HttpResponseRedirect(reverse('contacts'))

def test(request):
    utils.check_reminders()
    print('ok')
    return HttpResponseRedirect(reverse('contacts'))

@login_required
def update_person(request):
    user = request.user.person

    if request.method == 'POST':
        form = UpdateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('me'))
    else:
        form = UpdateUserForm(instance=user)

    return render(request, 'reminders/person_form.html', {'person_form': form})


# class PersonCreate(CreateView):
#     form_class = UpdateUserForm
#     fields = ['name', 'email', 'phone']
#     template_name = 'reminders/create_person_form.html'
    
#     def get_success_url(self):
#         return reverse('contacts', kwargs={
#             'pk': self.object.pk,
#         })

# def addContact(request, pk):
#     user = get_object_or_404(Person, pk=pk)
#     nextRem = 
#     freq = 
#     contact = Contact(name=, phone=, nextReminder=nextRem, frequency=freq)
#     user.contact_set.add(contact)