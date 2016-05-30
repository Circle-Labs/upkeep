from random import randint
from twilio.rest import TwilioRestClient
import keys

from reminders.models import Contact, Person
from django.utils import timezone
from datetime import timedelta

def generate_sms_code():
	return randint(10000, 99999)

client = TwilioRestClient(keys.TWILIO_ACCOUNT, keys.TWILIO_TOKEN)


def send_sms(to, message):
	format_to = '+1' + to
	message = client.messages.create(to=format_to, from_=keys.TWILIO_NUMBER, body=message)
	print(message.status)


def send_sms_code(to, code):
	send_sms(to, 'Your code is: ' + str(code))

def send_contact_reminder(to, contact_name, contact_number):
	send_sms(to, 'Don\'t forget to keep in touch with ' + contact_name +'. Here\'s the number: ' + contact_number + ' . Say Hi, ask them about their day, or try out that joke you\'ve been practicing. Good luck!')

def check_reminders():
	contacts = Contact.objects.all()
	now = timezone.now()
	duration = timedelta(minutes=16)
	for contact in contacts:
		dif = contact.next_reminder - now - duration
		if dif <= timedelta():
			send_contact_reminder(contact.user_set.all()[0].phone, contact.name, contact.phone)

def populate_contacts():
	now = timezone.now()
	diff = timedelta(hours=1)
	me = Person.objects.get(pk=1)
	for i in range(0, 100):
		contact = Contact(name="New" + str(i), phone="1231231221", next_reminder=now+diff, frequency=timedelta(weeks=1))
		now = now + diff
		contact.save()
		me.contact_set.add(contact)
