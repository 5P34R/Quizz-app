from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Question, Answer
from .serializers import QuestionSerializer


class QuestionView(APIView):
	def get(self, request, format=None):
		objs = Question.objects.all()
		serializer = QuestionSerializer(objs, many=True)
		return Response(
			serializer.data
			)

	def post(self, request, format=None):
		data = request.data 
		serializer = QuestionSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
		return Response(serializer.data)