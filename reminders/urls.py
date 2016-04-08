from django.conf.urls import url, include
from reminders import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'people', views.PersonViewSet)
router.register(r'contacts', views.ContactViewSet)

urlpatterns = [
	url(r'^', include(router.urls)),
]