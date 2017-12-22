from django.shortcuts import render
from django.views import generic
from .models import Project 
# Create your views here.

from django.http import HttpResponse

class ProjectListView(generic.ListView):
	template_name = 'projects/projects.html'
	context_object_name = 'project_list'
	def get_queryset(self):
		return Project.objects.order_by('-id').all()

class ProjectDetailView(generic.DetailView):
	model = Project
	template_name = 'projects/projectDetails.html'
	def get_queryset(self):
		return Project.objects.order_by('-id').all()
class HomeView(generic.TemplateView):
	template_name = 'home/home.html'

	
