from django.forms import ModelForm
from .models import Order, Customer


class OrderForm(ModelForm):
	class Meta:
		model = Order
		fields = '__all__'


class OrderFormCust(ModelForm):
	class Meta:
		model = Order
		fields = ['product','status']

class CustForm(ModelForm):
	class Meta:
		model = Customer
		fields = '__all__'