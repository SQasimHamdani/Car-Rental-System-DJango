from django import forms

from .models import Showroom, SaleOrder, Car, Feedback

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = [
            "car_name",
            "description",
            "Manufacturer",
            "Model",
            "car_type",
            "num_of_seats",
            "cost_par_day",
            "car_photo",
            "status",
        ]
        
class SaleOrderForm(forms.ModelForm):
    class Meta:
        model = SaleOrder
        fields = [
            "car",
            "Order_Date",
            "Deliver_Date",
            "address",
        ]

# class ShowroomForm(forms.ModelForm):
#     class Meta:
#         model = Car
#         fields = [
#             "image",
#             "car_name",
#             "company_name",
#             "num_of_seats",
#             "cost_par_day",
#             "content",
#         ]

# class FeedbackForm(forms.ModelForm):
#     class Meta:
#         model = PrivateMsg
#         fields = [
#             "name",
#             "email",
#             "message",
#         ]
