from django import forms
from reminders.models import Contact, Person
from django.contrib.auth.models import User
from reminders import utils

DAY_CHOICES = (
	(0, 'Monday'),
	(1, 'Tuesday'),
	(2, 'Wednesday'),
	(3, 'Thursday'),
	(4, 'Friday'),
	(5, 'Saturday'),
	(6, 'Sunday'))

class AddContactForm(forms.ModelForm):
	update_time = forms.TimeField(label="Time to be reminded at (Eastern Time)", initial='14:00')
	update_day = forms.ChoiceField(label='Day to be reminded on', choices=DAY_CHOICES)
	class Meta:
		model = Contact
		fields = ['name', 'phone']

	def clean_phone(self):
		phone = self.cleaned_data['phone']

		parsed = utils.parse_phone_number(phone)
		if parsed == "1":
			self.add_error("phone", "Phone number is invalid")
		else:
			return parsed



class UpdateUserForm(forms.ModelForm):
	class Meta:
		model = Person
		fields = ('phone', )

class CreateUserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['first_name','last_name', 'email']

	def clean_email(self):
		email = self.cleaned_data.get('email')
		if email and User.objects.filter(email=email).count():
			raise forms.ValidationError(u'Someone has already used this email address!')
		return email

class CreatePersonForm(forms.ModelForm):
	class Meta:
		model = Person
		fields = ['phone']

	def clean_phone(self):
		phone = self.cleaned_data.get('phone')
		parsed = utils.parse_phone_number(phone)
		if parsed == "1":
			self.add_error("phone", "Phone number is invalid")
		elif Person.objects.filter(phone=parsed).count():
			self.add_error("phone", "Someone has already registered this number!")
		else:
			return parsed