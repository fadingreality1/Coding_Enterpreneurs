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
        # ! if super() method is not used, below method is saved
        # serializer.save(name="from perbghvhjuyuyuykvhjvhjvbjhbjhbform_create method")
        return super().perform_create(serializer)
    
class StudentListAPIView(generics.ListAPIView):
    
    """
    Use ListCreateView instead of upper-two
    
    can create as well as return list.
    
    """
    queryset = Student.objects.all()
    
    def get_serializer_class(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return TestStudentSerializer
        else:
            return StudentSerializer
        
class StudentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    
    def get_serializer_class(self):
        if self.request.user.is_authenticated:
            return TestStudentSerializer
        else:
            return StudentSerializer
        
        
@api_view(['GET', 'POST'])
def bookList(req):
    if req.method == 'GET':
        books = Book.objects.all()
        if len(books) == 0:
            return Response({})
        serialized_books = BookSerializer(books, many = True)
        return Response(serialized_books.data)
    if req.method == 'POST':
        data = req.data
        serialized_data = BookSerializer(data = data)
        if serialized_data.is_valid(raise_exception = True):
            serialized_data.save()
            return Response(serialized_data.data)
        return Response({})
    return Response({})
    
    
            
# ! Creating functional based view that does exactly what these above Class based views have done

@api_view(['GET', 'POST'])
def allInOneForStudent(req, id = None,  *args):
    # For list and details view
    if req.method == 'GET':
        # For Detail
        if id != None:
            student_details = get_object_or_404(Student, id = id)
            serialized_data = StudentSerializer(student_details, many = False).data
            return Response(serialized_data)
        # for list
        students = Student.objects.all()
        serialized_students = TestStudentSerializer(students, many = True)
        return Response(serialized_students.data)
        
    elif req.method == 'POST':
        # For creation 
        serialized_data = StudentSerializer(data = req.data)
        if serialized_data.is_valid(raise_exception=True):
            serialized_data.save()
            return Response(serialized_data.data)
        
        
class DeleteStudentAPIView(generics.DestroyAPIView):
    queryset = Student.objects.all()
    lookup_field = 'id'
    
    
class UpdateStudentAPIView(generics.UpdateAPIView):
    queryset = Student.objects.all()
    lookup_field = 'id'
    serializer_class = StudentSerializer
    