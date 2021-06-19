from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Question, Answer
from .serializers import QuestionSerializer, AnswerSerializer


class QuestionView(APIView):
	def get(self, request, format=None):
		objs = Answer.objects.all()
		serializer = QuestionSerializer(objs, many=True)
		return Response(
			serializer.data
			)