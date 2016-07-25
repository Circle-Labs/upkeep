from random import randint
from twilio.rest import TwilioRestClient
from twilio import TwilioRestException
import phonenumbers
import keys

from reminders.models import Contact, Person
from django.utils import timezone
from datetime import timedelta

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives

def generate_sms_code():
	return randint(10000, 99999)

client = TwilioRestClient(keys.USE_TWILIO_ACCOUNT, keys.USE_TWILIO_TOKEN)


def send_email(to, subject, message):
	if hasattr(keys, 'SENDGRID_DEBUG') and keys.SENDGRID_DEBUG:
		print "Debug: Send email '" + subject + "'' to " + str(to) + " with message: " + message
	else:
		send_mail(subject, message, "Hello <hello@upkeepme.co>", to)

def send_beta_accept(to):
	send_email(to, "Welcome!", "Hi! We are happy to have you come on board for our closed beta. You can now go to upkeepme.co/user/create and create an account with this email address.")

def send_beta_acknowledge(to):
	send_email([to], "Beta Registration", "Hi! This is just to confirm that we have registered you for updates about our closed beta. Be on the look out for more!")

def send_sms(to, message):
	try:
		print("start send")
		message = client.messages.create(to=to, from_=keys.USE_TWILIO_NUMBER, body=message)
		print("end send")
	except TwilioRestException as e:
		print("Error")
		print(e)

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
			send_contact_reminder(contact.person_set.all()[0].phone, contact.name, contact.phone)
			contact.next_reminder = contact.next_reminder + contact.frequency
			contact.save()

def populate_contacts():
	now = timezone.now()
	diff = timedelta(hours=1)
	me = Person.objects.get(pk=1)
	for i in range(0, 100):
		contact = Contact(name="New" + str(i), phone="1231231221", next_reminder=now+diff, frequency=timedelta(weeks=1))
		now = now + diff
		contact.save()
		me.contact_set.add(contact)

def parse_phone_number(number):
	print(number)
	# parses number as dialed from US (localizes numbers with country code)
	try:
		x = phonenumbers.parse(number, "US")
	except:
		print("Phone # parsing error")
		return "1"
	# checks validity
	if not phonenumbers.is_possible_number(x):
		print("Phone # is not possible number")
		return "1"
	if not phonenumbers.is_valid_number(x):
		print("Phone # is not valid number")
		return "1"
	# returns standarized number with forced country code
	return phonenumbers.format_number(x, phonenumbers.PhoneNumberFormat.E164)
	
