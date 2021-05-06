from django.db import models
from django.conf import settings
from django.core.validators import *
from django.contrib.auth.models import User
from django.utils.timezone import now
from system.extra_functionalities import resize_car_image
# Create your models here.

#Photos
import os
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from PIL import Image


class Showroom(models.Model):
    name    = models.CharField(validators = [MinLengthValidator(3), MaxLengthValidator(50)], max_length = 50)
    address = models.CharField(max_length = 100)
    contact = models.CharField(validators = [MinLengthValidator(10), MaxLengthValidator(15)], max_length = 15)

    def __str__(self):
        return self.name

class OverwriteStorage(FileSystemStorage):
    def get_available_name(self, name,max_length=40):
        if self.exists(name):
            os.remove(os.path.join(settings.CAR_PHOTOS, name))
        return name

def rename_car_profile_uploaded_file(self, filename):
    ext = filename.split('.')[-1]
    filename = "%s_%s.%s" % (self.car_name, self.id, ext)
    return os.path.join(settings.CAR_PHOTOS, filename)

class Car(models.Model):
    CAR_TYPE_CHOICES = (
                ('Mini','Savings with Mini Car'),
                ('Go','AC Car'),
                ('Go Plus','Luxurous Car'),
                )
    
    car_name = models.CharField(max_length=100)
    description = models.CharField(max_length = 100)

    Manufacturer = models.CharField(max_length=50)
    Model = models.CharField(max_length=50)
    
    car_type = models.CharField(max_length=100, choices=CAR_TYPE_CHOICES)
    num_of_seats = models.IntegerField()
    cost_par_day = models.IntegerField()

    car_photo = models.ImageField(default = 'car-images/car-default.png', upload_to=rename_car_profile_uploaded_file, storage=OverwriteStorage())
    status = models.IntegerField(default=0,null=True,blank=True)

    available = models.CharField(max_length=50,default="Available")

    showroom = models.ForeignKey("system.Showroom", on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.car_name

    def save(self):
        super().save()  # saving image first

        resize_car_image(self.car_photo.path)
        
        return
        
class SaleOrder(models.Model):
    # salesman = models.ForeignKey("Accounts.Employee", on_delete=models.CASCADE)
    customer = models.ForeignKey("Accounts.Customer", on_delete=models.CASCADE)

    showroom = models.ForeignKey(Showroom, on_delete=models.CASCADE,blank=True,null=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE,blank=True,null=True)

    address = models.CharField(max_length = 100,default="")

    Order_Date = models.DateField(blank=True,null=True)
    Deliver_Date = models.DateField(blank=True,null=True)

    def __str__(self):
        days = self.Deliver_Date - self.Order_Date
        return "customer-{} booked car-{} from showroom-{} for {} days".format(self.customer,self.car,self.showroom,days)

class Feedback(models.Model):
    customer = models.ForeignKey("Accounts.Customer", on_delete=models.CASCADE)
    order_id = models.ForeignKey(SaleOrder, on_delete=models.CASCADE,blank=True,null=True)

    Feedback_Date = models.DateTimeField(blank=True,null=True,default=now)
    message = models.CharField(max_length=200)
    rating = models.IntegerField(default=5)


    def __str__(self):
        return "{} left a {} star rating with feedback on order-{} as {} on {}".format(
            self.customer,
            self.rating,
            self.id,
            self.message,
            self.Feedback_Date)