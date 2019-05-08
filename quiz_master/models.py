from django.db import models

# Create your models here.
class Que_Ans_Health(models.Model):
	quiz_id = models.CharField(max_length=40,primary_key=False)
	question = models.TextField(null =True)
	op1 = models.CharField(max_length=40, null =True)
	op2 = models.CharField(max_length=40, null =True)
	op3 = models.CharField(max_length=40, null =True)
	op4 = models.CharField(max_length=40, null =True)
	ans = models.CharField(max_length=40, null =True)
	weightage = models.IntegerField()

	def __str__(self):
		return self.question

class Que_Ans_Sports(models.Model):
	quiz_id = models.CharField(max_length=40,null=True)
	question = models.TextField(null =True)
	op1 = models.CharField(max_length=40, null =True)
	op2 = models.CharField(max_length=40, null =True)
	op3 = models.CharField(max_length=40, null =True)
	op4 = models.CharField(max_length=40, null =True)
	ans = models.CharField(max_length=40, null =True)
	weightage = models.IntegerField()

	def __str__(self):
		return self.question		

class Que_Ans_CS(models.Model):
	quiz_id = models.CharField(max_length=40,null=True)
	question = models.TextField(null =True)
	op1 = models.CharField(max_length=40, null =True)
	op2 = models.CharField(max_length=40, null =True)
	op3 = models.CharField(max_length=40, null =True)
	op4 = models.CharField(max_length=40, null =True)
	ans = models.CharField(max_length=40, null =True)
	weightage = models.IntegerField(null =True)

	def __str__(self):
		return self.question

class Que_Ans_Mix(models.Model):
	quiz_id = models.CharField(max_length=40,null=True)
	question = models.TextField(null =True)
	op1 = models.CharField(max_length=40, null =True)
	op2 = models.CharField(max_length=40, null =True)
	op3 = models.CharField(max_length=40, null =True)
	op4 = models.CharField(max_length=40, null =True)
	ans = models.CharField(max_length=40, null =True)
	weightage = models.IntegerField()

	def __str__(self):
		return self.question				