from django.urls import path
from .views import *

urlpatterns = [
	path('', index, name='item_list_url'),
]
