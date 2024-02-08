from django.db import models

class Student(models.Model):
    name = models.CharField(max_length = 255, null = False, default = 'John doe')
    age = models.IntegerField(null = False)
    
    @property
    def father(self):
        return 'kunal verma'
    
    def age_times_two(self):
        return self.age * 2
    
    
    def __str__(self):
        return f'{self.name}  {self.age}'
    

class Book(models.Model):
    name = models.CharField(max_length = 255, null = False)
    price = models.IntegerField(default = 100, null = False)
    
    @property
    def writer(self):
        return 'Kunal verma'
    
    def __str__(self):
        return f'{self.name}'
