from django.shortcuts import render
from django.http import HttpResponse
from Player.models import quiz_list,quiz_played
from quiz_master.models import Que_Ans_Health,Que_Ans_Sports,Que_Ans_CS,Que_Ans_Mix
from Reg.models import User
import Reg
import quiz_master
# Create your views here.
def profile(request):
	points = User.objects.only('user_points').get(user_name= request.session['user']).user_points
	return render(request,"Player/profile.html",{'points' : points})
def play_area(request):
	l = ['Health','Sports','CS','Mix']
	return render(request,"Player/play_area.html",{'l':l})

def cat_dis_quiz(request):
	cat = request.GET.get('value')
	request.session['cat'] = cat
	#print(request.session['cat'])
	Que=quiz_list.objects.filter(Catagory = cat)
	print(Que)	
	return render(request,"Player/cat_dis_quiz.html",{'cat': cat,'Que' : Que})
 
def quiz(request):
	quiz_id = request.GET.get('value')
	quiz_cat = request.session['cat'] #SESSION
	request.session['quiz_id'] = quiz_id		
	return render(request,"Player/quiz.html",{'Cat' : quiz_cat})	

def quiz_play(request):
	quiz_id = request.session['quiz_id'] #SESSION
	quiz_cat = request.session['cat'] #SESSION 
	x = request.session['user'] #SESSION
	user =  User.objects.get(user_name = x)
	q1 = quiz_played.objects.filter(user_name=user)
	print(q1)
	for item in q1:
		if(item.quiz_id == quiz_id):
			return render(request,"Player/quiz_play.html",{'Que':item,'flag':1})		
	q = quiz_played(user_name=user,quiz_id = quiz_id,quiz_points =0)

	if quiz_cat == 'Sports' :
		Que = Que_Ans_Sports.objects.filter(quiz_id = quiz_id)
	elif quiz_cat == 'Health' :
		Que = Que_Ans_Health.objects.filter(quiz_id = quiz_id)
	elif quiz_cat == 'CS' :
		Que = Que_Ans_CS.objects.filter(quiz_id = quiz_id)
	elif quiz_cat == 'Mix' :
		Que = Que_Ans_Mix.objects.filter(quiz_id = quiz_id)		
	q.save()
	return render(request,"Player/quiz_play.html",{'Que':Que})		

def submit(request):
	l =[request.POST['0'],request.POST['1'],request.POST['2'],request.POST['3'],request.POST['4'],request.POST['5'],request.POST['6'],request.POST['7'],request.POST['8'],request.POST['9']]
	print(l)
	#l=l.reverse()
	quiz_id = request.session['quiz_id'] #SESSION
	quiz_cat = request.session['cat'] #SESSION
	x = request.session['user'] #SESSION
	user =  User.objects.get(user_name = x) 
	l1=[]
	if quiz_cat == 'Sports' :
		Que = Que_Ans_Sports.objects.filter(quiz_id = quiz_id)
	elif quiz_cat == 'Health' :
		Que = Que_Ans_Health.objects.filter(quiz_id = quiz_id)
	elif quiz_cat == 'CS' :
		Que = Que_Ans_CS.objects.filter(quiz_id = quiz_id)
	elif quiz_cat == 'Mix' :
		Que = Que_Ans_Mix.objects.filter(quiz_id = quiz_id)
	for j in Que:
		l1.append(j.ans)
	print(l1)		
	i=0
	point=0
	for item in Que:
		#print(item.ans,l[i])
		if(item.ans==l[i]):
			#print("true"+str(i))
			point=point+item.weightage
			#print(item.weightage)
		i=i+1
		
	current = User.objects.only('user_points').get(user_name= request.session['user']).user_points + point
	u =User.objects.filter(user_name=request.session['user']).update(user_points =current)
	per=(point/20)*100
	status = "NULL"
	if per == 100:
		status = "You are Abnormal.."
	elif per <100 and per>=90:
		status = "Genius!!"
	elif per<90 and per>=70:
		status = "Well done!!"
	elif per<70 and per>=36:
		status = "Well Try.."
	elif per<36 :
		status = "Needs Improvement"			
	Q=quiz_played.objects.filter(quiz_id=quiz_id,user_name=user).update(quiz_points=point)
	#Q.save()
	return render(request,"Player/submit.html",{"points":point,"per":per,"Que":Que,"l" : l,"status":status})	