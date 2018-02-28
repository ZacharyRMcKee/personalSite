from django.db import models
class Resume(models.Model):
	pdf = models.FileField(upload_to='personalSite/static')
	def __str__(self):
		return "Resume"

# Create your models here.
