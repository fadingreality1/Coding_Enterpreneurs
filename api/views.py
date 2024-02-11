from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from .models import *
from .serializers import *
from rest_framework import generics, permissions, authentication
from rest_framework.mixins import *

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
        
        
# ! creating Class based api views for update and delete

class DeleteStudentAPIView(generics.DestroyAPIView):
    queryset = Student.objects.all()
    lookup_field = 'id'
    
    # ! use when needed only
    def perform_destroy(self, instance):
        return super().perform_destroy(instance)
    
    
class UpdateStudentAPIView(generics.UpdateAPIView):
    queryset = Student.objects.all()
    lookup_field = 'id'
    serializer_class = StudentSerializer
    
    # ! use when neede only
    def perform_update(self, serializer):
        return super().perform_update(serializer)
    
# ! Using mixins

# ! we should avoid doing all stuff with single view, it poses security threat as every task is identified on the bases of request.method, not the url of route, so we can accidently delete something when list route is send with METHOD == DELETE.

class AllInOneForStudentWithMixin(
    ListModelMixin,
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    generics.GenericAPIView,
    
    ):
    
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field = 'id'
    
    # ? permissions and authentication
    
    
    authentication_classes = [authentication.SessionAuthentication]
    # permission_classes = [permissions.IsAuthenticated]
    # permission_classes = [permissions.DjangoModelPermissions]
    
    # For List View
    def get(self, request,*args, **kwargs):
        
        # ! if we want to use retrieve model mixin in one route with list model mixin, we shall use kwargs.
        
        id = kwargs.get('id')
        if id:
            #?  Using different serializer for detail requests
            self.serializer_class = StudentSerializer
            return self.retrieve(request, *args, **kwargs)
            
        return self.list(request, *args, **kwargs)
    
    # For Create View
    def post(self, request, *args, **kwargs):
        
        #? This function calls for perform_create() method
        
        return self.create(request, *args, **kwargs)


    def perform_create(self, serializer):
        print('\n\n Was it called??\n\n')
        serializer.save()
        # ! or use below line instead of above 
        # return super().perform_create(serializer)
        
        
    
    def patch(self, request, *args, **kwargs):
        
        # ? this method calls for perform_update method
        
        #! For partial updtion [not all fields are required]
        return self.partial_update(request, *args, **kwargs)
        #! For complete updtion [all fields are required]
        return self.update(request, *args, **kwargs)
    
    def perform_update(self, serializer):
        print('\n\n was i called for update \n\n??')
        # return super().perform_update(serializer)
        serializer.save()
        
    def delete(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
    
        
    

        
    
    
    