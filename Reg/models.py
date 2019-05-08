from django.db import models

# Create your models here.
class User(models.Model):
	"""docstring for ClassName"""
	user_name = models.CharField(max_length=20)
	user_password = models.CharField(max_length=25)
	user_type = models.CharField(max_length=20)
	user_email = models.EmailField(max_length=70)
	user_points = models.IntegerField()
	
	def __str__(self):
		return 	self.user_name