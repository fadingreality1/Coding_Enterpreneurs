from rest_framework import serializers
from .models import *

class StudentSerializer(serializers.ModelSerializer):
    my_father = serializers.SerializerMethodField(read_only=True)
    some_random_shit = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Student
        fields = [
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
        
    