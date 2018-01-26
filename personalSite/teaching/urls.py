from django.urls import path
from .views import * 

app_name = 'teaching'
urlpatterns = [
	path('',TeachingView.as_view(),name='teaching'),
]
