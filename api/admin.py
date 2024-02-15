from django.contrib import admin

from .models import *

admin.site.register([Book, Student, SomeRandomTesting])

# Register your models here.
