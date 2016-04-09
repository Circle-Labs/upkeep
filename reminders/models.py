from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.core.validators import RegexValidator
from django.db import models

# Create your models here.
# 

PHONE_REGEX='^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$'


class Person(models.Model):
	name = models.CharField(max_length=100)
	email = models.EmailField()
	phone = models.CharField(max_length=100, validators=[RegexValidator(regex=PHONE_REGEX)])
	smsVerifyCode = models.IntegerField(blank=True, null=True)
	contacts = models.ManyToManyField('Contact', blank=True)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('me', kwargs={'pk': self.pk})


class Contact(models.Model):
	name = models.CharField(max_length=100)
	phone = models.CharField(max_length=100, validators=[RegexValidator(regex=PHONE_REGEX)])
	nextReminder = models.DateTimeField()
	frequency = models.DurationField()
	claimees = models.ManyToManyField('Person', through=Person.contacts.through, blank=True)

	def __str__(self):
		return self.name






