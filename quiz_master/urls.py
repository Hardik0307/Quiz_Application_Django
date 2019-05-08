from django.conf.urls import url
from . import views
urlpatterns =[
	url(r'^master_profile/$',views.master_profile,name='master_profile'),
	url(r'^generate_quiz/$',views.generate_quiz,name='generate_quiz'),
	url(r'^ask_que_cat/$',views.ask_que_cat,name='ask_que_cat'),
	url(r'^submit_quiz/$',views.submit_quiz,name='submit_quiz'),
	url(r'^ask_delete_que/$',views.ask_delete_que,name='ask_delete_que'),
	url(r'^delete_que/$',views.delete_que,name='delete_que'),
	url(r'^display_que/$',views.display_que,name='display_que'),
	url(r'^ask_update_que/$',views.ask_update_que,name='ask_update_que'),
	url(r'^update_que/$',views.update_que,name='update_que'),
	url(r'^update/$',views.update,name='update'),
]