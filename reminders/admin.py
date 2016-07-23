from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

# Register your models here.

from .models import Contact, Person, Beta

import utils


def inivite_to_beta(modeladmin, request, queryset):
		queryset.update(approved=True)
		emails = []
		for obj in queryset:
			emails.append(obj.email)
		utils.send_beta_accept(emails)

class BetaAdmin(admin.ModelAdmin):
	actions = [inivite_to_beta]

class PersonInline(admin.StackedInline):
	model = Person
	can_delete = False
	verbose_name_plural = 'person'

class UserAdmin(BaseUserAdmin):
	inlines = (PersonInline, )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(Contact)
admin.site.register(Person)
admin.site.register(Beta, BetaAdmin)