from django.db import models

# Create your models here.

class Question(models.Model):
	LEVEL = (
		('Hard', 'Hard'),
		('Medium', 'Medium'),
		('Easy', 'Easy'),
		)
	name = models.CharField(max_length=200)
	slug = models.SlugField()
	points = models.IntegerField()
	level = models.CharField(choices=LEVEL, max_length=10)


	def __str__(self):
		return self.name


class Answer(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	answer = models.CharField(max_length=200)
	correct = models.BooleanField(default=False)

	def __str__(self):
		return self.answer