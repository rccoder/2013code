from django.db import models

# Create your models here.

class People(models.Model):
    sm = models.CharField(max_length = 15)
    name = models.CharField(max_length=30)
    sex = models.BooleanField(default=True)
    birthday = models.CharField(max_length = 18)
    phone = models.CharField(max_length=11)
    qq = models.CharField(max_length = 10)
    email = models.EmailField()
    address = models.CharField(max_length=50)
    
    
   