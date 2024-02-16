from rest_framework import serializers, validators
from .models import *

def validate_age(value):
    if(value < 18):
        raise serializers.ValidationError("Age must be greater than 18.") 
    return value

unique_name = validators.UniqueValidator(SomeRandomTesting.objects.all())