from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class empoly(models.Model):
    name=models.CharField(max_length=100)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    designation=models.CharField(max_length=100)
    salary=models.IntegerField()
    phone=models.IntegerField()

    def __str__(self):
        return self.name

   
    
     
