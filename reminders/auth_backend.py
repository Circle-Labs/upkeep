from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User
from reminders.models import Person

class SMSAuthBackend(ModelBackend):
	"""
	Log in to Django with a provided sms verifcation code
	"""
	def authenticate(self, phone=None, code=None):
		try:
			person = Person.objects.get(phone=phone)
			user = person.user
			if (person.sms_verify_code == int(code)):
				person.sms_verify_code = None
				person.save()
				return user
			else:
				print('failed sms')
				return None
		except Person.DoesNotExist:
			print('person dne')
			return None

	def get_user(self, user_id):
		try:
			return User.objects.get(pk=user_id)
		except User.DoesNotExist:
			return None