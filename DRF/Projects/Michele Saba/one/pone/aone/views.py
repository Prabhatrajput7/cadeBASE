import imp
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Manufacture,Product
from django.http import JsonResponse
# Create your views here.
# https://github.com/pymike00/The-Complete-Guide-To-DRF-and-VueJS

class ProductDetails(DetailView):
    model = Product
    template_name = 'aone/details.html'

class ProductList(ListView):
    model = Product
    template_name = 'aone/list.html'    

def product_list(request):
    products = Product.objects.all()  # [:30]
    data = {"products": list(products.values())}  # .values("pk", "name") or .values("id", "name")
    response = JsonResponse(data)
    return response

def product_detail(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        response = JsonResponse(
            {"error": {"code": 404, "message": "product not found!"}}, status=404
        )
    else:
        data = {
            "product": {
                "name": product.name,
                "manufacturer": product.manufacture.name,
                "description": product.desc,
                "photo": product.photo.url,
                "price": product.price,
                "shipping_cost": product.ship_coast,
                "quantity": product.quality,
            }
        }
        response = JsonResponse(data)
    return response    

class ManuDetails(DetailView):
    model = Manufacture
    template_name = 'aone/mdetails.html'

    # def get_context_data(self,**kwargs):
    #     context =  super().get_context_data(**kwargs)
    #     manufacturer = Manufacture.objects.get(pk=self.kwargs['pk'])
    #     context['product'] = manufacturer.products.all()
    #     return context
    """
    pro {'object': <Manufacture: BMW>, 'manufacture': <Manufacture: BMW>, 'view': <aone.views.ManuDetails object at 0x0000018E7B6B2200>, 'product': <QuerySet 
    [<Product: S 1000 RR>, <Product: M 1000 RR>]>}
    """    

class ManuList(ListView):
    model = Manufacture
    template_name = 'aone/mlist.html'    


def manu_list(request):
    manufacture = Manufacture.objects.all()  # [:30]
    data = {"Manufacture": list(manufacture.values())}  # .values("pk", "name") or .values("id", "name")
    response = JsonResponse(data)
    return response

def manu_detail(request, pk):
    try:
        manufacture = Manufacture.objects.get(pk=pk)
    except Product.DoesNotExist:
        response = JsonResponse(
            {"error": {"code": 404, "message": "product not found!"}}, status=404
        )
    else:
        data = {
            "Manufacture": {
                "name": manufacture.name,
                "Location": manufacture.loc,
                "Active": manufacture.active,
                "Products": list(manufacture.products.values())
            }
        }
        response = JsonResponse(data)
    # print('value', manufacture.products.values())
    # print('all', manufacture.products.all())
    return response   

"""
m.products.all()
Out[5]: <QuerySet [<Product: S 1000 RR>, <Product: M 1000 RR>]>

In [6]: m.products.values()
Out[6]: <QuerySet [{'id': 1, 'manufacture_id': 1, 'name': 'S 1000 RR', 'desc': "Always pushing to the limit and in search of the ideal line, you've got 152 kW (207 hp) underneath you. Unbridled power pushes your RR to the max - with a maximum torque of 113 Nm at 11,000 rpm and a torque curve of at least 100 Nm over a range of 5,500 
to 14,500 [rpm].", 'photo': 'Capture.PNG', 'price': 15.0, 'ship_coast': 20.0, 'quality': 1}, {'id': 2, 'manufacture_id': 1, 'name': 'M 1000 RR', 'desc': 'Your competitive spirit drives you. Your passion dominates and challenges you. The search for more defines every millisecond: pure motorsport. High performance, high-tech materials, the highest-quality workmanship and exclusivity down to the last detail:', 'photo': 'Capture1.PNG', 'price': 12.0, 'ship_coast': 15.0, 'quality': 1}]>

list(m)
Out[4]: [<Manufacture: BMW>, <Manufacture: SpaceX>]

In [5]: list(m.values())
Out[5]: 
[{'id': 1, 'name': 'BMW', 'loc': 'Earth', 'active': True},
 {'id': 2, 'name': 'SpaceX', 'loc': 'Mars', 'active': True}]
 
"""