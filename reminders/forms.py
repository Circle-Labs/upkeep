from django import forms
from reminders.models import Contact

DAY_CHOICES = (
	('M', 'Monday'),
	('T', 'Tuesday'),
	('W', 'Wednesday'),
	('H', 'Thursday'),
	('F', 'Friday'),
	('S', 'Saturday'),
	('U', 'Sunday'))

class AddContactForm(forms.ModelForm):
	update_time = forms.TimeField(label="Time to be reminded at", initial='14:00')
	update_day = forms.ChoiceField(label='Day to be reminded on', choices=DAY_CHOICES)
	class Meta:
		model = Contact
		fields = ['name', 'phone']
