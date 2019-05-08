from django.shortcuts import render
from django.http import HttpResponse
from . models import User
import Reg
import quiz_master
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def index(request):
	print("Render to INDEX.html")
	a = User.objects.filter(user_points__gte = 30).values_list('user_name','user_points')
	b = sorted(sorted(a, key = lambda x : x[0]), key = lambda x : x[1], reverse = True)
	print(b)
	return render(request,"Reg/index.html",{"board" : b })
def signup_page(request):
	return render(request,"Reg/signup_page.html")

def signup(request):
	error = 0
	if request.method == 'POST':
		user_name = request.POST['uname']	
		password = request.POST['pass']
		password1 = request.POST['pass1']
		mail = request.POST['mail']
		print(password,password1)
		if password == password1:
			error = 0
			user = User(user_name=user_name,user_password=password,user_type=request.POST['Master'],user_email=mail,user_points = 30)
			user.save()		
			print("New User Registered.")
		else :
			error = 1
			
	return render(request,"Reg/signup_page.html",{'error' : error})		

def login_redirect(request):	
	return render(request,"Reg/login.html")

def login(request):	
	if request.method == 'POST': 
		user_name = request.POST['uname']
		password = request.POST['pass']
		#print(user_name)
		if User.objects.filter(user_name = user_name,user_password = password):
			print(User.objects.get(user_name =user_name,user_password = password))
			#str,x=User.objects.get(user_name =user_name,user_password = password)
			#print(x)
			points = User.objects.only('user_points').get(user_name=user_name,user_password=password).user_points
			utype = User.objects.only('user_type').get(user_name=user_name,user_password=password).user_type
			USER = User.objects.all()
			print(utype)
			print("ONE TUPLE")
			request.session['user'] = user_name
			print ("SESSION INVOKED -->Name  = " +request.session['user']+ " Logged in.")
			if utype == "Quiz-Master":
				return render(request,"quiz_master/master_profile.html",{"Data" : points})
			else:
				return render(request,"Player/profile.html",{"Data" : points})	
		else:
			print("NO TUPLES")
			return render(request,"Reg/login.html",{'error' : 1 })

def logout(request):
	try:
		del request.session['user']
		print("User Logged out.")
		return render(request,"Reg/logout.html")
	except Exception as e:
		raise e
#def generate_quiz(request):
#	return render(request,"quiz_master/generate_quiz.html")
				
	