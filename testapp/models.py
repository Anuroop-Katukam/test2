from django.db import models

# Create your models here.

class file(models.Model):
	field_name = models.FileField(upload_to='files/', max_length=254,null=True,blank=True)
	status = models.BooleanField(default =False)

class Simple(models.Model):
	GenderFreeForm = models.CharField(max_length=500,null=True,blank=True)	
	KaggleMotivationFreeForm = models.CharField(max_length=500,null=True,blank=True)
	CurrentJobTitleFreeForm = models.CharField(max_length=500,null=True,blank=True)
	MLToolNextYearFreeForm = models.CharField(max_length=500,null=True,blank=True)	
	