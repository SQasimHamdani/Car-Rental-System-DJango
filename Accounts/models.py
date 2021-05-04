from django.db import models
from django.conf import settings
from django.core.validators import *

from django.contrib.auth.models import User

# Create your models here.

class Person(models.Model):
    person  = models.OneToOneField(User, on_delete=models.CASCADE)
    name    = models.CharField(max_length = 50)
    address = models.CharField(max_length = 100)
    phone   = models.CharField(validators = [MinLengthValidator(8), MaxLengthValidator(15)], max_length = 15)
    
    # username = models.CharField(max_length = 100, null=True, unique=True)
    # email   = models.EmailField(null=True, default="")
    # password = models.CharField(null=True, max_length = 100)

    def __str__(self):
        return self.name
    
    def get_loggedin_user(self,request):
        user = Person.objects.all().filter(user = request.user)
        return user.name

class Employee(models.Model):
    employee = models.ForeignKey(Person, on_delete=models.CASCADE,related_name='employee')
    manager = models.ForeignKey(Person, on_delete=models.CASCADE,related_name='manager',blank=True,null=True)
    works_at_showroom = models.ForeignKey("system.Showroom", on_delete=models.CASCADE,related_name='works_at',blank=True,null=True)

    def __str__(self):
        return self.employee.name

class Customer(models.Model):
    customer = models.ForeignKey(Person, on_delete=models.CASCADE,related_name='customer')

    def __str__(self):
        return self.customer.name