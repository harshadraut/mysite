from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Question,Choice

class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 3

class QuestionAdmin(admin.ModelAdmin):
	fieldsets = [
	(None, {'fields': ['pub_date']}),
	('Data Information',{'fields':['question_text']})]
	inlines = [ChoiceInline]	
	list_display = ('question_text','pub_date','was_published_recently')
	

admin.site.register(Question,QuestionAdmin)

