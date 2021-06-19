from django.contrib import admin

from .models import Question, Answer

class AnswerInline(admin.TabularInline):
	model = Answer
	fields = [
		'answer',
		'correct'
	]

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
	fields = [
		'name',
		'points',
		'level'
	]

	list_display = [
		'name',
		'points'
	]

	inlines = [
		AnswerInline,
	]

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
	list_display = [
		'answer',
		'correct',
		'question'
	]


