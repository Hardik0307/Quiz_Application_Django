from django.conf.urls import url
from  . import views

urlpatterns =[
	url(r'^$',views.index,name='index'),
	url(r'^signup/$',views.signup,name='signup'),
	url(r'^signup_page/$',views.signup_page,name='signup_page'),
	url(r'^login_redirect/$',views.login_redirect,name='login_redirect'),
	url(r'^login/$',views.login,name='login'),
	url(r'^logout/$',views.logout,name='logout'),
	#url(r'^generate_quiz/$',views.generate_quiz,name='generate_quiz'),
]