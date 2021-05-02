from django.db import models
from django.conf import settings
from django.core.validators import *

from django.contrib.auth.models import User
# Create your models here.

class Person(models.Model):
    person  = models.OneToOneField(User, on_delete=models.CASCADE)
    name    = models.CharField(validators = [MinLengthValidator(3), MaxLengthValidator(50)], max_length = 50)
    address = models.CharField(max_length = 100)
    phone   = models.CharField(validators = [MinLengthValidator(10), MaxLengthValidator(15)], max_length = 15)

    def __str__(self):
        return self.name

class Employee(models.Model):
    employee = models.ForeignKey(Person, on_delete=models.CASCADE,related_name='employee')
    username = models.CharField(max_length = 100,unique=True)
    email   = models.EmailField()
    password = models.CharField(max_length = 100)
    manager = models.ForeignKey(Person, on_delete=models.CASCADE,related_name='manager',blank=True,null=True)
    works_at_showroom = models.ForeignKey("system.Showroom", on_delete=models.CASCADE,related_name='works_at',blank=True,null=True)

    def __str__(self):
        return self.username

class Customer(models.Model):
    customer = models.ForeignKey(Person, on_delete=models.CASCADE,related_name='customer')
    username = models.CharField(max_length = 100,unique=True)
    email   = models.EmailField()
    password = models.CharField(max_length = 100)
    def __str__(self):
        return self.username

    
