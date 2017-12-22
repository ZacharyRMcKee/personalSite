from django.shortcuts import render
from django.views import generic
# Create your views here.

from django.shortcuts import redirect
from django.http import HttpResponse

def homeRedirect(request):
	return redirect('home/')
