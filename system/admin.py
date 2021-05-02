from django.contrib import admin

# Register your models here.

from .models import Showroom, Car, SaleOrder, Feedback

admin.site.register(Showroom)
admin.site.register(Car)

admin.site.register(Feedback)
admin.site.register(SaleOrder)

