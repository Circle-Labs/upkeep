from django.conf.urls import url, include
from reminders import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'people', views.PersonViewSet)
router.register(r'contacts', views.ContactViewSet)

urlpatterns = [
	url(r'^api/', include(router.urls)),
	url(r'^user/create/$', views.PersonCreate.as_view(), name='create'),
	url(r'^user/(?P<pk>[0-9]+)/me/$', views.PersonUpdate.as_view(), name='me'),
	url(r'^user/(?P<pk>[0-9]+)/me/update/$', views.update, name='update'),
	url(r'^user/(?P<pk>[0-9]+)/contacts/$', views.yourContacts, name='contacts'),
]