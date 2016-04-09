from reminders.models import Person, Contact
from rest_framework import serializers

class PersonSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Person
		fields = ('url', 'id', 'name', 'email', 'phone', 'contacts')

class ContactSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Contact
		fields = ('url', 'id', 'name', 'phone', 'nextReminder', 'frequency', 'claimees')
