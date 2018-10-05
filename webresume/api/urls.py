from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()

# appends persn to the URL
router.register('person', views.PersonView)

# from the URLs available, append it the main URL i.e. person
urlpatterns = [
    path('',include(router.urls))
]
