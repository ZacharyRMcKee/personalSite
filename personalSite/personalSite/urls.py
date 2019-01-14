"""personalSite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.shortcuts import redirect
from .views import *
from django.conf.urls import (handler400, handler403, handler404, handler500)
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('projects/',include('projects.urls'),name='project'),
    path('home/',include('home.urls'),name='home'),
    path('teaching/',include('teaching.urls'),name='teaching'),
    path('sandbox-1/',include('sandbox-1.urls'),name='sandbox-1'),
    path('',homeRedirect),
]

urlpatterns += staticfiles_urlpatterns()
