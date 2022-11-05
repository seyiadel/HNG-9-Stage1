from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from hng9_stage2.serializers import CalculationSerializer


# Create your views here.
class Evaluate:
    def subtract(x,y):
        return x - y
    
    def add(x,y):
        return x + y

    def multiply(x,y):
        return x * y


class Task(APIView):
   def post(self, request):
    serializer = CalculationSerializer(data=request.data)
    if serializer.is_valid():
        operation=serializer.validated_data['operation_type']
        x=serializer.validated_data['x']
        y=serializer.validated_data['y']
        if operation == 'addition':
            return JsonResponse(data={"slackUsername":"seyiadel",
                                "operation_type":"addition",
                                'result': Evaluate.add(x,y)})
        elif operation == 'subtraction':
            return JsonResponse(data={"slackUsername":"seyiadel",
                                "operation_type":"subtraction",
                                'result': Evaluate.subtract(x,y)})
        elif operation == 'multiplication':
            return JsonResponse(data={"slackUsername":"seyiadel",
                                "operation_type":"multiplication",
                                'result': Evaluate.multiply(x,y)})
        else:
            return JsonResponse(data={"slackUsername":"seyiadel",
                                "operation_type":"Operation_type do not exist",
                                'result': "No Results"})
    return JsonResponse(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
