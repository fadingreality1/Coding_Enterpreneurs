from rest_framework import serializers
from .models import *

class StudentSerializer(serializers.ModelSerializer):
    my_father = serializers.SerializerMethodField(read_only=True)
    some_random_shit = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Student
        fields = [
            'id', # ! should be avoided when transferring data outside.
            'name',
            'age',
            'my_father',
            'double_age',
            # 'age_times_two'
            'some_random_shit',
        ]
        
    # double_age = serializers.SerializerMethodField()
    
    double_age = serializers.SerializerMethodField(method_name='age_multiplier')
    # ! two way to do same thing with serializer method field
    
    def age_multiplier(self, obj):
        if not isinstance(obj, Student):
            return None
        if not hasattr(obj, 'id'):
            return None
        return  obj.age_times_two()
    
    def get_double_age(self, obj : Student):
        try:
            # ! when using post method, these fields are not accesible, that's why try catch
            # ? Have to implement different serializers to work around this problem.
            return obj.age_times_two()
        except:
            return None
        
    def get_my_father(self, obj):
        try:
            return obj.father
        except:
            return None
    
    def get_some_random_shit(self,obj):
        try:
            return obj.age**2
        except:
            return None
        

class TestStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        
        
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
    
    
    
class SomeRandomSerializer(serializers.ModelSerializer):
    
    owner = serializers.SerializerMethodField(method_name='get_owner')
    
    class Meta:
        model = SomeRandomTesting
        fields = ['id', 'name', 'owner']
        depth = 2
        
    def get_owner(self, obj):
        return obj.owner.username