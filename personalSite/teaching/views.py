from django.shortcuts import render
from django.views import generic
# Create your views here.
class TeachingView(generic.TemplateView):
	template_name = "teaching/teaching.html"
