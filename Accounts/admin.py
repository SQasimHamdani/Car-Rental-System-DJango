from django.contrib import admin

from .models import Person, Employee, Customer

admin.site.register(Person)
admin.site.register(Employee)
admin.site.register(Customer)


# admin.site.Register()