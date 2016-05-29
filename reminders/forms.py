from django import forms
from reminders.models import Contact, Person
from django.contrib.auth.models import User

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

class UpdateUserForm(forms.ModelForm):
	class Meta:
		model = Person
		fields = ('phone', )

class CreateUserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['first_name','last_name', 'email']

class CreatePersonForm(forms.ModelForm):
	class Meta:
		model = Person
		fields = ['phone']