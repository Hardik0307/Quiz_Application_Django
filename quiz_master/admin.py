from django.contrib import admin
from . models import Que_Ans_Health,Que_Ans_Sports,Que_Ans_CS,Que_Ans_Mix 
# Register your models here.
admin.site.register(Que_Ans_Health)
admin.site.register(Que_Ans_Sports)
admin.site.register(Que_Ans_CS)
admin.site.register(Que_Ans_Mix)