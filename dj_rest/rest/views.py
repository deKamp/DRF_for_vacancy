from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import LessonsSerializer


class LessonsView(APIView):
    def get(self, request):
        lessons = Lesson.objects.all()
        serializer = LessonsSerializer(lessons, context={'request': request}, many=True)
        return Response(serializer.data)
