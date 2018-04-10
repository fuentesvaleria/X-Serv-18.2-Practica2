from django.db import models

# Create your models here.
# sigo este esquema
#class Person(models.Model):
    #first_name = models.CharField(max_length=30)
    #last_name = models.CharField(max_length=30)
    
class list_urls(models.Model):
	url_larga = models.CharField(max_length=64)
	
	def __str__(self):
		return self.url_larga