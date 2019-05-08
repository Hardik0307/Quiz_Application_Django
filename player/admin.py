from django.contrib import admin
from .models import quiz_played,quiz_list
# Register your models here.
admin.site.register(quiz_played)
admin.site.register(quiz_list)