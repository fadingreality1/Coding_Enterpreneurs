from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from .models import *
from .serializers import *


@api_view(['GET', 'POST'])
def apiHome(req):
    if req.method == 'GET':
        instance = Student.objects.all()
        instance = StudentSerializer(instance, many= True)
        return Response(instance.data, status=200) 
    
    elif req.method == 'POST':
        data = req.data
        ser = StudentSerializer(data = data)
        # if ser.is_valid():
        if ser.is_valid(raise_exception=True):
            ser.save()
            print(ser.data) 
            print("*************************")
            return Response(ser.data)
        return Response(ser.is_valid())


@api_view(["GET"])
def studentDetails(req, id):
    student = get_object_or_404(Student,id = id)
    serialized_student = StudentSerializer(student)
    return Response(serialized_student.data)


# ! Django restframework generic views:


from rest_framework import generics
from .models import *


class StudentDetailAPIView(generics.RetrieveAPIView):
    # ? specifying which quesry set to be transferred
    queryset = Student.objects.all()
    
    
    # ! if we want custom query set, like two queryset merged into one or something like that.
    
    # def get_queryset(self):
    #     return Student.objects.all()
    
    # ? passing serializer to use
    
    lookup_field = 'id'
    
    # ! using different serializers
    
    # serializer_class = StudentSerializer

    def get_serializer_class(self):
        if self.request.method == "POST":
            return TestStudentSerializer
        else:
            return StudentSerializer
        
# ! Create API view
class StudentCreateAPIView(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = TestStudentSerializer
    
    def perform_create(self, serializer):
        print(serializer.validated_data)
        # ! if super() method is not used, below method is saved
        serializer.save(name="from perbghvhjuyuyuykvhjvhjvbjhbjhbform_create method")
        return super().perform_create(serializer)
    
    
