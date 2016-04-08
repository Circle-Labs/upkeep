from reminders.models import Person, Contact
from rest_framework import serializers

class PersonSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Person
		fields = ('url', 'name', 'email', 'phone', 'contacts')

class ContactSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Contact
		fields = ('url', 'name', 'phone', 'nextReminder', 'frequency', 'claimees')
	