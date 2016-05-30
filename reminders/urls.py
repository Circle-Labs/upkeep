from django.conf.urls import url, include
from reminders import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'people', views.PersonViewSet)
router.register(r'contacts', views.ContactViewSet)

urlpatterns = [
	
	url(r'^user/create/$', views.create_person, name='create'),
	url(r'^user/me/$', views.update_person, name='me'),
	url(r'^user/declaim/(?P<contact>[0-9]+)/$', views.declaim_contact, name='declaim'),
	url(r'^user/contacts/$', views.your_contacts, name='contacts'),
	url(r'^user/logout/$', views.logout_view, name='user_logout'),
	url(r'^user/login/$', views.verification_view, name='user_login'),
	url(r'^user/login/(?P<number>[0-9]+)/$', views.login_view, name='user_verify_code'),
	url(r'^test/$', views.test, name='test'),
	url(r'^api/', include(router.urls)),
]