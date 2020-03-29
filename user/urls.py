
from django.urls import path, include

from . import api
from rest_framework import routers

# registering our api's url 
router = routers.DefaultRouter()
router.register('api/members-activity', api.MembersView, 'Member')


urlpatterns = [
   path('', include(router.urls)),   
   ]
