from django.contrib import admin

# Register your models here.

from .models import Contact, Person

admin.site.register(Contact)
admin.site.register(Person)


