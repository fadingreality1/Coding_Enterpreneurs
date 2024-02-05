from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializers import *


@api_view(['GET', 'POST'])
def apiHome(req):
    if req.method == 'GET':
        instance = Student.objects.all()
        instance = StudentSerializer(instance, many= True)
        return Response({'Hello':instance.data}, status=200) 
    
    elif req.method == 'POST':
        data = req.data
        ser = StudentSerializer(data = data)
        if ser.is_valid(raise_exception=True):
            ser.save()
            print(ser.data) 
            print("*************************")
            return Response(ser.data)
        return Response(ser.is_valid())