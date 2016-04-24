from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# 

PHONE_REGEX='^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$'


class Person(models.Model):
	user = models.OneToOneField(User, blank=True, on_delete=models.CASCADE)
	phone = models.CharField(max_length=100, validators=[RegexValidator(regex=PHONE_REGEX)])
	sms_verify_code = models.IntegerField(blank=True, null=True)
	contacts = models.ManyToManyField('Contact', blank=True)

	def __str__(self):
		return self.user.username

	def get_absolute_url(self):
		return reverse('me')


class Contact(models.Model):
	name = models.CharField(max_length=100)
	phone = models.CharField(max_length=100, validators=[RegexValidator(regex=PHONE_REGEX)])
	next_reminder = models.DateTimeField()
	frequency = models.DurationField()
	claimees = models.ManyToManyField('Person', through=Person.contacts.through, blank=True)

	def __str__(self):
		return self.name






