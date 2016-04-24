from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

# Register your models here.

from .models import Contact, Person

admin.site.register(Contact)
admin.site.register(Person)

class PersonInline(admin.StackedInline):
	model = Person
	can_delete = False
	verbose_name_plural = 'person'

class UserAdmin(BaseUserAdmin):
	inlines = (PersonInline, )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)


