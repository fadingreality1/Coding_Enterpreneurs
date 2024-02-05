from django.db import models

class Student(models.Model):
    name = models.CharField(max_length = 255, default = "kunal", null=True)
    age = models.IntegerField(default = 18, null = False)
    
    @property
    def father(self):
        return 'kunal verma'
    
    def age_times_two(self):
        return self.age * 2
    
    
    def __str__(self):
        return f'{self.name}  {self.age}'
