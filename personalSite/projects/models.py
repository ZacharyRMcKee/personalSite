from django.db import models

# Create your models here.

class Project(models.Model):
	name = models.CharField(max_length=50)
	source = models.URLField()
	summary = models.TextField()
	contents = models.TextField()
	def __str__(self):
		return self.name
	def getSummary(self):
		summary = self.contents[:97] + "..."
		return summary
