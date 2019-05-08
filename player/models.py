from django.db import models 
from Reg.models import User
# Create your models here.
class quiz_played(models.Model):
	user_name = models.ForeignKey(User,on_delete=models.CASCADE)
	quiz_id = models.CharField(max_length=40)
	quiz_points = models.IntegerField()

class quiz_list(models.Model):
	quiz_id = models.CharField(max_length=20)
	Catagory = models.CharField(max_length=40)

	def __str__(self):
		return self.quiz_id