from __future__ import absolute_import

from celery import shared_task
import reminders.utils

from reminders.models import Contact

@shared_task
def send_sms(message):
	reminders.utils.send_sms("7068773908", message)

@shared_task
def check_reminders():
	reminders.utils.check_reminders()