from django.shortcuts import render
from django.http import HttpResponse
from . models import Que_Ans_Health,Que_Ans_Sports,Que_Ans_CS,Que_Ans_Mix
from Player.models import quiz_list
import Reg
import quiz_master
#from django.contrib.auth import authenticate, login, logout

# Create your views here.
def master_profile(request):
	return render(request,"quiz_master/master_profile.html")

def generate_quiz(request):
	print("quiz_master going to generate quiz....")
	return render(request,"quiz_master/generate_quiz.html")

def ask_que_cat(request):
	if request.method == 'POST' :
		print("IN ask_que_cat view...")
		#que = int(request.POST['quantity'])
		cat = request.POST['Category']
		#creator_id = request.session['user']
		#quiz_id = creator_id + cat + '01'
		l =list(range(1,10+1))
		print(l)
		request.session['Category'] = cat
		request.session['Number'] = 10
		request.session['id'] = request.POST['quiz_id']
		print(request.session['id'])
		#Quiz = Que_Ans(creator_id=creator_id,quiz_id = quiz_id )
		#Quiz.save()
		#print(que,cat,creator_id,quiz_id + "Data Saved.")
		return render(request,"quiz_master/generate_quiz.html",{'label' : 1,'list' : l  })

def submit_quiz(request):
	if request.method == 'POST' :
		print("Reached after Submission of Questions and data going to database..")
		print(request.session['id'])
		#x = request.session['Number']
		cat = request.session['Category']
		Quiz1=quiz_list(quiz_id=request.session['id'],Catagory=cat)
		Quiz1.save()
		for i in range(1,10+1):
			que_ip = 'que' + str(i)
			op1_ip = 'op1' + str(i)
			op2_ip = 'op2' + str(i)
			op3_ip = 'op3' + str(i)
			op4_ip = 'op4' + str(i)
			ans_ip = 'ans' + str(i)
			weight_ip = 'weight' + str(i)
			que = request.POST[que_ip]
			op1 = request.POST[op1_ip]
			op2 = request.POST[op2_ip]
			op3 = request.POST[op3_ip]
			op4 = request.POST[op4_ip]
			ans = request.POST[ans_ip]
			weight =request.POST[weight_ip]
			
			if cat == 'Health':
				Quiz = Que_Ans_Health(quiz_id=request.session['id'],question=que,op1=op1,op2=op2,op3=op3,op4=op4,ans=ans,weightage=weight)
			elif cat == 'Sports' :
				Quiz = Que_Ans_Sports(quiz_id= request.session['id'],question=que,op1=op1,op2=op2,op3=op3,op4=op4,ans=ans,weightage=weight)
			elif cat == 'CS' :
				Quiz = Que_Ans_CS(quiz_id=request.session['id'],question=que,op1=op1,op2=op2,op3=op3,op4=op4,ans=ans,weightage=weight)
			elif cat == 'Mix' :
				Quiz = Que_Ans_Mix(quiz_id= request.session['id'],question=que,op1=op1,op2=op2,op3=op3,op4=op4,ans=ans,weightage=weight)				
			#Que = Que_Ans(question=que,op1=op1,op2=op2,op3=op3,op4=op4,ans=ans)
			#Que_Ans.objects.filter().update(question=que,op1=op1,op2=op2,op3=op3,op4=op4,ans=ans)
			#Que.update()
			Quiz.save()
			#	del request.session['id']
		return render(request,"quiz_master/master_profile.html",{'Success' : 1})

def display_que(request):
	#cat = request.session['Category']
	cat = request.POST['Category']
	if cat == 'Health':
		Que_cat1 = Que_Ans_Health.objects.all()
	elif cat == 'Sports' :
		Que_cat1 = Que_Ans_Sports.objects.all()		
	elif cat == 'CS' :
		Que_cat1 = Que_Ans_CS.objects.all()		
	elif cat == 'Mix' :
		Que_cat1 = Que_Ans_Mix.objects.all()		
	return render(request,"quiz_master/display_que.html",{'Que_cat1' : Que_cat1})

def ask_delete_que(request):
	cat = request.POST['Category']
	request.session['UD'] = cat
	if cat == 'Health': 
		Que_cat1 =Que_Ans_Health.objects.all()
	elif cat == 'Sports': 
		Que_cat1 =Que_Ans_Sports.objects.all()	
	elif cat == 'CS': 
		Que_cat1 =Que_Ans_CS.objects.all()
	elif cat == 'Mix': 
		Que_cat1 =Que_Ans_Mix.objects.all()		
	return render(request,"quiz_master/ask_delete_que.html",{'Que_cat1' : Que_cat1})

def ask_update_que(request):
	cat = request.POST['Category']
	request.session['UD'] = cat
	if cat == 'Health': 
		Que_cat1 =Que_Ans_Health.objects.all()
	if cat == 'Sports': 
		Que_cat1 =Que_Ans_Sports.objects.all()
	if cat == 'CS': 
		Que_cat1 =Que_Ans_CS.objects.all()
	if cat == 'Mix': 
		Que_cat1 =Que_Ans_Mix.objects.all()		
	return render(request,"quiz_master/ask_update_que.html",{'Que_cat1' : Que_cat1})	

def delete_que(request):
	if request.method == 'POST' :
		Category=request.session['UD']
		Selection = request.POST.getlist('sel')

		if Category=='Health':
			for l in Selection :
				Que_Ans_Health.objects.filter(question = l).delete()
		elif Category=='Sports':
			for l in Selection :
				Que_Ans_Sports.objects.filter(question = l).delete()
		elif Category=='CS':
			for l in Selection :
				Que_Ans_CS.objects.filter(question = l).delete()
		elif Category=='Mix':
			for l in Selection :
				Que_Ans_Mix.objects.filter(question = l).delete()
		del request.session['UD']						
		return render(request,"quiz_master/master_profile.html",{'Success' : 1})
#for display update
def update_que(request):
	if request.method == 'POST' :
		sel = request.POST['same']
		Category = request.session['UD']
		if Category=='Health':
				Que = Que_Ans_Health.objects.get(question = sel)
		elif Category=='Sports':
				Que = Que_Ans_Sports.objects.get(question = sel)
		elif Category=='CS':
				Que = Que_Ans_CS.objects.get(question = sel)
		elif Category=='Mix':
				Que = Que_Ans_Mix.objects.get(question = sel)
		return render(request,"quiz_master/update.html",{'Que' : Que})
def update(request):
	if request.method == 'POST' :
		pk  = request.POST['pk']
		que = request.POST['que']
		op1 = request.POST['op1']
		op2 = request.POST['op2']
		op3 = request.POST['op3']
		op4 = request.POST['op4']
		ans = request.POST['ans']
		weight = request.POST['weight']
		Category = request.session['UD']
		if Category=='Health':
				Que = Que_Ans_Health.objects.filter(question=pk).update(question=que,op1=op1,op2 = op2,op3 =op3,op4 =op4,ans= ans,weightage=weight)
		elif Category=='Sports':
				Que = Que_Ans_Sports.objects.filter(question=pk).update(question=que,op1=op1,op2 = op2,op3 =op3,op4 =op4,ans= ans,weightage=weight)
		elif Category=='CS':
				Que = Que_Ans_CS.objects.filter(question=pk).update(question=que,op1=op1,op2 = op2,op3 =op3,op4 =op4,ans= ans,weightage=weight)
		elif Category=='Mix':
				Que = Que_Ans_Mix.objects.filter(question=pk).update(question=que,op1=op1,op2 = op2,op3 =op3,op4 =op4,ans= ans,weightage=weight)
		del request.session['UD']
		return render(request,"quiz_master/master_profile.html",{'Success' : 1})