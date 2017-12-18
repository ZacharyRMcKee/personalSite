from django.urls import path
from . import views

app_name = 'project'
urlpatterns = [
	path('',views.ProjectListView.as_view(),name='list'),
	path('<int:pk>/',views.ProjectDetailView.as_view(),name='detail')
]
