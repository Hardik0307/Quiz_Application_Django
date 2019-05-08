from django.conf.urls import url
from . import views
urlpatterns = [
		url(r'^profile/$',views.profile,name='profile'),
		url(r'^play_area/$',views.play_area,name='play_area'),
		url(r'^cat_dis_quiz/$',views.cat_dis_quiz,name='cat_dis_quiz'),
		url(r'^quiz/$',views.quiz,name='quiz'),
		url(r'^quiz_play/$',views.quiz_play,name='quiz_play'),
		url(r'^submit/$',views.submit,name='submit'),
]