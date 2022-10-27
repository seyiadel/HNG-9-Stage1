from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
# Create your views here.

class Intern_Information(APIView):

    def get(self, request):
        return JsonResponse(data={'slackUsername':'seyiadel',
        'backend':True,
        'age':19,
        'bio':'I turn ideas into software using python.'}, status=status.HTTP_200_OK)